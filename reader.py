import json

# Opening JSON file
with open('data2.json', 'r') as openfile:

    # Reading from json file
    json_object = json.load(openfile)

print(json_object['data'])
print(type(json_object))
