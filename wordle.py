import random


def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


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
    return word

def make_guess_line(word) :
    underscore_list=[]
    for i in word :
        underscore_list.append("_")
    for j in underscore_list :
        print(j,end='')
    print("\n")

        
def get_word(guess) :
    while True :
        var = None
        guessed_word = input(f"Guess {guess} : ")
        for i in guessed_word :
            if i.isdigit() == True :
                var = False
                break
            elif i.isalpha() == True :
                var = True
                
            
        if len(guessed_word) > 5 or len(guessed_word) < 5 :
            print("Your word should be 5 letters long")
            continue
        elif var == False :
            print("Please enter a word.")
            continue
        elif var == True :
            break
    return guessed_word.lower()


def check_word(word,guessed_word) :
    correct_letter = '-'
    incorrect_letter = '-'
    misplaced_letter = '-'
    for i in guessed_word :
        if i in word :
            if list(guessed_word).index(i) == list(word).index(i) :
                correct_letter = f"{correct_letter}, {i}"
            else :
                misplaced_letter = f"{misplaced_letter}, {i}"
        else :
            incorrect_letter = f"{incorrect_letter}, {i}"
    if guessed_word == word :
        print("Correct!")
        return True
    else :
        correct_letter = correct_letter.strip('-')
        incorrect_letter = incorrect_letter.strip('-')
        misplaced_letter = misplaced_letter.strip('-')
        print(f"Correct letters : {correct_letter}")
        print(f"Incorrect letters : {incorrect_letter}")
        print(f"Misplaced letters : {misplaced_letter}")
        return False




if __name__ == "__main__" :
    print("Welcome to wordle you have 6 chances to play")
    guess = 0
    word_list = get_words()
    word = pick_word(word_list)
    while guess < 6 :
        guess += 1
        guessed_word = get_word(guess)
        check=check_word(word,guessed_word)
        if check == True :
            print("You won!")
            break
    else:
        print("You lost!")
        print(f"The word was : {word}")
    
        
    
        