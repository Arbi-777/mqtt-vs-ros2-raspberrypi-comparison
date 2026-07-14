import json
import time
import csv
import paho.mqtt.client as mqtt

BROKER = "192.168.0.106"
PORT = 1883
TOPIC = "test/topic"

# Create CSV file
csv_file = open("mqtt_latency.csv", "w", newline="")
csv_writer = csv.writer(csv_file)

csv_writer.writerow([
    "message_id",
    "sent_time",
    "received_time",
    "latency_ms"
])

received_messages = 0


def on_connect(client, userdata, flags, rc):
    print("Connect with result code", rc)
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    global received_messages

    received_messages += 1

    try:
        data = json.loads(msg.payload.decode())

        message_id = data["message_id"]
        sent_time = data["timestamp"]

        received_time = time.time()

        latency_ms = (received_time - sent_time) * 1000
        payload_size = len(msg.payload)

        print(
            f"Received {message_id} | "
            f"Latency: {latency_ms:.3f} ms |"
            f"payload: {payload_size} bytes"
        )

        csv_writer.writerow([
            message_id,
            sent_time,
            received_time,
            latency_ms
        ])

        csv_file.flush()

    except Exception as e:
        print("Error:", e)


client  =mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

print(f"Connecting to broker {BROKER}...")

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("\nStopping subscriber...")

finally:
    csv_file.close()
