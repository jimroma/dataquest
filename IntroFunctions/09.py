#f = open("story.txt", 'r')
#story_string = f.read()
story_string = open("story.txt", 'r').read()

vocabulary = open("dictionary.txt", 'r').read()

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
misspelled_words = []
for word in tokenized_story:
    if word not in tokenized_vocabulary:
        misspelled_words.append(word)
        
print(misspelled_words)
