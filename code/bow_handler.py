import json

with open('../data_json/data6_nlp.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

with open('../data_json/vocab.json', 'r') as openfile:
    # Reading from json file
    vocab_dict = json.load(openfile)


def bow(n: str, v: list) -> list:
    bow_list = list()
    for word in vocab_dict['vocab_' + n]:
        bow_list.append(v.count(word))
    return bow_list


to_bow_json = dict()
for i in range(1, len(json_object) + 1):
    card = json_object[f'{i}']
    tmp = dict()
    for n, v in card.items():
        tmp.update({n: bow(n, v)})
    to_bow_json.update({i: tmp})

with open("../data_json/data6_bow.json", "w", encoding='utf8') as outfile:
    outfile.write(json.dumps(to_bow_json, indent=2, ensure_ascii=False))
