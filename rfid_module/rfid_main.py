from rfidController import RFIDController
import paho.mqtt.client as mqtt
import time

HOST = "localhost"
PORT = 1883
TOPIC = "TAKE_LABS_DOOR"

while True:
    try:
        rfid = RFIDController()
        
        mqtt_client = mqtt.Client()
        mqtt_client.connect(HOST, port=PORT)
        
        print("Iniciado...")
        time.sleep(0.05)
        id = rfid.read()
        print(id)
        
        if rfid.hasAccess(id):
            # Publicar na fila open
            mqtt_client.publish(TOPIC, "OPEN")
        else:
           # Publicar na fila refused
           mqtt_client.publish(TOPIC, "REFUSED")
        
    finally:
        time.sleep(0.05)