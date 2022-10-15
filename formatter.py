import json
import re

with open('data4.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

# print(json_object['data'])

to_json_dict_edited = dict()
i = 1
for card in json_object['data']:
    tmp = dict()
    for k, v in card.items():
        tmp.update({k: v.strip()})
    to_json_dict_edited.update({i: tmp})
    i += 1

# print(to_json_dict_edited[1])
# to_json_dict_f = dict()
# to_json_dict_f.update({'data':to_json_dict_edited})

json_object = json.dumps(to_json_dict_edited, indent=5, ensure_ascii=False)
with open("data4_edited.json", "w", encoding='utf8') as outfile:
    outfile.write(json_object)
