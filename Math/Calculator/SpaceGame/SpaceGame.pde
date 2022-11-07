import processing.sound.*;
Ship s1;
ArrayList<Star> stars = new ArrayList<Star>();
ArrayList<PowerUp> powerUps = new ArrayList<PowerUp>();
SoundFile laser;
ArrayList<Rock> rocks = new ArrayList<Rock>();
ArrayList<Laser> lasers = new ArrayList<Laser>();
Timer rockTimer;
Timer puTimer;
int score, level;
boolean play;

void setup() {
  size(1000, 1000);
  s1 = new Ship();
  laser = new SoundFile(this, "laser.wav");
  //startScreen = loadImage("start.png");
  //gameOver = loadImage("over.png");
  score = 0;
  level = 1;
  /*
  for (int i = 0; i<stars.length; i++) {
    stars[i] = new Star();
  }
  */
  rockTimer = new Timer(1000);
  rockTimer.start();
}

void draw() {
  background(0);
  noCursor();

  //check for the status of the play boolean and load game over if false
  if (!play) {
    startScreen();
  } else {
    infoPanel();
    //Render Stars
    stars.add(new Star());
    for (int i = 0; i< stars.size(); i++) {
      Star star = stars.get(i);
      star.display();
      star.move();
      if (star.reachedBottom()) {
        stars.remove(star);
      }
    }

    s1.display(mouseX, mouseY);
    if (rockTimer.isFinished()) {
      rocks.add(new Rock(int(random(width)), -100));
      rockTimer.start();
    }
    /*
    if (puTimer.isFinished()) {
      rocks.add(new Rock(int(random(width)), -100));
      puTimer.start();
    }
    */
    for (int i = 0; i < powerUps.size(); i++) {
      PowerUp pu = powerUps.get(i);
      pu.display();
      pu.move();
      /*
      if (pu.intersect(s1)) {
        if (pu.type == 'h') {
          s1.health+=100;
        } else if (pu.type == 'h') {
          s1.health+=100;
        }
      }
      */
      if (pu.reachedBottom()) {
        powerUps.remove(pu);
      }
    }

    for (int i = 0; i < rocks.size(); i++) {
      Rock rock = rocks.get(i);
      rock.display();
      rock.move();
      if (rock.intersect(s1)) {
        s1.health-=rock.diam;
        rocks.remove(rock);
        score+=rock.health;
      }
      if (rock.reachedBottom()) {
        rocks.remove(rock);
      }
    }
    for (int i = 0; i < lasers.size(); i++) {
      Laser laser = lasers.get(i);
      for (int j = 0; j<rocks.size(); j++) {
        Rock rock = rocks.get(j);
        if (laser.intersect(rock)) {
          lasers.remove(laser);
          score = score+rock.health;
          rock.diam = rock.diam - 50;
          if (rock.health<10) {
            rocks.remove(rock);
            score = score + rock.health;
          }
        }
      }
      laser.display();
      laser.move();
      if (laser.reachedTop()) {
        lasers.remove(laser);
      }
    }
  }
}
void infoPanel() {
  fill(127, 127);
  rectMode(CENTER);
  rect(0, 0, width, 60);
  fill(255);
  textAlign(CENTER);
  textSize(20);
  text("Score:" + score + "Level" + level + "Health" + s1.health, width/2, 50);
}

void startScreen() {
  background(0);
  textAlign(CENTER);
  textSize(45);
  fill(255);
  text("Welcome to ARTeMOS", width/2, height/2);
  textSize(35);
  text("By Calvin Webb", width/2, height/2+30);
  textSize(18);
  text("Press any key to start...", width/2, height/2+500);
  if (mousePressed) {
    play = true;
  }
}

void gameOver() {
  background(0);
  //image(gameOver,0,0);
  textAlign(CENTER);
}

void ticker() {
}

void mousePressed() {
  if (s1.fire()) {
    /*
    if (s1.turret = 1)
      laser.stop();
    */
    lasers.add(new Laser(s1.x, s1.y));
    laser.play();
    s1.laserCount-=1;
  }
}

void keyPressed() {
  if (keyPressed) {
    if (key == ' ') {
      laser.stop();
      lasers.add(new Laser(s1.x, s1.y));
      laser.play();
      s1.laserCount--;
    }
  }
}
