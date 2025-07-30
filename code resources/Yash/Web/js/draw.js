import { resumeAudio } from './app.js';

// --- Sequencer Globals ---
const cols = 8; // Steps
const rows = 7; // Notes: C D E F G A B
const whiteNotes = [71, 69, 67, 65, 64, 62, 60]; // MIDI notes reversed
const windowWidth = window.innerWidth;

let grid = [];
let currentStep = 0;
let cellSize = 40;
let cellHeight = 20;
let bpm = 120;
let tempo = (60 / bpm) * 1000;
let deviceRef = null;

export function initSequencer(device) {
    deviceRef = device;
    cellSize = windowWidth / cols;
    cellHeight = cellSize / 2;

    createGrid();
    const canvas = createCanvas();
    const ctx = canvas.getContext("2d");

    createBPMControl(canvas);
    createStartStopButton(canvas);
    setupCanvasClick(canvas, ctx);
    drawGrid(ctx);

    startSequencer(ctx);
}

function createGrid() {
    for (let i = 0; i < cols; i++) {
        grid[i] = Array(rows).fill(false);
    }
}

function createCanvas() {
    const canvas = document.createElement("canvas");
    canvas.width = windowWidth;
    canvas.height = rows * cellHeight;
    canvas.style.border = "1px solid gray";
    canvas.style.marginTop = "20px";
    canvas.id = "seq-canvas";
    document.body.appendChild(canvas);
    return canvas;
}

function createBPMControl(beforeElement) {
    const bpmDiv = document.createElement("div");
    bpmDiv.style.margin = "20px 0";

    const bpmLabel = document.createElement("label");
    bpmLabel.textContent = "BPM: ";
    bpmLabel.setAttribute("for", "bpm-input");

    const bpmInput = document.createElement("input");
    bpmInput.type = "number";
    bpmInput.id = "bpm-input";
    bpmInput.value = bpm;
    bpmInput.min = 30;
    bpmInput.max = 300;
    bpmInput.style.width = "60px";
    bpmInput.style.marginRight = "10px";

    bpmInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            bpm = parseInt(bpmInput.value) || 120;
            tempo = (60 / bpm) * 1000;
        }
    });

    bpmDiv.append(bpmLabel, bpmInput);
    document.body.insertBefore(bpmDiv, beforeElement);
}

function createStartStopButton(beforeElement) {
    const startButton = document.createElement("button");
    startButton.className = "start-button";

    const playIcon = document.createElement("span");
    playIcon.textContent = "▶";
    playIcon.className = "icon play-icon";

    const pauseIcon = document.createElement("span");
    pauseIcon.textContent = "❚❚";
    pauseIcon.className = "icon pause-icon";
    pauseIcon.style.display = "none";

    startButton.append(playIcon, pauseIcon);
    document.body.insertBefore(startButton, beforeElement);

    startButton.addEventListener("click", resumeAudio);
}

function setupCanvasClick(canvas, ctx) {
    canvas.addEventListener("click", (e) => {
        const rect = canvas.getBoundingClientRect();
        const x = Math.floor((e.clientX - rect.left) / cellSize);
        const y = Math.floor((e.clientY - rect.top) / cellHeight);

        if (grid[x] && typeof grid[x][y] !== "undefined") {
            grid[x][y] = !grid[x][y];
            drawGrid(ctx);
        }
    });
}

function drawGrid(ctx) {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
            const isActive = grid[i][j];
            const isCurrentStep = i === currentStep;
            ctx.fillStyle = isActive
                ? (isCurrentStep ? "#00FFAA" : "#FFF")
                : (isCurrentStep ? "#333" : "#777");
            ctx.strokeStyle = "#222";
            ctx.fillRect(i * cellSize, j * cellHeight, cellSize - 1, cellHeight - 1);
            ctx.strokeRect(i * cellSize, j * cellHeight, cellSize - 1, cellHeight - 1);
        }
    }
}

function startSequencer(ctx) {
    let running = true;
    
    function step() {
        if (!running) return;

        for (let j = 0; j < rows; j++) {
            if (grid[currentStep][j]) {
                triggerRNBONote(whiteNotes[j], 100);
            }
        }

        currentStep = (currentStep + 1) % cols;
        drawGrid(ctx);
        setTimeout(step, tempo);
    }

    step();
}

function triggerRNBONote(note, duration = 250) {
    if (!deviceRef) return;

    const midiChannel = 0;
    const noteOn = [144 + midiChannel, note, 100];
    const noteOff = [128 + midiChannel, note, 0];
    const tNow = deviceRef.context.currentTime * 1000;

    const onEvent = new RNBO.MIDIEvent(tNow, 0, noteOn);
    const offEvent = new RNBO.MIDIEvent(tNow + duration, 0, noteOff);

    deviceRef.scheduleEvent(onEvent);
    deviceRef.scheduleEvent(offEvent);
}
