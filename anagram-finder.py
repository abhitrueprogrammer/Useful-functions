#importing
import random 
import enchant
# initialization of var.
x = False
no = 0
correct_words = []
#taking input and capatalizing the name
name_lower= str(input("Input a word: "))
name = name_lower.upper()
limit = int(input("enter no. of permutations you want: "))
#actual work
while no != limit :
    alphabetlist=[]
    #Takes all the letters, randomly select a letter one by one,no. of times the length of name[word inputted] deletes which repeats,
    # gives out a list of random number of random alphabets
    for i in range (0, len(name)):                         
        alphabet = name[random.randrange(0,len(name))]
        if alphabet not in alphabetlist :
            alphabetlist.append(alphabet)
    #changes list of letters to a word
    answer ="".join(alphabetlist)
    #check if the word is in database of enchant, ie if its a english word
    x = enchant.Dict("en_UK").check(answer)
    #if the answer hasen't been repeated add it in a list, and thus lower the no. of times the loop is executed
    # (loop is executed till the no. of letters in list== no. of permutations the user wants)
    if x == True and answer not in correct_words :
        correct_words.append(answer)
        no  = no +1
#displaying all the words that are found.
print(correct_words)
