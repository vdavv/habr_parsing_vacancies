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

with open('../data_json/data6_edited.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
names_extractor = NamesExtractor(morph_vocab)


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


# print(json_object['1'].items())
vocab_vacancy = list()
# vocab_description = list()
vocab_requirements = list()
to_data_nlp = dict()
for i in range(1, len(json_object) + 1):
    card = json_object[f'{i}']
    tmp = dict()
    for n, v in card.items():
        if n == 'vacancy':
            k = nlp(v)
            vocab_vacancy += k
            tmp.update({n: k})
        elif n == 'requirements':
            k = nlp(v)
            vocab_requirements += k
            tmp.update({n: k})
        """elif n == 'description':
            vocab_description += nlp(v)"""
    to_data_nlp.update({i: tmp})

# print(vocab)
with open("../data_json/vocab.json", "w", encoding='utf8') as outfile:
    outfile.write(json.dumps(
        {'vocab_vacancy': list(set(vocab_vacancy)),
         'vocab_requirements': list(set(vocab_requirements))}, ensure_ascii=False))

with open("../data_json/data6_nlp.json", "w", encoding='utf8') as outfile:
    outfile.write(json.dumps(to_data_nlp,indent=2, ensure_ascii=False))
"""with open('../data_json/vocab.txt', 'w', encoding='utf8') as outfile:
    outfile.write(str(set(vocab)))"""
