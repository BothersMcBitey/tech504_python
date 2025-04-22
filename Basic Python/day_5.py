#===============================================================================
#  Task: Convert a Python dictionary into a JSON-formatted string and JSON file
#===============================================================================
import json
# create the dictionary
servers_dict = {
 "server1": {
 "hostname": "web-server-1",
 "ip_address": "192.168.1.1",
 "role": "web",
 "status": "active"
 },
 "server2": {
 "hostname": "db-server-1",
 "ip_address": "192.168.1.2",
 "role": "database",
 "status": "maintenance"
 }
}

dict_json = json.JSONEncoder().encode(servers_dict)
with open("server_2.json","w+") as f:
    f.write(dict_json)

with open("server_2.json", "r") as f:
    servers = json.JSONDecoder().decode(f.read())
    print(type(servers))
    for s in servers:
     print(servers[s])
     for k in servers[s].keys():
         print(f"Record key and sub value: '{k}' = '{servers[s][k]}'")

with open("server_2.json", "r") as f:
  text = f.read()
  print(text)
  servers = json.loads(text)
  print(servers)

# ===============================================================================
#  Task: Convert JSON file to valid YAML file
# ===============================================================================
import os
import sys
import yaml
# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")
# 1. Convert the JSON to YAML - use yaml library
with open(sys.argv[1], "r") as f, open(sys.argv[2], "w+") as o:
    servers = json.loads(f.read())#json.JSONDecoder().decode(f.read())
    yaml.dump(servers, o)

# ===============================================================================
#  Task: YAML scripting
# ===============================================================================
with open(sys.argv[2], "r") as f, open("json_from_yaml.json", "w+") as o:
    servers = yaml.full_load(f)
    print("==========")
    print(servers)
    json.dump(servers, o)