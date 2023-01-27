#define LEDPin 13

char msg;

void setup() {
  Serial.begin(9600);

  pinMode(LEDPin, OUTPUT);

  digitalWrite(LEDPin, LOW);
  
}

void loop() {

  if(Serial.available() > 0) {

    msg = Serial.read(); 
    



    if(msg == 'n') {

      digitalWrite(LEDPin, HIGH);
    }
    
  }
}

  




    
