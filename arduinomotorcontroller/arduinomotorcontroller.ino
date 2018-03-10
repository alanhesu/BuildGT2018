const int m11 = 9;
const int m12 = 10;
char data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(m11, OUTPUT);
  pinMode(m12, OUTPUT);
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
    digitalWrite(m11, HIGH);
    digitalWrite(m12, LOW);
    delay(1000);
    digitalWrite(m11, LOW);
    delay(1000);
    data = '0';
  }
}
