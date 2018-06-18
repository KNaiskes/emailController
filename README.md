## Internet of Things Led Strip

### Components
- Raspberry Pi 2 (possibly any version would work)
- Arduino UNO
- Ethernet Shield 2
- IR transmitter Sensor

### How it works

A Raspberry Pi checks every five seconds if there is an unread E-mail. If there is
and is from the master user and contains a valid command it sends it to the
Arduino UNO via the MQTT protocol.

### Setup
- Enter in key.py the username, password and master credentials. Master is the
E-mail address that you will have to use in order to send commands to the led strip

- Install Python dependencies: pip3 install -r requirements.txt

#### Arduino dependencies

1. PubSubClient
2. IRremote


#### Known issues

- It is not possible to send the same E-mail twice in less than one minute as
Gmail will block it as spam.
