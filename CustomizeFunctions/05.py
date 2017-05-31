story_string = open("story.txt", 'r').read()
vocabulary = open("dictionary.txt", 'r').read()

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)

def spell_check(vocabulary_file, text_file, special_characters = [",",".","'",";","\n"]):
    misspelled_words = []
    vocab = open(vocabulary_file, "r").read()
    txt = open(text_file, "r").read()
    tokenized_vocabulary = tokenize(vocab, special_characters = [",",".","'",";","\n"], clean = False)
    tokenized_text = tokenize(txt, special_characters = [",",".","'",";","\n"], clean=True)
    for tok in tokenized_text:
        if tok not in tokenized_vocabulary and tok != '':
            misspelled_words.append(tok)
    return(misspelled_words)
    
final_misspelled_words = []
final_misspelled_words = spell_check("dictionary.txt", "story.txt")
print(final_misspelled_words)