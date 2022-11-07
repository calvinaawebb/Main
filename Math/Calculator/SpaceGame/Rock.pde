class Rock {
  int x,y,diam,speed,rand,health;
  PImage rock;
  
  Rock(int x, int y) {
    this.x = x;
    this.y = y;
    diam = int(random(300,390));
    speed = int(random(2,7));
    rand = int(random(3));
    if(rand == 0) {
      rock = loadImage("rock1.png");
    } else if(rand == 1) {
      rock = loadImage("rock2.png");
    } else {
      rock = loadImage("rock3.png");
    }
  }
  
  void display() {
    fill(128);
    imageMode(CENTER);
    image(rock,x,y);
  }
  
  void move() {
    y = y + speed;
  }
  
  boolean reachedBottom() {
    if(y>height+100) {
      return true; 
    } else {
      return false;
    }
  }
  
  boolean intersect(Ship s1) {
    float distance = dist(x,y,s1.x,s1.y);
    if(distance<40) {
      return true; 
    } else {
      return false;
    }
  }
}
