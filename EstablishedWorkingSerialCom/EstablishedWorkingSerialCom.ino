#define LEDPin1 12
#define LEDPin2 11
#define LEDPin3 10
#define LEDPin4 8

#define MotValBLPin 3
#define MotValBRPin 5
#define MotValTLPin 6
#define MotValTRPin 9
#define conPin 4 

int msg;
int motAddr;
int motVal;

int get_motor_address(int msg) {
  return msg >> 6;
  
}

int get_motor_value(int msg) {
  
  return msg & 0b00111111;
}


void setup() {
  Serial.begin(9600);

  pinMode(LEDPin1, OUTPUT);
  pinMode(LEDPin2, OUTPUT);
  pinMode(LEDPin3, OUTPUT);
  pinMode(LEDPin4, OUTPUT);

  pinMode(MotValBLPin, OUTPUT);
  pinMode(MotValBRPin, OUTPUT);
  pinMode(MotValTLPin, OUTPUT);
  pinMode(MotValTRPin, OUTPUT);



  digitalWrite(LEDPin1, LOW);
  digitalWrite(LEDPin2, LOW);
  digitalWrite(LEDPin3, LOW);
  digitalWrite(LEDPin4, LOW);


  analogWrite(MotValBLPin, 0);
  analogWrite(MotValBRPin, 0);
  analogWrite(MotValTLPin, 0);
  analogWrite(MotValTRPin, 0);
  
}

void loop() {

  if(Serial.available() > 0) {

    msg = Serial.read(); 

    motAddr = get_motor_address(msg);
    motVal = get_motor_value(msg);

    if(motAddr == 0) { // 00
      digitalWrite(LEDPin1, HIGH);
      analogWrite(MotValBLPin, (float(motVal)/63)*255);
    } else {
      digitalWrite(LEDPin1, LOW);
    }
    
    if(motAddr == 1) { // 01
      digitalWrite(LEDPin2, HIGH);
      analogWrite(MotValBRPin, (float(motVal)/63)*255);
    } else {
      digitalWrite(LEDPin2, LOW);
    }

    if(motAddr == 2) { // 10
      digitalWrite(LEDPin3, HIGH);
    } else {
      digitalWrite(LEDPin3, LOW);
    }

    if(motAddr == 3) { // 11
      digitalWrite(LEDPin4, HIGH);
    } else {
      digitalWrite(LEDPin4, LOW);
    }

    
    
    
  }
}
