class PowerUp {
  int x,y,diam,speed,rand,health;
  PImage powerUp;
  
  PowerUp(int x, int y) {
    this.x = x;
    this.y = y;
    diam = int(random(30,90));
    speed = int(random(2,7));
    rand = int(random(3));
    if(rand == 0) {
      powerUp = loadImage("healthIncrease.png");
    } else if(rand == 1) {
      powerUp = loadImage("laserIncrease.png");
    } else {
      powerUp = loadImage("turretCount.png");
    }
  }
  
  void display() {
    fill(128);
    imageMode(CENTER);
    //if(type == "h")
    image(powerUp,x,y);
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
