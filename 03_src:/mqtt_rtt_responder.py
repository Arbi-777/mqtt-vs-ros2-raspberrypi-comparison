import json
import paho.mqtt.client as mqtt

BROKER = "192.168.0.106"
PORT = 1883

REQUEST_TOPIC = "mqtt/rtt/request"
REPLY_TOPIC = "mqtt/rtt/reply"

def on_connect(client, userdata, flags, rc):
    print("Responder connect with code", rc)
    client.subscribe(REQUEST_TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    reply = {
        "message_id" : data["message_id"],
        "payload": data["payload"]
    }

    client.publish(REPLY_TOPIC, json.dumps(reply))
    print(f"ACK sent for {data['message_id']}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
