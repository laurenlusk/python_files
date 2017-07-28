import json
import csv
from os import chdir
from collections import OrderedDict

chdir("/home/ece411c/Documents")

with open('gps_test.json', 'r') as f:
    file_str = f.read()
    data = json.loads(file_str, object_pairs_hook=OrderedDict)

f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["latitude", "longitude", "event length", "event time", "event type", "gain", "gps present",
            "power","ref lock", "rx frequency", "rx rate", "rx time", "temp"])

for x in data:
    f.writerow([x["Latitude"],
                x["Longitude"],
                x["es::event_length"],
                x["es::event_time"],
                x["es::event_type"],
                x["gain"],
                x["gps_present"],
                x["power"],
                x["ref_locked"],
                x["rx_freq"][1],
                x["rx_rate"][1],
                x["rx_time"][1],
                x["temp"]])