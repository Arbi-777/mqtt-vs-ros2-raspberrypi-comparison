import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import json
import csv

class LatencySubscriber(Node):
    def __init__(self):
        super().__init__('latency_subscriber')

        self.subscriber = self.create_subscription(
            String,
            'ros2_latency_topic',
            self.listener_callback,
            10
        )

        self.csv_file = open("ros2_latency_results.csv", "w", newline="")
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow(["seq", "send_time", "receive_time", "latency_ms", "payload_size_bytes"])

        print("ROS 2 subscriber started. Waiting for messages...")

    def listener_callback(self, msg):
        receive_time = time.time()
        data = json.loads(msg.data)

        seq = data["seq"]
        send_time = data["send_time"]
        payload = data["payload"]

        latency_ms = (receive_time - send_time) * 1000
        payload_size = len(payload.encode("utf-8"))

        self.writer.writerow([seq, send_time, receive_time, latency_ms, payload_size])
        self.csv_file.flush()

        print(f"Received {seq} | Latency: {latency_ms:.3f} ms | Payload: {payload_size} bytes")

def main():
    rclpy.init()
    node = LatencySubscriber()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
