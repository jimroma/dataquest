f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\\n"]

# Previous code for clean_text().
def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for clean_char in special_characters:
        cleaned_string = cleaned_string.replace(clean_char,"")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

cleaned_story = clean_text(story_string, clean_chars)
print(cleaned_story)