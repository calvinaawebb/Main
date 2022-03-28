import processing.sound.*;
Player temp = new Player(width/2, height/2, 50, 5, "gay", "base.png", "blaster.png");

public boolean[] keyState = new boolean[4];

public color back = 128;

public PImage map;

void setup() {
  fullScreen();
  frameRate(60);
  temp.imageLoad();
  map = loadImage("map.png");
}

void draw() {
  background(back);
  image(map,0, 0);
  temp.render();
  temp.move();
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
