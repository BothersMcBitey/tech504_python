import requests
import json

#getting
post_code_req = requests.get("https://api.postcodes.io/postcodes/PR30SG")
content = post_code_req.content.decode("utf-8")
print(content)
postcode_dict = json.loads(content)
print(postcode_dict["result"]["region"])

for x in postcode_dict["result"]:
    print(x, ": ", postcode_dict["result"][x])
print()

#posting
json_body = json.dumps({'postcodes':["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type" : "application/json"}
post_code_req = requests.post("https://api.postcodes.io/postcodes/",headers=headers,data=json_body)#{\"postcodes\":[\"SO16 9HE\",\"SO16 1BJ\"]}")
print(post_code_req.status_code)
content = post_code_req.content.decode("utf-8")
print(content)