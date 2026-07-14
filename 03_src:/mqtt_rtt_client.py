import json
import time
import csv
import paho.mqtt.client as mqtt

BROKER = "192.168.0.106"  # Pi2 broker IP
PORT = 1883
REQUEST_TOPIC = "mqtt/rtt/request"
REPLY_TOPIC = "mqtt/rtt/reply"
NUM_MESSAGES = 100
INTERVAL = 0.1

send_times = {}
received_acks = 0

csv_file = open("mqtt_rtt_results.csv", "w", newline="")
writer = csv.writer(csv_file)
writer.writerow([
    "message_id",
    "send_time",
    "ack_time",
    "rtt_ms",
    "estimated_one_way_latency_ms",
    "payload_size_bytes"
])

def on_connect(client, userdata, flags, rc):
    print("RTT client connected with code", rc)
    client.subscribe(REPLY_TOPIC)

def on_message(client, userdata, msg):
    global received_acks
    ack_time = time.time()
    data = json.loads(msg.payload.decode())
    message_id = data["message_id"]
    payload = data["payload"]

    if message_id in send_times:
        send_time = send_times[message_id]
        rtt_ms = (ack_time - send_time) * 1000
        one_way_ms = rtt_ms / 2
        payload_size = len(payload.encode("utf-8"))
        print(
            f"ACK {message_id} | RTT: {rtt_ms:.3f} ms | "
            f"Estimated one-way: {one_way_ms:.3f} ms | payload: {payload_size} bytes"
        )
        writer.writerow([message_id, send_time, ack_time, rtt_ms, one_way_ms, payload_size])
        csv_file.flush()
        received_acks += 1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_start()
time.sleep(1)

print("Starting MQTT RTT test...")
for i in range(1, NUM_MESSAGES + 1):
    payload = {"message_id": i, "payload": "X" * 256}
    send_times[i] = time.time()
    client.publish(REQUEST_TOPIC, json.dumps(payload))
    print(f"Sent {i}")
    time.sleep(INTERVAL)

while received_acks < NUM_MESSAGES:
    time.sleep(0.1)

client.loop_stop()
client.disconnect()
csv_file.close()
print("Finished MQTT RTT test.")
