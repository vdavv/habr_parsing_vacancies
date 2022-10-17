# habr_parsing_vacancies
current project parses vacancies from habr into a raw json file, handles them using bag of words (bow) and neural linguistic processing (nlp)
compares processed entered text to created data and outputs the best matching vacancies according to euclidean_similarity
# components purposes and launch order
1. parser_writer.py - parses and then writes raw data into json file
2. formatter.py - formats raw data into json file data_edited.json kind of {'1':{},'2':{},...}
3. nlp_handler.py - handles nlp processing, takes data_edited.json | outputs vocab.json and data_nlp.json
4. bow_handler.py - handles bow processing, takes data_nlp.json and vocab.json | outputs data_bow.json
5. comparator.py - compares entered text to parsed vacancies, takes vocab.json, data_bow.json, data_edited.json | outputs simplified vacancy cards in terminal
