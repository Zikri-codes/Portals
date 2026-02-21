// script.js – full interactivity, dark mode default with toggle

// DOM elements
const xInput = document.getElementById('xInput');
const yInput = document.getElementById('yInput');
const zInput = document.getElementById('zInput');
const outputX = document.getElementById('outputX');
const outputY = document.getElementById('outputY');
const outputZ = document.getElementById('outputZ');
const outputCombined = document.getElementById('outputCombined');
const convertBtn = document.getElementById('convertBtn');
const toNetherBtn = document.getElementById('toNether');
const toOverworldBtn = document.getElementById('toOverworld');
const darkToggle = document.getElementById('darkModeToggle');
const copyBtns = document.querySelectorAll('.copy-btn');

// state: true = overworld -> nether (/8), false = nether -> overworld (*8)
let toNether = true;

// format number: avoid .0, max 5 decimals
function formatCoord(num) {
    if (num === null || num === undefined || isNaN(num)) return null;
    let rounded = Math.round(num * 1e5) / 1e5;
    return Number.isInteger(rounded) ? rounded.toString() : rounded.toString();
}

// main conversion
function convert() {
    let x = parseFloat(xInput.value.trim());
    let z = parseFloat(zInput.value.trim());
    let y = yInput.value.trim() === '' ? null : parseFloat(yInput.value.trim());

    if (isNaN(x)) x = 0;
    if (isNaN(z)) z = 0;
    if (y !== null && isNaN(y)) y = null;

    let outX, outY, outZ;
    if (toNether) {
        outX = x / 8;
        outZ = z / 8;
        outY = y;
    } else {
        outX = x * 8;
        outZ = z * 8;
        outY = y;
    }

    const fmtX = formatCoord(outX) ?? '0';
    const fmtZ = formatCoord(outZ) ?? '0';
    const fmtY = outY !== null ? formatCoord(outY) : null;

    outputX.textContent = fmtX;
    outputZ.textContent = fmtZ;
    outputY.textContent = fmtY !== null ? fmtY : '-';

    const combined = fmtY !== null ? `${fmtX} ${fmtY} ${fmtZ}` : `${fmtX} ${fmtZ}`;
    outputCombined.textContent = combined;
}

// update active button styles (via data attribute)
function setDirection(nether) {
    toNether = nether;
    toNetherBtn.dataset.active = nether;
    toOverworldBtn.dataset.active = !nether;
    convert();
}

// copy to clipboard with icon feedback
async function copyText(text, btn) {
    if (!text) text = '';
    try {
        await navigator.clipboard.writeText(text);
        const icon = btn.querySelector('i');
        const original = icon.className;
        icon.className = 'fas fa-check';
        setTimeout(() => {
            icon.className = original;
        }, 700);
    } catch (err) {
        alert('Copy failed');
    }
}

// ---- event listeners ----
toNetherBtn.addEventListener('click', () => setDirection(true));
toOverworldBtn.addEventListener('click', () => setDirection(false));

convertBtn.addEventListener('click', convert);
[xInput, yInput, zInput].forEach(input => input.addEventListener('input', convert));

copyBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        const type = btn.dataset.copy;
        let text = '';
        if (type === 'x') text = outputX.textContent;
        else if (type === 'y') text = outputY.textContent === '-' ? '' : outputY.textContent;
        else if (type === 'z') text = outputZ.textContent;
        else if (type === 'combined') text = outputCombined.textContent;
        copyText(text, btn);
    });
});

// dark mode toggle
darkToggle.addEventListener('click', () => {
    document.body.classList.toggle('light');
    const icon = darkToggle.querySelector('i');
    if (document.body.classList.contains('light')) {
        icon.className = 'fas fa-moon';
    } else {
        icon.className = 'fas fa-sun';
    }
});

// initialise: dark mode is default (no light class)
setDirection(true);
darkToggle.querySelector('i').className = 'fas fa-sun';

// optional: enter key triggers convert
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') convert();
});