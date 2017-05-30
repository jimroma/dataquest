vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = []
tokenized_vocabulary = vocabulary.split(" ")
print(tokenized_vocabulary[0:5])