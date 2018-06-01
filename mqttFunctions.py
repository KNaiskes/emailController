import paho.mqtt.client as mqtt

def send_Mqtt_message(topic, message):
	client = mqtt.Client()
	client.connect("localhost", 1883)
	client.publish(topic, message)
	print("sent message to", topic,", message:",message)
	client.disconnect()
