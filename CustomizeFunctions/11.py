story_string = open("story.txt", 'r').read()
vocabulary = open("dictionary.txt", 'r').read()
#this need the tokenize function

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    # Add ending parentheses.
    text = open(text_file).read()
    
    # Fix indentation.
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt", special_characters=[",",".","'",";","\n"])
print(final_misspelled_words)