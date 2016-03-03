const int coinPin = 2;
const int pumpPin = 7;

void setup() {
  //Start Serial Communication
  Serial.begin(9600);                 
  //If coinInt goes HIGH (a Pulse), call the coinInserted function
  pinMode(pumpPin, OUTPUT);      // sets the digital pin as output
  pinMode(coinPin, INPUT);       // sets the digital pin as input
}

void loop() {
  if (digitalRead(coinPin) == HIGH) {
      Particle.publish("drink_pour", "data");// publish event to cloud
      digitalWrite(pumpPin, HIGH);   // sets the LED on
      delay(30000);                  // waits for a second
      digitalWrite(pumpPin, LOW);    // sets the LED off
  }
}
