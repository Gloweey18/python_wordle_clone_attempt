import random


def get_words() :
    with open("words.txt","r") as my_words :
        data = my_words.read()
        word_list = data.split("\n")
        my_words.close()
    return word_list

def pick_word(word_list) :
    word_index = random.randint(0,len(word_list)-1)
    my_word = word_list[word_index]
    word = my_word.lower()
    print(word)
    return word

def make_guess_line(word) :
    underscore_list=[]
    for i in word :
        underscore_list.append("_")
    for j in underscore_list :
        print(j,end='')
        
if __name__ == "__main__" :
    word_list = get_words()
    word = pick_word(word_list)
    make_guess_line(word)
    
    
        
    
        