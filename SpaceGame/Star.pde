class Star{
  int x,y,diam,speed;
  
  Star() {
    x = int(random(width));
    y = int(random(height));
    diam = int(random(1,5));
    speed = int(random(1,7));
  }
  
  void display() {
    fill(random(95, 255));
    ellipse(x,y,diam,diam);
  }
  
  void move() {
    if(y>height+10) {
      y = 0;  
    }
    y = y + speed;
  }
  
  boolean reachedBottom() {
    return true;
  }
}
