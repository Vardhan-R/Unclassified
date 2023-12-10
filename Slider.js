function slider(sliderX, sliderY, sliderL, thing, minVal, maxVal) {
  if (mouseIsPressed) {
    if (sliderX <= mouseX && mouseX <= sliderX + sliderL && sliderY - 5 <= mouseY && mouseY <= sliderY + 5) {
      thing = map(mouseX, sliderX, sliderX + sliderL, minVal, maxVal)
    }
  }
  textAlign(CENTER)
  strokeWeight(1)
  stroke(0, 255, 0)
  line(sliderX, sliderY, sliderX + sliderL, sliderY)

  noStroke()
  fill(255, 255, 0)
  text(minVal, sliderX, sliderY)
  text(maxVal, sliderX + sliderL, sliderY)

  fill(255, 0, 0)
  circle(map(thing, minVal, maxVal, sliderX, sliderX + sliderL), sliderY, 10)

  fill(255, 255, 0)
  text(thing, map(thing, minVal, maxVal, sliderX, sliderX + sliderL), sliderY)

  return (thing)
}
