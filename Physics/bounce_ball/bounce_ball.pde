import java.util.Collection;
//import processing.sound.*;
Pop start;
Ball[] balls = new Ball[max_balls];

public static boolean play;
public static boolean dragged = false;

public static color primary = (45);
public static color secondary = (95);
public static color background = (185);

public static float gravity = 1;

public static int max_balls = 30;
public static int ball_counter = 0;
public static int ball_rad = 50;

public boolean vel = true;

public static float px;
public static float py;
public static float pw;
public static float ph;



//public static font = loadFont();


void setup() {
  size(displayWidth, displayHeight);
  noCursor();
  frameRate(60);
  px = width-(width/5);
  py = height/26;
  pw = (width/5)-(width/60);
  ph = height/2;
  start = new Pop(px, py, pw, ph);
}

void draw() {
  background(background);

  if (!play) {
    opening();
  } else {
    // add fade out
    stage();
    //tramp();
    start.render();
    start.setCoords(px, py);
    for (int i=0; i<ball_counter; i++) {
      balls[i].render();
      if (vel) {
        balls[i].velo();
      }
    }
    for (int c=0; c<1; c++) {
      for (int i=0; i<ball_counter; i++) {
        for (int j=0; j<ball_counter; j++) {
          if (i != j) {
            float dist = balls[i].coords.dist(balls[j].coords);
            if (dist < ball_rad) {
              PVector colS = PVector.sub(balls[i].coords, balls[j].coords);
              PVector n = PVector.div(colS, dist);
              float delta = ball_rad+0.01 - dist;
              balls[i].coords.add(PVector.mult(PVector.mult(n, delta), 0.5));
              balls[j].coords.sub(PVector.mult(PVector.mult(n, delta), 0.5));
              PVector bspeed =  new PVector(balls[i].speed.x, balls[i].speed.y);
              balls[i].speed = new PVector(balls[j].speed.x, balls[j].speed.y);
              balls[j].speed = bspeed;
            }
          }
        }
        balls[i].move(1);
      }
    }
    cursor();
  }
}

void keyReleased() {
  if ((key == 'e' || key == 'E') && ball_counter != max_balls) {
    balls[ball_counter] = new Ball(mouseX, mouseY, ball_rad, ball_rad);
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

/*
void mouseDragged() {
 System.out.println(mouseX);
 System.out.println(mouseY);
 System.out.println((px+(pw-10)));
 System.out.println((py+(ph-10)));
 if (((mouseX > px && mouseX < px + 100) && (mouseY > py && mouseY < py + 200))) {
 System.out.println("Alive");
 dragged = true;
 }
 if (dragged == true) {
 final float difx = mouseX - px;
 final float dify = mouseY - py;
 System.out.println("tf");
 px = mouseX + difx; //+ ((rwid + xpos)-mouseX);
 py = mouseY + dify; //+ ((rhei + ypos)-mouseY);
 System.out.println(px);
 System.out.println(py);
 }
 dragged = false;
 }
 */
void stage() {
  fill(primary);
  rect(0, height-100, width, 1000);
}

void tramp() {
  fill(secondary);
  rect(width/2, height-115, 100, 100);
}
