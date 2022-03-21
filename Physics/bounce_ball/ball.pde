public class Ball {

  float xpos;
  float ypos;
  float cwid;
  float chei;
  float radius;
  float ySpeed;
  float xSpeed;

  Ball(int xpos, int ypos, int cwid, int chei) {
    this.xpos = xpos;
    this.ypos = ypos;
    this.cwid = cwid;
    this.chei = chei;
    this.ySpeed = ySpeed;
    this.xSpeed = xSpeed;
    this.radius = cwid/2;
    this.xSpeed = 0;
    render();
  }

  void render() {
    fill(0);
    //ellipseMode(RADIUS);
    ellipse(xpos, ypos, cwid, chei);
  }

  void move() {
    noStroke();
    
    xSpeed = 10;
    ySpeed += gravity;
    ypos += ySpeed;
    xpos += xSpeed;
    System.out.println(cwid);
    if (ypos >= height -100-radius) {
      ypos = height - 100 - radius;
      ySpeed *= -0.85;
      //this.xSpeed *= 0.75;
      if (xpos >= width/2 && xpos <= width/2+100) {
        ySpeed *= 10;
      }
    } else if (ypos <= 0 +radius) {
      ypos = 0+radius;
      ySpeed *= -0.85;
    }
    if (xpos >= width) {
      xpos = 0;
    }
  }

  void velo() {
    stroke(255);
    line(xpos, ypos, xpos+xSpeed*5, ypos+ySpeed*5);
  }
}
