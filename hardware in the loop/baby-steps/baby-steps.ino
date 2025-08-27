float number;
String message;

void setup() {

Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0){
    number = Serial.parseFloat();
    message = String(number*10.01) + " hey " + String(number-0.5);
    Serial.println(message);

  }

}
