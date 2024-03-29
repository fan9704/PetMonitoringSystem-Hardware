import paho.mqtt.client as mqtt
import os 

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("weight/#")
    client.subscribe("temperature/#")
    client.subscribe("humidity/#")
    client.subscribe("water/#")
    client.subscribe("distance/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(
    username=os.getenv("MQTT_USERNAME","guest"),
    password=os.getenv("MQTT_PASSWORD","guest")
)
client.connect(
    os.getenv("MQTT_SERVER_IP","127.0.0.1"), 
    int(os.getenv("MQTT_SERVER_PORT",1883)),
    60
)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()