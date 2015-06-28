char sepStr[ ] = ",";

int lightSensorPin = A1;
int lightSensorValue = 0;
int lightness = 0;

int tempSensorPin = A0;
int tempSensorValue = 0;
int temperature = 0;

int sampleDelayMs = 10*60;

void setup() {
  Serial.begin(9600);
}

void loop() {
  lightSensorValue = analogRead(lightSensorPin);
  lightness = map( lightSensorValue, 0, 1023, 1023, 0 );

  tempSensorValue = analogRead(tempSensorPin);
  temperature = map( tempSensorValue, 0, 1023, -50, 450 );

  Serial.print( lightness );
  Serial.print( sepStr );
  Serial.println(temperature);
  delay(sampleDelayMs);
}

