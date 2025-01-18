def main():
    path = "books/frankenstein.txt"
    full_text = get_text(path) 
    num_words = word_count(full_text)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print (letter_count(full_text))
    
    
def get_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    word_array = text.split()
    return len(word_array)

def letter_count(text):
    char_dict = {}
    for l in text:
        if l.lower() not in char_dict:
            char_dict[l.lower()]=1
        else:
            char_dict[l.lower()] +=1
    return char_dict

def char_report(char_dict):
    pass


main()