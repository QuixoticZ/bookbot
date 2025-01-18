def main():
    path = "books/frankenstein.txt"
    full_text = get_text(path) 
    num_words = word_count(full_text)
    report_details = char_report(letter_count(full_text))
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for c in report_details:
        print(f"The '{c["char"]}' character was found {c["count"]} times")
    print("--- End Report ---")   
    
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

def sort_on(dict):
    return dict["count"]

def char_report(char_dict):
    list_dict=[]
    for i in char_dict:
            if i.isalpha() == True:
                char = char_dict[i]
                list_dict.append({"char":i,"count":char})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict



main()