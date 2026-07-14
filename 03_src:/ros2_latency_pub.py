import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import json

class LatencyPublisher(Node):
    def __init__(self):
        super().__init__('latency_publisher')
        self.publisher_ = self.create_publisher(String, 'ros2_latency_topic', 10)
        self.seq = 0
        self.total_messages = 100
        self.timer = self.create_timer(0.1, self.publish_message)

    def publish_message(self):
        self.seq += 1
        data = {
            "seq": self.seq,
            "send_time": time.time(),
            "payload": "x" * 256
        }
        msg = String()
        msg.data = json.dumps(data)
        self.publisher_.publish(msg)
        print(f"Sent {self.seq}")
        if self.seq >= self.total_messages:
            self.timer.cancel()
            self.get_logger().info("Finished sending messages.")
            rclpy.shutdown()

def main():
    rclpy.init()
    node = LatencyPublisher()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
