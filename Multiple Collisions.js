let n, s, x, y, vx, vy, r, g, b, temp
let size = []
let xpos = []
let ypos = []
let velx = []
let vely = []
let rlst = []
let glst = []
let blst = []

function setup() {
  n = 5
  createCanvas(600, 500);
  noStroke()

  for (i = 0; i < n; i++) {
    s = random(10, 40)
    x = round(random(0, width - s))
    y = round(random(0, height - s))
    vx = round(random(-10, 10))
    vy = round(random(-10, 10))
    r = round(random(100, 255))
    g = round(random(100, 255))
    b = round(random(100, 255))

    size[i] = s
    xpos[i] = x
    ypos[i] = y
    velx[i] = vx
    vely[i] = vy
    rlst[i] = r
    glst[i] = g
    blst[i] = b
  }
}

function draw() {
  background(0);

  for (i = 0; i < n; i++) {
    for (j = (i + 1); j < n; j++) {
      if (((xpos[i] + size[i]) >= xpos[j]) && (xpos[i] <= (xpos[j] + size[j])) && ((ypos[i] + size[i]) >= ypos[j]) && (ypos[i] <= (ypos[j] + size[j]))) {
        if (abs(xpos[i] - xpos[j]) > abs(ypos[i] - ypos[j])) {
          temp = velx[i]

          velx[i] = (((size[i]) ** 2 - (size[j]) ** 2) * velx[i] + 2 * (velx[j]) * (size[j]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)

          velx[j] = (((size[j]) ** 2 - (size[i]) ** 2) * velx[j] + 2 * temp * (size[i]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)

        } else if (abs(xpos[i] - xpos[j]) < abs(ypos[i] - ypos[j])) {
          temp = vely[i]

          vely[i] = (((size[i]) ** 2 - (size[j]) ** 2) * vely[i] + 2 * (vely[j]) * (size[j]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)

          vely[j] = (((size[j]) ** 2 - (size[i]) ** 2) * vely[j] + 2 * temp * (size[i]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)

        } else {
          temp = velx[i]

          velx[i] = (((size[i]) ** 2 - (size[j]) ** 2) * velx[i] + 2 * (velx[j]) * (size[j]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)

          velx[j] = (((size[j]) ** 2 - (size[i]) ** 2) * velx[j] + 2 * temp * (size[i]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)

          temp = vely[i]

          vely[i] = (((size[i]) ** 2 - (size[j]) ** 2) * vely[i] + 2 * (vely[j]) * (size[j]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)

          vely[j] = (((size[j]) ** 2 - (size[i]) ** 2) * vely[j] + 2 * temp * (size[i]) ** 2) / ((size[i]) ** 2 + (size[j]) ** 2)
        }
        rlst[i] = random(100, 255)
        glst[i] = random(100, 255)
        blst[i] = random(100, 255)
        rlst[j] = random(100, 255)
        glst[j] = random(100, 255)
        blst[j] = random(100, 255)
      }
    }

    if ((xpos[i] <= 0) || ((xpos[i] + size[i]) >= width)) {
      velx[i] = -velx[i]

      rlst[i] = random(100, 255)
      glst[i] = random(100, 255)
      blst[i] = random(100, 255)
      rlst[j] = random(100, 255)
      glst[j] = random(100, 255)
      blst[j] = random(100, 255)
    }

    if ((ypos[i] <= 0) || ((ypos[i] + size[i]) >= height)) {
      vely[i] = -vely[i]

      rlst[i] = random(100, 255)
      glst[i] = random(100, 255)
      blst[i] = random(100, 255)
      rlst[j] = random(100, 255)
      glst[j] = random(100, 255)
      blst[j] = random(100, 255)
    }
  }



  for (i = 0; i < n; i++) {
    xpos[i] += velx[i]
    ypos[i] += vely[i]
  }



  for (i = 0; i < n; i++) {
    fill(rlst[i], glst[i], blst[i])
    square(xpos[i], ypos[i], size[i])
  }
}
