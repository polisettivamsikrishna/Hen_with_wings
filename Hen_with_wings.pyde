def setup():
    size(800, 600, P3D)
    background(255)
    
def draw():
    with pushMatrix(): #yellow sphere
        translate(400,220)
        noStroke()
        fill(255, 204, 0)
        directionalLight(126, 126, 126, 10, 0, -1)
        lightSpecular(102, 102, 102)
        ambientLight(102, 102, 102)
        pointLight(255,255,255,400,200,1000)
        sphere(55)
        strokeWeight(2)
    with pushMatrix(): #big ellipse
        translate(400,355,100)
        noStroke()
        fill(255, 204, 0)
        spotLight(51, 102, 126, 80, 20, 40, -1, 0, 0, PI/2, 2)
        sphere(80)
        strokeWeight(2)
    with pushMatrix(): #left eye
        translate(385,220,110)
        stroke(0)
        fill(255)
        ellipse(0,0,15,20)
    with pushMatrix(): #right eye
        translate(415,220,110)
        stroke(0)
        fill(255)
        ellipse(0,0,15,20)
    with pushMatrix(): #inner left eye
        translate(385,223,110)
        noStroke()
        fill(100,0,0)
        ellipse(0,0,10,10)
        fill(255)
    with pushMatrix(): #inner right eye
        translate(415,223,110)
        noStroke()
        fill(100,0,0)
        ellipse(0,0,10,10)
        fill(255)
    with pushMatrix(): #nose
        translate(400,240,110)
        stroke(0)
        fill(255,100,0)
        ellipse(0,0,20,10)
        spotLight(51, 102, 126, 80, 20, 40, -1, 0, 0, PI/2, 2)
    with pushMatrix(): #left leg 
        translate(360,500);
        fill(102);
        noStroke();
        strokeWeight(2);
        beginShape();        
        rotateX(PI/3)
        vertex(0, 0);
        vertex(7, -10);
        vertex(24, -7);
        vertex(11, 4);
        vertex(15, 20);
        vertex(0, 13);
        vertex(-15, 20);
        vertex(-11, 3);
        vertex(-22, -8);
        vertex(-7, -10);
        endShape(CLOSE);
    with pushMatrix(): #right leg 
        translate(440,500);
        fill(102);
        noStroke();
        strokeWeight(2);
        beginShape();        
        rotateX(PI/3)
        vertex(0, 0);
        vertex(7, -10);
        vertex(24, -7);
        vertex(11, 4);
        vertex(15, 20);
        vertex(0, 13);
        vertex(-15, 20);
        vertex(-11, 3);
        vertex(-22, -8);
        vertex(-7, -10);
        endShape(CLOSE);
        
    with pushMatrix(): #left wing
        translate(330,355);
        fill(255, 204, 70);
        stroke(0);
        strokeWeight(2);
        beginShape();
        vertex(0, -75);
        vertex(57, -60);
        vertex(0,0);
        vertex(0,0);
        vertex(0, 0);
        vertex(0, 62);
        vertex(-65, 70);
        vertex(-63, 57);
        vertex(-70, -55);
        vertex(-57, -60);
        endShape(CLOSE);
        strokeWeight(1)
        pointLight(255,255,255,400,200,1000)
    with pushMatrix(): #right wing
        translate(450,355);
        fill(255, 204, 70);
        stroke(0);
        strokeWeight(2);
        beginShape();
        vertex(40, -71);
        vertex(84, -60);
        vertex(88, -15);
        vertex(113, 47);
        vertex(69, 40);
        vertex(0, 25);
        vertex(0,0);
        vertex(0, 27);
        vertex(0,0);
        vertex(-14, -20);
        endShape(CLOSE);
        strokeWeight(1)
        pointLight(255,255,255,400,200,1000)
    with pushMatrix(): #left leg strip
        translate(355,463);
        fill(255, 104, 40)
        beginShape(); 
        rect(0,0,10,35)
        endShape(CLOSE)
    with pushMatrix(): #left leg strip
        translate(435,463);
        fill(255, 104, 40)
        beginShape(); 
        rect(0,0,10,35)
        endShape(CLOSE)
