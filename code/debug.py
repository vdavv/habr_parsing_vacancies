import json

with open('../data_json/vocab.json', 'r') as openfile:
    # Reading from json file
    vocab_dict = json.load(openfile)

print(len(vocab_dict['vocab_vacancy']))
