class Player {

  // player variables
  PVector pos;
  int radius;
  float speed;
  float speeD;
  String classType;
  String basen;
  PImage base;
  
  PVector mousePV = new PVector(mouseX, mouseY);

  // gun variables
  PVector g = new PVector();
  PImage blaster;
  String blastern;
  int gRad;

  Player(float xpos, float ypos, int radius, float speed, String classType, String basen, String blastern) {
    pos = new PVector(xpos, ypos);
    this.radius = radius;
    this.speed = speed;
    speeD = sqrt((speed*speed)/2);
    this.classType = classType;
    this.basen = basen;
    this.blastern = blastern;
    gRad = this.radius;
  }

  void move() {
    if (keyState[2] == true && keyState[3] == true) {
      this.pos.x += speeD;
      this.pos.y -= speeD;
    } else if (keyState[0] == true && keyState[3] == true) {
      this.pos.x -= speeD;
      this.pos.y -= speeD;
    } else if (keyState[2] == true && keyState[1] == true) {
      this.pos.x += speeD;
      this.pos.y += speeD;
    } else if (keyState[0] == true && keyState[1] == true) {
      this.pos.x -= speeD;
      this.pos.y += speeD;
    } else if (keyState[0] == true) {
      //left
      this.pos.x -= this.speed;
    } else if (keyState[2] == true) {
      //right
      this.pos.x += this.speed;
    } else if (keyState[3] == true) {
      //up
      this.pos.y -= this.speed;
    } else if (keyState[1] == true) {
      //down
      this.pos.y += this.speed;
    }
  }

  void render() {
    image(base,this.pos.x, this.pos.y);
    println(radians(angle(pos, mousePV)));
    mousePV = new PVector(mouseX, mouseY);
    gun(radians(angle(pos, mousePV))+radians(180));
  }

  void gun(float ang) {
    println("in gun");
    println(this.pos.x);
    float dist = this.radius + gRad/2;
    println(this.pos.y);
    g.x = this.pos.x + (dist*cos(ang));
    g.y = this.pos.y + (dist*sin(ang));
    println(g.x, g.y);
    pushMatrix();
    translate(g.x,g.y);
    rotate(ang-radians(90));
    image(blaster,0, 0);
    popMatrix();
    println("out gun");
  }
  
  void bullet(float ang) {
    println(this.pos.x);
    float dist = this.radius + gRad + 10;
    println(this.pos.y);
    g.x = this.pos.x + (dist*cos(ang));
    g.y = this.pos.y + (dist*sin(ang));
    println(g.x, g.y);
    image(blaster,g.x, g.y);
  }

  float angle(PVector a, PVector b) {
    println("in angle");
    PVector c = new PVector();
    c.x = a.x - b.x;
    c.y = a.y - b.y;
    float d = atan2(c.y, c.x);
    float e = degrees(d);
    /*
    if (mouseY<c.y) {
      e=360-e;
      e=360-e;
      e=abs(e);
    } else {
      e=360-e;
    }
    */
    println("out angle");
    return e;
  }
  void imageLoad() {
    base = loadImage(basen);
    blaster = loadImage(blastern);
    base.resize(this.radius,this.radius);
    blaster.resize(gRad,gRad);
    imageMode(CENTER);
  }
}
