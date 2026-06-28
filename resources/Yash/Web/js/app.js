import { initSequencer } from './draw.js';

let rotationAlphaParam, rotationBetaParam, rotationGammaParam, context;
let isPlaying = false;
let playIcon, pauseIcon;

// Main setup function, initializes audio, loads patch, sets up UI
async function setup() {
    const patchExportURL = "export/hspwmrnbo.export.json";

    // Create AudioContext (cross-browser)
    const WAContext = window.AudioContext || window.webkitAudioContext;
    context = new WAContext();

    // Output node
    const outputNode = context.createGain();
    outputNode.connect(context.destination);

    // Fetch and parse exported patcher JSON
    const response = await fetch(patchExportURL);
    const patcher = await response.json();

    // Load RNBO script for the correct version
    await loadRNBOScript(patcher.desc.meta.rnboversion);

    // Create RNBO device from patcher
    const device = await RNBO.createDevice({ context, patcher });
    device.node.connect(outputNode);

    // Get references to orientation parameters from the rnbo patch
    rotationAlphaParam = device.parametersById.get('rotationAlpha');
    rotationBetaParam = device.parametersById.get('rotationBeta');
    rotationGammaParam = device.parametersById.get('rotationGamma');

    // Update UI with patcher info
    document.getElementById("patcher-title").innerText =
        `${patcher.desc.meta.filename || "Unnamed Patcher"} (v${patcher.desc.meta.rnboversion})`;

    // Create parameter sliders and sequencer UI
    makeSliders(device);
    initSequencer(device);

    // Start with audio context suspended (required by browsers)
    context.suspend(); // Wait for user interaction
}

// Handles play/pause and UI icon toggling
export function resumeAudio() {

    playIcon = document.querySelector(".play-icon");
    pauseIcon = document.querySelector(".pause-icon");

    if (!isPlaying) {
        context.state !== 'running' && context.resume();
        isPlaying = true;
        readOrient(); // Start reading device orientation
        if (playIcon && pauseIcon) {
            playIcon.style.display = "none";
            pauseIcon.style.display = "inline";
        }
    } else {
        isPlaying = false;
        context.state === 'running' && context.suspend();
        if (playIcon && pauseIcon) {
            pauseIcon.style.display = "none";
            playIcon.style.display = "inline";
        }
    }
}

// Dynamically loads the RNBO script for the given version
function loadRNBOScript(version) {
    return new Promise((resolve, reject) => {
        if (/^\d+\.\d+\.\d+-dev$/.test(version)) {
            throw new Error("Patcher exported with a Debug Version!");
        }

        const script = document.createElement("script");
        script.src = `https://c74-public.nyc3.digitaloceanspaces.com/rnbo/${encodeURIComponent(version)}/rnbo.min.js`;
        script.onload = resolve;
        script.onerror = () => reject(new Error(`Failed to load rnbo.js v${version}`));
        document.body.append(script);
    });
}

// Creates sliders and text inputs for each RNBO parameter
function makeSliders(device) {
    const pdiv = document.getElementById("rnbo-parameter-sliders");
    const noParamLabel = document.getElementById("no-param-label");
    if (noParamLabel && device.numParameters > 0) {
        pdiv.removeChild(noParamLabel);
    }

    let isDragging = false; // Prevents UI update while dragging
    const uiElements = {};

    device.parameters.forEach(param => {
        // Create label for parameter
        const label = document.createElement("label");
        label.setAttribute("class", "param-label");
        label.textContent = `${param.name}:`;

        // Create slider for parameter
        const slider = document.createElement("input");
        slider.type = "range";
        slider.className = "param-slider";
        slider.min = param.min;
        slider.max = param.max;
        slider.step = param.steps > 1
            ? (param.max - param.min) / (param.steps - 1)
            : (param.max - param.min) / 1000;
        slider.value = param.value;

        // Create text input for precise value entry
        const text = document.createElement("input");
        text.type = "text";
        text.value = param.value.toFixed(1);

        // Container for label, slider, and text input
        const container = document.createElement("div");
        container.append(label, slider, text);
        pdiv.appendChild(container);

        // Handle slider drag state
        slider.addEventListener("pointerdown", () => isDragging = true);
        slider.addEventListener("pointerup", () => {
            isDragging = false;
            slider.value = param.value;
            text.value = param.value.toFixed(1);
        });

        // Update parameter value from slider
        slider.addEventListener("input", () => {
            param.value = parseFloat(slider.value);
        });

        // Update parameter value from text input
        text.addEventListener("keydown", e => {
            if (e.key === "Enter") {
                let val = parseFloat(text.value);
                if (!isNaN(val)) {
                    val = Math.min(param.max, Math.max(param.min, val));
                    text.value = val;
                    param.value = val;
                } else {
                    text.value = param.value.toFixed(1);
                }
            }
        });

        uiElements[param.id] = { slider, text };
    });

    // Listen for parameter changes from device and update UI
    device.parameterChangeEvent.subscribe(param => {
        if (!isDragging) {
            uiElements[param.id].slider.value = param.value;
            uiElements[param.id].text.value = param.value.toFixed(1);
        }
    });
}

// Reads device orientation and updates RNBO parameters accordingly
function readOrient() {
    if (window.DeviceOrientationEvent) {
        window.addEventListener(
            "deviceorientation",
            (event) => {
                const frontToBack = event.beta; // beta: front back motion   [-180.0 - 180.0]    
                const leftToRight = event.gamma; // gamma: left to right [-90.0 - 90.0]
                const rotateDegrees = event.alpha; // alpha: rotation around z-axis [0.0 - 360.0]
                console.log("Front to Back:", frontToBack, "Left to Right:", leftToRight, "Rotate Degrees:", rotateDegrees);    

                handleOrientationEvent(frontToBack, leftToRight, rotateDegrees);
            },
            true,
        );
    }

    // Updates parameter values with orientation data
    const handleOrientationEvent = (frontToBack, leftToRight, rotateDegrees) => {
        rotationAlphaParam.value = rotateDegrees;
        rotationBetaParam.value = frontToBack;
        rotationGammaParam.value = leftToRight;
    };
}

// Start setup on load
setup();
