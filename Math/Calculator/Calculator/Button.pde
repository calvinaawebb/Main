class Button {
  //Member Variables
  float x,y,w,h;
  boolean on;
  String val;
  color c1,c2;
  
  //Constructor
  Button(float tempX, float tempY, float tempW, float tempH, String tempVal, color tempC1, color tempC2) {
    x = tempX;
    y = tempY;
    w = tempW;
    h = tempH;
    val = tempVal;
    on = false;
    c1 = tempC1;
    c2 = tempC2;
  }
  
  
  //Method for Display
  void display() {
    if(on) {
      fill(c1);
    } else {
      fill(c2);
    }
    rect(x,y,w,h,5);
    fill(255);
    textSize(16);
    textAlign(LEFT);
    text(val,x+15,y+25);
  }
  //Method to detect mouseover
  void hover(int mx, int my) {
    on = (mx>x && mx<x+w && my>y && my<y+h);
  }
}
