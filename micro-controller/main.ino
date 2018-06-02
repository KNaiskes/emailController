#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>
#include <IRremote.h>

byte mac[]    = {  0xDE, 0xED, 0xBA, 0xFE, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 100);
IPAddress server(192, 168, 1, 70);

IRsend irSend;

void ledStrip(char* command){
	char* commands[] = {
	"on", "off", "red","orange","dark_yellow","yellow",
	"yellow2","green","pea","cyan","light_blue","sky_blue","blue",
	"dark_blue","purple","violet","pink","white","flash","strobe",
	"fade","smooth"
	};

	long codes[] = {
	0xF7C03F,0xF740BF,0xF720DF,0xF710EF,0xF730CF,0xF708F7,
	0xF728D7,0xF7A05F,0xF7906F,0xF7B04F,0xF78877,0xF7A857,0xF7609F,
	0xF750AF,0xF7708F,0xF748B7,0xF76897,0xF7E01F,0xF7D02F,0xF7F00F,
	0xF7C837,0xF7E817
	};

	int length = sizeof(commands) / sizeof(commands[0]);
	int index = -1;
	for(int i=0; i<length; i++){
		if(!strcmp(commands[i], command)){
			index = i;
		}
	}
	if(index > -1){
		irSend.sendNEC(codes[index], 32);
		delay(10);
	}
}


void callback(char* topic, byte* payload, unsigned int length) {
  String receivedMessage;
  char copy[12]; // In order irSend work correctly, the command has to be char
  Serial.println();
  for(int i=0;i<length; i++){
	receivedMessage = receivedMessage +  (char)payload[i];
	}
	receivedMessage.toCharArray(copy,12);
	ledStrip(copy);
}

EthernetClient ethClient;
PubSubClient client(ethClient);

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    if (client.connect("arduinoClient")) {
      client.subscribe("ledStrip");
    } 
     else { delay(5000); }
  }
}

void setup()
{
  client.setServer(server, 1883);
  client.setCallback(callback);

  Ethernet.begin(mac, ip);
  // Allow the hardware to sort itself out
  delay(1500);
}

void loop()
{
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
