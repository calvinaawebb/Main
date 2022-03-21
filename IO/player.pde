class Player {

  float xpos;
  float ypos;
  float radius;
  float speed;
  float speeD;
  String classType;
  color rcolor;
  

  Player(float xpos, float ypos, float radius, float speed, String classType, color rcolor) {
    this.xpos = xpos;
    this.ypos = ypos;
    this.radius = radius;
    this.speed = speed;
    speeD = sqrt((speed*speed)/2);
    this.classType = classType;
    this.rcolor = rcolor;
  }
  
  void move() {
    if (keyState[2] == true && keyState[3] == true) {
      this.xpos += speeD;
      this.ypos -= speeD;
    } else if (keyState[0] == true && keyState[3] == true) {
      this.xpos -= speeD;
      this.ypos -= speeD;
    } else if (keyState[2] == true && keyState[1] == true) {
      this.xpos += speeD;
      this.ypos += speeD;
    } else if (keyState[0] == true && keyState[1] == true) {
      this.xpos -= speeD;
      this.ypos += speeD;
    } else if (keyState[0] == true) {
      //left
      this.xpos -= this.speed;
    } else if (keyState[2] == true) {
      //right
      this.xpos += this.speed;
    } else if (keyState[3] == true) {
      //up
      this.ypos -= this.speed;
    } else if (keyState[1] == true) {
      //down
      this.ypos += this.speed;
    }
  }

  void render() {
    fill(this.rcolor);
    ellipse(this.xpos, this.ypos, this.radius, this.radius);
  }
}
