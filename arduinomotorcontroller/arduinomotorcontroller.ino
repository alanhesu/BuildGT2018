const int m11 = 9;
const int m12 = 10;
const int m21 = 11;
const int m22 = 12;
const int sw11 = 2;
const int sw12 = 3;
char data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(m11, OUTPUT);
  pinMode(m12, OUTPUT);
  pinMode(m21, OUTPUT);
  pinMode(m22, OUTPUT);
  pinMode(sw11, INPUT);
  pinMode(sw12, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '\0';
    delay(10);   
  }
  
  if(data == '1') {
    //raise();
    analogWrite(m11,100);
    //delay(50);   
    slap();
    delay(50);
    drawbackSlap();
    delay(50);
    //lower();
    //delay(50);
    analogWrite(m11,0);
    data = '0';
  }
}

void raise() {
  digitalWrite(m11, HIGH);
  digitalWrite(m12, LOW);    
  delay(600);
  digitalWrite(m11, LOW);    
}

void slap() {
  digitalWrite(m21, HIGH);
  digitalWrite(m22, LOW);    
  delay(500);
  digitalWrite(m21, LOW);    
}

void drawbackSlap() {
  digitalWrite(m12, HIGH);
  digitalWrite(m11, LOW);    
  while(digitalRead(sw12) == 1) {
    continue;     
  }
  digitalWrite(m12, LOW);    
}

void lower() {
  digitalWrite(m22, HIGH);
  digitalWrite(m21, LOW);    
  while(digitalRead(sw12) == 0) {
    continue;     
  }
  digitalWrite(m22, LOW);    
}
