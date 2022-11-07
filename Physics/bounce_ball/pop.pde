public class Pop {
  // pop out class
  float xpos;
  float ypos;
  float rwid;
  float rhei;
  
  Pop(float xpos, float ypos, float rwid, float rhei){
    this.xpos = xpos;
    this.ypos = ypos;
    this.rwid = rwid;
    this.rhei = rhei;
  }
  
  void render() {
    fill(secondary); 
    rect(xpos, ypos, rwid, rhei);
    textAlign(LEFT);
    fill(255);
    text("Collisions and Momentum:\n This model simulates 2D\n collisions between circles.\n To spawn balls, press 'e' \nand a ball will spawn at \nyour cursor location.\n The white line you see \non each ball is its \nvelocity visualized.\n Each ball is equal in mass\n so you can see the collisions \nand how they effect velocity \nbetter.", xpos+(width/60), ypos+50);
  }

  void setCoords(float x, float y) {
        this.xpos = x;
        this.ypos = y;
  }
}
