f = open("story.txt", 'r')
story_string = f.read()


def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

clean_chars = [",", ".", "'", ";", "\\n"]
cleaned_story = clean_text(story_string, clean_chars)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, clean_chars)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

tokenized_story = []
tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story)
