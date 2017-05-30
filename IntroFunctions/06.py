
f = open("story.txt", "r")
story_string = f.read()
#print(story_string)

def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\\n", "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)
cleaned_story = clean_text(story_string)
print(cleaned_story)