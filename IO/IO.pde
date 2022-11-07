import processing.sound.*;
ArrayList<Player> temp = new ArrayList<Player>();

public PImage base;
public PImage blaster;
public PImage map;
public PImage bullet;

public boolean[] keyState = new boolean[4];

public color back = 128;

void setup() {
  fullScreen();
  frameRate(60);
  imageMode(CENTER);
  map = loadImage("map.png");
  base = loadImage("base.png");
  blaster = loadImage("blaster.png");
  temp.add(new Player(width/2, height/2, 150, 5, "gay", new PVector(512*10, 512*10)));
}

void draw() {
  background(back);
  for (int i=0; i<temp.size(); i++) {
    temp.get(i).render();
    temp.get(i).move();
  }
}

void keyPressed() {
  switch(key) {
  case 'a':
    keyState[0] = true;
    break;
  case 's':
    keyState[1] = true;
    break;
  case 'd':
    keyState[2] = true;
    break;
  case 'w':
    keyState[3] = true;
    break;
  }
}

void keyReleased() {
  switch(key) {
  case 'a':
    keyState[0] = false;
    break;
  case 's':
    keyState[1] = false;
    break;
  case 'd':
    keyState[2] = false;
    break;
  case 'w':
    keyState[3] = false;
    break;
  }
}
