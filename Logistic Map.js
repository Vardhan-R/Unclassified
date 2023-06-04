let x

function setup() {
  createCanvas(400, 400);
  background(0);
  x = 0.6
  stroke(0, 255, 0)
  for (let f = 100; f < 400; f++) {
    x = f * x * (1 - x) / 100
    point(width * f / 400, height * (1 - x))
  }
}

function draw() {

}
