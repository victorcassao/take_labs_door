from GPIOController import GPIOController
import paho.mqtt.client as mqtt
import time

HOST = "localhost"
PORT = 1883
TOPIC = "TAKE_LABS_DOOR"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)


def on_message(client, userdata, message):
    
    msg_rcv = message.payload.decode('utf-8')
    topic_rcv = message.topic
    
    gpio_control = GPIOController()
    
    print("Message received")
    print(msg_rcv)
    
    if topic_rcv == TOPIC:
        if "OPEN" in msg_rcv:
            print("openning...")
            gpio_control.open_door()
        elif "REFUSED" in msg_rcv:
            pass

broker_address = "localhost"  # Broker address
port = 1883  # Broker port
# user = "yourUser"                    #Connection username
# password = "yourPassword"            #Connection password

client = mqtt.Client()  # create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_forever()