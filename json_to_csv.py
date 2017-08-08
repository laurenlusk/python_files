import json
import csv
from os import chdir
from collections import OrderedDict

# Navigate to folder with json file
chdir("/home/ece411c/Documents")

# Open json file
with open('data_Tucson_to_Phoenix.json', 'r') as f:
    file_str = f.read()
    data = json.loads(file_str, object_pairs_hook=OrderedDict)

# Open new csv file
f = csv.writer(open("data_TtoP_Aug4.csv", "wb+"))

# Write csv header
f.writerow(["event length", "event time", "event type", "power",
            "frequency", "rate", "time"])

# Write data
for x in data:
    f.writerow([#x["Latitude"],
                #x["Longitude"],
                x["es::event_length"],
                x["es::event_time"],
                x["es::event_type"],
                #x["gain"],
                #x["gps_present"],
                x["power"],
                #x["ref_locked"],
                x["rx_freq"][1],
                x["rx_rate"][1],
                x["rx_time"][1][0]+x["rx_time"][1][1]])
                #x["temp"] ])