
int fanPin = 2;
String serialPc;
String fanStatus = "ON";
void setup() {
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(fanPin,OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
    while(Serial.available()) {
        serialPc = Serial.readString();// read the incoming data as string
        serialPc.trim();
        Serial.println("BIOSINO v0.1");
        Serial.println("Help -h");
        if (serialPc == "-h"){
            Serial.println("[FAN] ON/OFF ... fanOn/fanOff");
            Serial.print("[BIOSINO] status ... status");
        }
        if ( serialPc == "fanOn" ){
            
            Serial.println("Fan [ON]");
            fanStatus = "ON";
        }
        if ( serialPc == "fanOff" ){
            
            Serial.println("Fan [OFF] ");
            fanStatus = "OFF";
        }
        if(serialPc == "status"){
            Serial.println("Fan ["+fanStatus+"]");
        }
    }

   if (fanStatus == "ON"){
       digitalWrite(fanPin, HIGH);
   } else if ( fanStatus == "OFF"){
       digitalWrite(fanPin, LOW);
   }
   
}
