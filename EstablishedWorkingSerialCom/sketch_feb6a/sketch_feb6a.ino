
uint8_t data = 170; //value to transmit, binary 10101010
uint8_t mask = 11000000; //our bitmask




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


byte getMS(byte data){
byte motorSelect = data >> 6; 

return motorSelect;
}

byte getVS(byte data){
byte voltageSelect = data;
voltageSelect &= ~(1UL << 6);
voltageSelect &= ~(1UL << 7);

return voltageSelect;
}

void doStuff(byte data)
{
  switch(getMS(data))
  {
    case 0b00: 
      break;
    case 0b01: 
      break;
    case 0b10: 
      break;
    case 0b11: 
      break;
  }
}



  




    
