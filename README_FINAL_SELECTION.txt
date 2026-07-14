Seminar Final Sorted Files - ROS 2 vs MQTT

IMPORTANT STATUS:
- ROS 2 one-way latency data is available: 01_Data/ros2_latency_results.csv
- MQTT positive one-way latency data is available from the earlier working run: 01_Data/mqtt_latency_results_positive.csv
- The later MQTT timestamp run produced negative latency because Pi1 and Pi2 clocks were not synchronized. It is kept only in 05_Notes_Not_For_Submission/mqtt_latency_negative_clock_unsynced.csv and should NOT be used as a final result.
- For a stronger final submission, run MQTT RTT using 03_Code/mqtt_rtt_client.py on Pi1 and 03_Code/mqtt_rtt_responder.py on Pi2, then add mqtt_rtt_results.csv to 01_Data.

USE FOR SUBMISSION:
1) 01_Data/ros2_latency_results.csv
2) 01_Data/mqtt_latency_results_positive.csv
3) 01_Data/summary_statistics.csv
4) 02_Graphs/*.png
5) 03_Code/ros2_latency_pub.py and ros2_latency_sub.py
6) 03_Code/mqtt_rtt_client.py and mqtt_rtt_responder.py if you present RTT; otherwise mqtt_oneway_subscriber_clock_sync_required.py only as implementation evidence.
7) 04_Evidence_Screenshots/* for report screenshots.

DO NOT SUBMIT:
- .swp files
- ._ Apple metadata files
- duplicate screenshots
- empty latency files
- mqtt_latency_negative_clock_unsynced.csv as final evidence

Summary statistics from usable datasets:
protocol  messages  avg_latency_ms  min_latency_ms  max_latency_ms  std_latency_ms  median_latency_ms  payload_size_bytes
    MQTT      9167       12.530417        3.190041      109.775066        4.517989          11.532307                 256
    ROS2        99       54.019215       39.153337      127.207756       19.390335          44.868946                 256
