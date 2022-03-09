public class Pop {
  // pop out class
  int xpos;
  int ypos;
  int rwid;
  int rhei;
  
  Pop(int xpos, int ypos, int rwid, int rhei){
    this.xpos = xpos;
    this.ypos = ypos;
    this.rwid = rwid;
    this.rhei = rhei;
  }
  
  void render() {
    fill(secondary); 
    rect(xpos, ypos, rwid, rhei);
    textAlign(CENTER);
    fill(255);
    text("Options", xpos+150, ypos+50);
  }

  void drag() {
    if (mousePressed && ((mouseX > xpos && mouseX < xpos + rwid-10) && (mouseY > ypos && mouseY < ypos + rhei-10))) {
      if (mousePressed) {
        xpos = mouseX; //+ ((rwid + xpos)-mouseX);
        ypos = mouseY; //+ ((rhei + ypos)-mouseY);
      }
    }
  }
}
