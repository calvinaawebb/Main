//import process.sound.*;

public float xpos = 500;
public float ypos = 500;
public int size = 100;
public PImage car;


public vehicle v1 = new vehicle(ypos,xpos,size);

void setup() {
  fullScreen();
  frameRate(60);
  imageMode(CENTER);
  car = loadImage("car.png");
}

void draw() {
  v1.render();
  v1.control();
}

class vehicle {
  int size;
  public float ang;
  public PVector coords;
  public PVector mousePV;
  
  vehicle(float ypos, float xpos, int size) {
    coords = new PVector(xpos, ypos);
    mousePV = new PVector(mouseX, mouseY);
    float ang = radians(angle(coords, mousePV));
    this.size = size;
  }
  
  float angle(PVector a, PVector b) {
    println("in angle");
    PVector c = new PVector();
    c.x = a.x - b.x;
    c.y = a.y - b.y;
    float d = atan2(c.y, c.x);
    float e = degrees(d);
    println("out angle");
    return e;
  }
  
  public void control() {
    if (keyPressed && key == 'w') {
      
    }
  }
  
  public void render() {
    pushMatrix();
    rotate(ang-radians(90));
    image(car, coords.x, coords.y, this.size, this.size);
    popMatrix();
  }
}
