class Laser{
  int x,y,w,h,speed;
  
  Laser(int x, int y) {
    this.x = x;
    this.y = y;
    w = 3;
    h = 9;
    speed = 8;
  }
  
  void display() {
    fill(255,0,0);
    noStroke();
    rectMode(CENTER);
    rect(x,y,w,h);
  }
  
  void move() {
    y = y - speed;
  }
  
  boolean intersect(Rock r) {
    float distance = dist(x,y,r.x,r.y);
    if(distance<40) {
      return true; 
    } else {
      return false;
    }
  }
  
  boolean reachedTop() {
    if(y<0-10) {
      return true;
    } else {
      return false;
    }
  }
}
