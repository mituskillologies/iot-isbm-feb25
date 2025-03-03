int obstaclePin = 10;
int hasObstacle = LOW; // LOW MEANS NO OBSTACLE
void setup() {
  pinMode(obstaclePin, INPUT);
  Serial.begin(9600);
}
void loop() {
  hasObstacle = digitalRead(obstaclePin);
  if (hasObstacle == HIGH) {
    Serial.println("Stop something is ahead!!");
  }
  else {
    Serial.println("Path is clear");
  }
  delay(200);
}
