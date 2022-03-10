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
    ellipse(this.xpos, this.ypos, this.cwid, this.chei);
  }
  
  void move() {
    //this.xSpeed = 5;
    this.ySpeed += gravity;
    this.ypos += this.ySpeed;
    this.xpos += this.xSpeed;
    System.out.println(cwid);
    if (ypos >= height -100-radius) {
      this.ypos = height - 100 - radius;
      this.ySpeed *= -0.5;
      //this.xSpeed *= 0.75;
    }
  }
}
