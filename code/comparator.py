import json
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    PER,
    NamesExtractor,
    Doc,
)

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
names_extractor = NamesExtractor(morph_vocab)
# intended to compare bow's of inputted text and parsed ones and print the closest vacancies


with open('../data_json/vocab.json', 'r') as openfile:
    # Reading from json file
    vocab_dict = json.load(openfile)

with open('../data_json/data6_bow.json', 'r') as openfile:
    # Reading from json file
    data_bow_dict = json.load(openfile)

with open('../data_json/data6_edited.json', 'r') as openfile:
    # Reading from json file
    data_edited = json.load(openfile)


def nlp(v: str) -> list:
    text = v
    doc = Doc(text)
    data = []
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.sents[0].morph.print()
    doc.tag_ner(ner_tagger)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
        if token.pos not in ["PUNCT", "CCONJ", "ADP"]:
            data.append(token.lemma)
    return data


def bow(n: str, v: list) -> list:
    bow_list = list()
    for word in vocab_dict['vocab_' + n]:
        bow_list.append(v.count(word))
    return bow_list


def euclidean_similarity(x: list, y: list) -> float:
    _sum = 0
    for i in range(len(x)):
        _sum += (x[i] - y[i]) ** 2
    _sum **= 1 / 2
    # sensitivity of algorithm
    return 1 / (0.1 + _sum)


print('Введите описание желаемой вакансии:')
in_text = input()
in_nlp = nlp(in_text)
in_bow = [bow('vacancy', in_nlp), bow('requirements', in_nlp)]
similarity = dict()
# print(in_bow)

for i in range(1, len(data_bow_dict) + 1):
    card_bow = data_bow_dict[str(i)]
    vs = float()
    rs = float()
    ts = float()
    for n, v in card_bow.items():
        if n == 'vacancy':
            vs = euclidean_similarity(in_bow[0], v)
        elif n == 'requirements':
            rs = euclidean_similarity(in_bow[1], v)
    # weight coefficients here
    ts = 1 * vs + 5 * rs
    similarity.update({i: ts})

similarity_sorted = list()
while len(similarity) > 0:
    id_max = list(similarity.items())[0][0]
    s_max = similarity[id_max]
    for id, s in similarity.items():
        if s > s_max:
            s_max = s
            id_max = id
    similarity_sorted.append({id_max: s_max})
    similarity.pop(id_max)

# number of vacancies to print
n_vacs = 10
# debugging
# print(similarity_sorted)
print('\n')
for i in range(n_vacs):
    idc = list(similarity_sorted[i].keys())[0]
    card_vc = data_edited[str(idc)]
    print('-' * 100)
    for n, v in card_vc.items():
        if n == 'vacancy':
            print('vacancy:', v)
        elif n == 'company':
            print('company:', v)
        elif n == 'requirements':
            print('requirements:', v)
        elif n == 'link':
            print('link:', v)
    print('-' * 100 + '\n')
