Button[] numButtons = new Button[10];
Button[] opButtons = new Button[12];
String dVal = "0";
String op = "";
boolean left = true;
float r = 0.0;
float l = 0.0;
float result = 0.0;

void setup() {
  size(640, 840);
  numButtons[0] = new Button(160, 720, 100, 100, "0", color(59, 53, 122), color(59, 53, 122));
  numButtons[1] = new Button(40, 360, 100, 100, "1", color(59, 53, 122), color(59, 53, 122));
  numButtons[2] = new Button(160, 360, 100, 100, "2", color(59, 53, 122), color(59, 53, 122));
  numButtons[3] = new Button(280, 360, 100, 100, "3", color(59, 53, 122), color(59, 53, 122));
  numButtons[4] = new Button(40, 480, 100, 100, "4", color(59, 53, 122), color(59, 53, 122));
  numButtons[5] = new Button(160, 480, 100, 100, "5", color(59, 53, 122), color(59, 53, 122));
  numButtons[6] = new Button(280, 480, 100, 100, "6", color(59, 53, 122), color(59, 53, 122));
  numButtons[7] = new Button(40, 600, 100, 100, "7", color(59, 53, 122), color(59, 53, 122));
  numButtons[8] = new Button(160, 600, 100, 100, "8", color(59, 53, 122), color(59, 53, 122));
  numButtons[9] = new Button(280, 600, 100, 100, "9", color(59, 53, 122), color(59, 53, 122));
  opButtons[0] = new Button(40, 720, 100, 100, "C", color(59, 53, 122), color(59, 53, 122));
  opButtons[1] = new Button(40, 240, 100, 100, "+", color(59, 53, 122), color(59, 53, 122));
  opButtons[2] = new Button(40, 720, 100, 100, "-", color(59, 53, 122), color(59, 53, 122));
  opButtons[3] = new Button(40, 720, 100, 100, "*", color(59, 53, 122), color(59, 53, 122));
  opButtons[4] = new Button(40, 720, 100, 100, "/", color(59, 53, 122), color(59, 53, 122));
  opButtons[5] = new Button(400, 600, 220, 220, "=", color(255, 0, 128), color(255, 0, 128));
  opButtons[6] = new Button(280, 720, 100, 100, ".", color(59, 53, 122), color(59, 53, 122));
  opButtons[7] = new Button(400, 480, 100, 100, "±", color(59, 53, 122), color(59, 53, 122));
  opButtons[8] = new Button(40, 720, 100, 100, "C", color(59, 53, 122), color(59, 53, 122));
  opButtons[9] = new Button(40, 720, 100, 100, "C", color(59, 53, 122), color(59, 53, 122));
  opButtons[10] = new Button(40, 720, 100, 100, "C", color(59, 53, 122), color(59, 53, 122));
  opButtons[11] = new Button(40, 720, 100, 100, "C", color(59, 53, 122), color(59, 53, 122));
}
//255, 0, 128

void draw() {
  background(46, 41, 102);
  updateDisplay();
  for (int i=0; i<numButtons.length; i++) {
    numButtons[i].display();
    numButtons[i].hover(mouseX, mouseY);
  }
  for (int i=0; i<opButtons.length; i++) {
    opButtons[i].display();
    opButtons[i].hover(mouseX, mouseY);
  }
}

void mousePressed() {
  for (int i=0; i<numButtons.length; i++) {
    if (numButtons[i].on && dVal.length()<26) {
      handleEvent(numButtons[i].val, true);
    }
  }
  for (int i=0; i<opButtons.length; i++) {
    if (opButtons[i].on) {
      handleEvent(opButtons[i].val, false);
    }
  }
  println("L:" + l + " Op:" + op + " R:" + r + " Result" + result + " Left:" + left);
}

void clearCalc() {
  dVal = "0";
  op = "";
  left = true;
  r = 0.0;
  l = 0.0;
  result = 0.0;
}

void updateDisplay() {
  fill(222);
  rect(40, 40, 560, 190);
  fill(0);
  textAlign(RIGHT);
  if (dVal.length() < 12) {
    textSize(48);
  } else if (dVal.length() < 13) {
    textSize(44);
  } else if (dVal.length() < 14) {
    textSize(40);
  } else if (dVal.length() < 15) {
    textSize(38);
  } else if (dVal.length() < 16) {
    textSize(36);
  } else {
    textSize(20);
  }
  text(dVal, 580, 120);
}

void performCalculation() {
  if (op.equals("+")) {
    result = l + r;
  } else if (op.equals("-")) {
    result = l - r;
  } else if (op.equals("*")) {
    result = l * r;
  } else if (op.equals("/")) {
    result = l / r;
  }
  dVal = str(result);
  l = result;
}

void keyPressed() {
  println("key?:" + key);
  println("keyCode:" + keyCode);
  if (keyPressed) {
    if (key == 1) {
      handleEvent("1", true);
    } else if (key == 2) {
      handleEvent("2", true);
    } else if (key == 3) {
      handleEvent("3", true);
    } else if (key == 4) {
      handleEvent("4", true);
    } else if (key == 5) {
      handleEvent("5", true);
    } else if (key == 6) {
      handleEvent("6", true);
    } else if (key == 7) {
      handleEvent("7", true);
    } else if (key == 8) {
      handleEvent("8", true);
    } else if (key == 9) {
      handleEvent("9", true);
    } else if (key == 0) {
      handleEvent("0", true);
    }
  }
}

void handleEvent(String val, boolean num) {
  if (num) {
    //handle all number clicks or keypress
    if (dVal.equals("0")) {
      dVal = val;
      if (left) {
        l = float(dVal);
      } else if (!left) {
        r = float(dVal);
      }
    } else if (dVal.length() < 24) {
      dVal = dVal + val;
      if (left) {
        l = float(dVal);
      } else if (!left) {
        r = float(dVal);
      }
    }
  } else if (val.equals("C")) {
    clearCalc();
  } else if (val.equals("+")) {
    left = false;
    op = "+";
    dVal = "0";
  } else if (val.equals("=")) {
    performCalculation();
  } else if (val.equals("±")) {
    if (left) {
      l = l * -1;
      dVal = str(l);
    } else if (!left) {
      r = r * -1;
      dVal = str(r);
    }
  } else if (val.equals(".")) {
  }
}
