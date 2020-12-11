def brandnewfunc(str= "abhi",find= " "):
    count = str.count(find)
    start = 0
    for i in range(0,count+1):
        a = str.find("ab",start,-1)
        start=a +1
        print(a, end ="," )
def primefactor(n, checkprime = "do not check for prime"):
    prime= [2]
    factors = []
    for i in range(2,n+1):
            if all([i%j != 0 for j in prime]):
                prime.append(i)
    if checkprime == "checkprime":
        if n in prime:
            print(n,"is prime")
        else:
            print("n is not prime")
    else:
        for a in prime:
            if n%a ==0:
                factors.append(a)
        print(factors)


def anagramfinder(name,limit=1): #accepts : name = a word/string, limit = no. of word to find.
        #importing
        import random 
        import enchant
        # initialization of var.
        x = False
        no = 0
        correct_words = []
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
def frequency_unique_duplicate(lst):                  #displays the frequency of elements in list alongwith the unique elements amd the duplicate ones
    unique = []
    duplicate= []
    for i in lst:
        frequency = lst.count(i)
        if frequency == 1:
            print(i,"'s frequency ",frequency,sep="")
            unique.append(i)
        elif duplicate.count(i) ==0 and i not in unique :
            duplicate.append(i)
            print(i,"'s frequency",frequency)
    print("unique ele",unique,"duplicate ele",duplicate)