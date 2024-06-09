String incominigByte;
const int REDPIN = 11;
const int GREENPIN = 10;
const int BLUEPIN = 9;

void setup() {
  Serial.begin(9600);
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT); 
}
 
 
void loop() {
  if (Serial.available() > 0 ){
    incominigByte = Serial.readStringUntil('\n');
    
    //color off        
    if (incominigByte == "e"){
      digitalWrite(REDPIN, LOW);
      digitalWrite(GREENPIN, LOW);
      digitalWrite(BLUEPIN, LOW);          
    } 
    //color green
    if (incominigByte == "g"){
      digitalWrite(REDPIN, 0);
      digitalWrite(GREENPIN, 255);
      digitalWrite(BLUEPIN, 0);
    }
    //color red
    if (incominigByte == "r"){
      digitalWrite(REDPIN, 255);
      digitalWrite(GREENPIN, 0);
      digitalWrite(BLUEPIN, 0);
    }
    //color blue
    if (incominigByte == "b"){
      digitalWrite(REDPIN, 0);
      digitalWrite(GREENPIN, 0);
      digitalWrite(BLUEPIN, 255);       
    } 
    //color white    
    if (incominigByte == "w"){
      digitalWrite(REDPIN, 255);
      digitalWrite(GREENPIN, 255);
      digitalWrite(BLUEPIN, 255);       
    }     
    //color violet    
    if (incominigByte == "v"){
      digitalWrite(REDPIN, 102);
      digitalWrite(GREENPIN, 0);
      digitalWrite(BLUEPIN, 153);       
    } 
    //color cyan    
    if (incominigByte == "c"){
      digitalWrite(REDPIN, 0);
      digitalWrite(GREENPIN, 255);
      digitalWrite(BLUEPIN, 255);       
    }   
    //color yellow    
    if (incominigByte == "y"){
      digitalWrite(REDPIN, 255);
      digitalWrite(GREENPIN, 255);
      digitalWrite(BLUEPIN, 0);       
    }               
  }
}
