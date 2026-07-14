import pandas as pd
import matplotlib.pyplot as plt

files = {
    "MQTT": "mqtt_latency_results_positive.csv",
    "ROS2": "ros2_latency_results.csv",
}
for name, file in files.items():
    df = pd.read_csv(file)
    latency = df["latency_ms"]
    print(name)
    print(latency.describe())
    plt.figure()
    plt.plot(range(1, len(latency)+1), latency)
    plt.xlabel("Message number")
    plt.ylabel("Latency / transfer time (ms)")
    plt.title(f"{name} latency")
    plt.grid(True)
    plt.savefig(f"{name.lower()}_latency_graph.png", dpi=300)
