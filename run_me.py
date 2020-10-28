import random 
import enchant
x = False
no = 0
name_lower= str(input("Input a word: "))
name = name_lower.upper()
limit = int(input("enter no. of permutations you want: "))
correct_words = []
while no != limit :
    listt=[]
    for i in range (0, len(name)):
        alphabet = name[random.randrange(0,len(name))]
        if alphabet not in listt :
            listt.append(alphabet)
    answer ="".join(listt)
    x = enchant.Dict("en_UK").check(answer)
    if x == True and answer not in correct_words :
        correct_words.append(answer)
        no  = no +1
print(correct_words)
