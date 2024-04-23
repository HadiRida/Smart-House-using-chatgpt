const int microwavePin = 8;  // Replace with the actual pin connected to the microwave
const int livingRoomPin = 9; // Replace with the actual pin connected to the living room lights
const int kitchenPin = 10;    // Replace with the actual pin connected to the kitchen lights
const int fanPin = 11;   
const int TvPin = 12;     // Replace with the actual pin connected to the fan





void setup() {
  Serial.begin(9600);
  pinMode(microwavePin, OUTPUT);
  pinMode(livingRoomPin, OUTPUT);
  pinMode(kitchenPin, OUTPUT);
  pinMode(fanPin, OUTPUT);
 
  pinMode(TvPin, OUTPUT);

 

}



void loop()
{
  if (Serial.available() > 0) {
        char key = Serial.read();
        if(key == '1')
        {
          digitalWrite(microwavePin ,HIGH);
          delay(2000);
          digitalWrite(microwavePin,LOW);
        } 

        if(key == '3')
        {
          digitalWrite(kitchenPin ,HIGH);
        } 
        
        else if (key == '2')
        {
          digitalWrite(livingRoomPin ,HIGH);
        } 

        else if(key == '4')
        {
          {  
           digitalWrite(fanPin ,HIGH);
         }  
        
        }
        else if (key == '5')
        {
          digitalWrite(TvPin ,HIGH);
        } 
         
         else if(key == '6')
        {
          digitalWrite(microwavePin ,LOW);
        } 
        else if (key == '7')
        {
          digitalWrite(livingRoomPin ,LOW);
        } 

        if(key == '8')
        {
          digitalWrite(kitchenPin ,LOW);
        } 

        else if(key == '9')
        {
          digitalWrite(fanPin ,LOW);
        } 

        else if (key == '10')
        {
          digitalWrite(TvPin ,LOW);
        } 

  }
}