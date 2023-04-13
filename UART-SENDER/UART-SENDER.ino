#include <SoftwareSerial.h>

SoftwareSerial ads1(4, 2);
SoftwareSerial ads2(5, 3);

void setup() {
  Serial.begin(9600);
  ads1.begin(9600);
  ads2.begin(9600);
}

void loop() {
  Serial.print("plate20DUE");
  Serial.println(random());
  delay(500);
  ads1.print("plate2DUE");
  ads1.println(random());
  delay(500);
  ads2.print("plateDUE");
  ads2.println(random());
  delay(500);

}
