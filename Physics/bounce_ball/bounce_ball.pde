import java.util.Collection;
import processing.sound.*;
Pop start;
Ball[] balls = new Ball[max_balls];

public static boolean play;

public static color primary = (45);
public static color secondary = (95);
public static color background = (185);

public static float gravity = 1;

public static int max_balls = 500;
public static int ball_counter = 0;

public boolean vel = true;


//public static font = loadFont();


void setup() {
  fullScreen(); 
  noCursor();
  frameRate(60);
  start = new Pop(width-(width/4), height/10, (width/4)-(width/6), height/5);
}
  
void draw() {
  background(background);
  
  if(!play) {
    opening();
  } else {
    // add fade out
    stage();
    tramp();
    start.render();
    start.drag();
    for (int i=0;i<ball_counter;i++) {
      balls[i].render();
      balls[i].move();
      if (vel) {
        balls[i].velo();
      }
    }
    cursor();
  }
}

void keyReleased() {
  if ((key == 'e' || key == 'E') && ball_counter != max_balls) {
    balls[ball_counter] = new Ball(mouseX, mouseY, 50, 50);
    ball_counter += 1;
  }
}

void opening() {
  // opening screen
  background(0);
  textAlign(CENTER);
  textSize(45);
  fill(255);
  text("BBIS", width/2, height/2);
  textSize(24);
  text("Bouncing Ball Interactive Simulation", width/2, height/2+60);
  if (mousePressed) {
    play = true;
  }
}

void stage() {
  fill(primary);
  rect(0, height-100, width, 1000);
}

void tramp() {
  fill(secondary);
  rect(width/2, height-115, 100, 100);
}
