public PImage worldmap;

public color primary = color(255, 0, 0);
public color base;

public int xpos;
public int ypos;

void setup() {
  worldmap = loadImage("worldmap.png");
  fullScreen();
  frameRate(60);
  //loadPixels();
}

void draw() {
  image(worldmap, 0, 0);
  if (mousePressed && worldmap.pixels[mouseX + (mouseY*worldmap.width)] != primary) {
    thread("fillThread");
    xpos = mouseX;
    ypos = mouseY;
  }
}

void fillThread() {
  ArrayList<PVector> check = new ArrayList<PVector>();
  check.add(new PVector(xpos, ypos));
  base = worldmap.pixels[xpos + (ypos*worldmap.width)];   
  worldmap.loadPixels();
  while (check.size() > 0) {
    worldmap.pixels[(int)check.get(0).x + ((int)check.get(0).y*worldmap.width)] = primary;
    worldmap.updatePixels();
    int ypos = (int)check.get(0).y;
    int xpos = (int)check.get(0).x;
    if (_get(xpos-1, ypos-1) == base) {
      check.add(new PVector(xpos-1, ypos-1));
    }
    if (_get(xpos+1, ypos+1) == base) {
      check.add(new PVector(xpos+1, ypos+1));
    }
    if (_get(xpos+1, ypos-1) == base) {
      check.add(new PVector(xpos+1, ypos-1));
    }
    if (_get(xpos-1, ypos+1) == base) {
      check.add(new PVector(xpos-1, ypos+1));
    }
    if (_get(xpos, ypos-1) == base) {
      check.add(new PVector(xpos, ypos-1));
    }
    if (_get(xpos+1, ypos) == base) {
      check.add(new PVector(xpos+1, ypos));
    }
    if (_get(xpos, ypos+1) == base) {
      check.add(new PVector(xpos, ypos+1));
    }
    if (_get(xpos-1, ypos) == base) {
      check.add(new PVector(xpos-1, ypos));
    }
    check.remove(0);
  }
}

color _get(int x, int y) {
  color c;
  if (x>=0&&y>=0&&x<worldmap.width&&y<worldmap.height) {
    c = worldmap.pixels[x+y*width];
  } else {
    return -1;
  }
  return c;
}
