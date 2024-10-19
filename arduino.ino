int x;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1000);  
  Serial.flush(); 
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readString();
    x = input.toInt();
    int resultado = x + 1;
    Serial.println(resultado);
  }
}
