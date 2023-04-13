#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>
#include <ESP8266HTTPUpdateServer.h>

#define LPin 0
#define SPin 2
#define masLen 30000

#define OTAUSER         "admin"    // Логин для входа в OTA
#define OTAPASSWORD     "admin"    // Пароль для входа в ОТА
#define OTAPATH         "/firmware"// Путь, который будем дописывать после ip адреса в браузере.
#define SERVERPORT      80         // Порт для входа, он стандартный 80 это порт http
#define SENDSERVER      20          //Порт передачи данных

//MDNSResponder mdns;

SoftwareSerial ads1(SPin, 5);

IPAddress ip(192,168,102,42);  //статический IP
IPAddress gateway(192,168,102,99);
IPAddress subnet(255,255,255,0);


ESP8266WebServer server(SERVERPORT);

WiFiServer ServerJ(SENDSERVER);

WiFiClient cli;
bool firstCon = 1, working = 0;
byte sending = 0;

ESP8266HTTPUpdateServer httpUpdater;

byte mas[masLen];

const char* ssid = "MiRouter3"; const char* password =  "1234567890";
//const char* ssid = "BorisA50"; const char* password =  "00054003";

void handleRootPath() {            //Обработчик для корневого пути
  String a = "<html><head><title>iMaxB6duoWiFi</title></head><body><button onclick=\"sendButtonState()\">LedPin</button><script>function sendButtonState() {var xhttp = new XMLHttpRequest(); xhttp.open('POST', '/button', true); xhttp.send();}</script><br>";
  int t;
  if(working){
    t=200;
  }else{
    t=1000;
  }
  for(int i = 0; i < t; i++){
    if(mas[i] != '\0'){
      a += String(mas[i])+" ";
      if(i%20 == 0) a += "<br>";
    }
  }
  a += "<br>IMAX B6duo WiFiSender";
  a += "<meta http-equiv=\"refresh\" content=\"2\"></body></html>";
  server.send(200, "text/html;charset=utf-8", a);

}


void handlebutton() {            //Обработчик для корневого пути
  digitalWrite(LPin, !digitalRead(LPin));
  server.send(200, "text/html;charset=utf-8", "\0");
}



void setup(){
  pinMode(LPin, OUTPUT);
  Serial.begin(9600);
  ads1.begin(9600);

  WiFi.begin(ssid, password);
  WiFi.config(ip, gateway, subnet);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println(".");
  }
  /*if (MDNS.begin("esp8266", WiFi.localIP())) {
    Serial.println("MDNS responder started");
  }*/
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  httpUpdater.setup(&server, OTAPATH, OTAUSER, OTAPASSWORD);
  server.on("/", handleRootPath);
  server.on("/button", HTTP_POST, handlebutton);
  server.begin();
  ServerJ.begin();
  for(int i = 0; i < masLen; i++){
    mas[i] = '\0';
  }
}

void loop() {
  if(Serial.available()){
    for(int i = masLen-2; i != -1; i--){
      mas[i+1] = mas[i];
    }
    mas[0] = '\0';
    mas[0] = Serial.read();
    sending++;
  }
  if(ads1.available()){
    for(int i = masLen-2; i != -1; i--){
      mas[i+1] = mas[i];
    }
    mas[0] = '\0';
    mas[0] = ads1.read();
    sending++;
  }
   server.handleClient();

  if(working == 0){
    cli = ServerJ.available();
    if(cli) {
      working = 1;
      firstCon = 1;
      sending = 0;
    }
  }

    if (working == 1 && cli.connected()) {
      if(firstCon){
        for(int i = 0; i < masLen; i++){
          if(mas[i] != '\0'){
            cli.write(mas[i]);
          }
        }
        firstCon = 0;
        }else{
          for(int i = 0; i < sending; i++){
          cli.write(mas[i]);
        }
        sending = 0;
        }
  
    } else if(!cli.connected()){
      working = 0;
      cli.stop();
    }
}
