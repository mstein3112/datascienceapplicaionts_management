from string import punctuation
PUNCTUATIONS = punctuation + "“”"

def clean_to_lower(text:str) -> str:
    return text.lower()

def clean_punctuation(text:str) -> str:
    output_string = ""
    for character in text:
        if character not in PUNCTUATIONS:
            output_string += character
    return output_string

