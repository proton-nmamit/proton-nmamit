class MatrixBackground {
    constructor() {
        this.section = document.getElementById('matrix-bg');
        this.numberOfSpans = Math.floor((window.innerWidth * window.innerHeight) / 5000);
    }

    createSpans() {
        for (let i = 0; i < this.numberOfSpans; i++) {
            const span = document.createElement('span');
            span.className = 'matrix-element';
            this.section.appendChild(span);
        }
    }

    init() {
        if (this.section) {
            this.createSpans();
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const matrix = new MatrixBackground();
    matrix.init();
});
