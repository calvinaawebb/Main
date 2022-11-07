class Ship{
  int x,y,w,health,laserCount;
  PImage ship;
  boolean active;
  
  Ship() {
    x = 0;
    y = 0;
    w = 8;
    health = 100;
    laserCount = 500;
    active = true;
    ship = loadImage("Ship.png");
  }
  
  void display(int x, int y) {
    this.x = x;
    this.y = y;
    imageMode(CENTER);
    image(ship,x,y);
  }
  
  void move() {}
  
  boolean fire() {
    if(laserCount>0) {
      return true;
    } else {
      return false;
    }
  }
  
  boolean intersect(Rock r) {
    float distance = dist(x,y,r.x,r.y);
    if(distance<10) {
      return true;
    } else {
      return false;
    }
  }
}
