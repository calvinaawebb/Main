public class Ball {

  public PVector coords;
  float cwid;
  float chei;
  float radius;
  public PVector speed;

  Ball(float xpos, float ypos, float cwid, float chei) {
    coords = new PVector(xpos, ypos);
    this.cwid = cwid;
    this.chei = chei;
    speed = new PVector();
    this.radius = cwid/2;
    speed.x = 10;
    render();
  }

  void render() {
    fill(0);
    //ellipseMode(RADIUS);
    ellipse(coords.x, coords.y, cwid, chei);
  }

  void move(float t) {
    noStroke();
    speed.y += gravity/t;
    coords.y += speed.y/t;
    coords.x += speed.x/t;
    if (coords.y >= height -100-radius) {
      coords.y = height - 100 - radius;
      speed.y *= -0.85;
      speed.x *= 0.95;
      /*
      tramp:
      if (coords.x >= width/2 && coords.x <= width/2+100) {
        speed.y *= 2;
        speed.x *= 1.5;
      }
      */
    } else if (coords.y <= 0 +radius) {
      coords.y = 0+radius;
      speed.y *= -0.85;
    }
    if (coords.x >= width) {
      coords.x = width - 25;
      speed.x *= -0.50;
    } else if (coords.x <= 0) {
        coords.x = radius;
        speed.x *= -0.50;
    }
  }

  void velo() {
    stroke(255);
    line(coords.x, coords.y, coords.x+speed.x*5, coords.y+speed.y*5);
  }
}
