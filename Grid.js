function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  grid(4, 5, 0, 100)
}

function grid (r, c, colour, alp) {
  strokeWeight(1)
  stroke(colour, alp)
  for (i = 1; i < r; i++) {
    line(0, i * height / r, width, i * height / r)
  }
  for (i = 1; i < c; i++) {
    line(i * width / c, 0, i * width / c, height)
  }
}
