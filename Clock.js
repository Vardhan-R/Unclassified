let ls, lm, lh, ts, tm, th

function setup() {
  createCanvas(400, 400);
  ls = 150
  lm = 150
  lh = 100
  ts = -PI / 2
  tm = -PI / 2
  th = -PI / 2
  frameRate(1)
}

function draw() {
  background(220);
  textAlign(CENTER, CENTER)
  noStroke()
  for (i = 1; i < 13; i++) {
    text(i, lh * cos(-PI / 2 + i * PI / 6) + width / 2, lh * sin(-PI / 2 + i * PI / 6) + height / 2)
  }

  for (i = 0; i < 60; i++) {
      text(i, ls * cos(-PI / 2 + i * PI / 30) + width / 2, ls * sin(-PI / 2 + i * PI / 30) + height / 2)
  }
  stroke(255, 0 , 0)
  line(width / 2, height / 2, ls * cos(ts) + width / 2, ls * sin(ts) + height / 2)
  stroke(0)
  line(width / 2, height / 2, lm * cos(tm) + width / 2, lm * sin(tm) + height / 2)
  line(width / 2, height / 2, lh * cos(th) + width / 2, lh * sin(th) + height / 2)
  ts = ts + PI / 30
  tm = tm + PI / 1800
  th = th + PI / 21600
  if (ts > (2 * PI)) {
    ts = ts - 2 * PI
  }
  if (tm > (2 * PI)) {
    tm = tm - 2 * PI
  }
  if (th > (2 * PI)) {
    th = th - 2 * PI
  }
}
