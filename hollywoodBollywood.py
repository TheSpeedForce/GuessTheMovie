#python based Hollywood-Bollywood movie guessing game.
from random import randint
import re , string
def movieselect(m):
    '''
This function selects any movie randomly from the movie list based on type of movie the user wants.
input=integer
output=string
    '''
    global movie, ques, blanks, vowels, spaces
    movietype={1:{1:'the bfg',
                  2:'spy',
                  3:'underworld',
                  4:'passengers',
                  5:'justice league',
                  6:'resident evil',
                  7:'ring',
                  8:'warcraft',
                  9:'captain america',
                  10:'the jungle book',
                  11:'finding dory',
                  12:'fantastic beasts and where to find them',
                  13:'deadpool',
                  14:'suicide squad',
                  15:'kung fu panda',
                  16:'ice age',
                  17:'transformers',
                  18:'toy story',
                  19:'terminator',
                  20:'fast and furious',
                  21:'zootopia',
                  22:'harry potter',
                  23:'inside out',
                  24:'shrek',
                  25:'doctor strange'},
               2:{1:'dangal',
                  2:'sultan',
                  3:'kaabil',
                  4:'befikre',
                  5:'ae dil hai mushkil',
                  6:'shivaay',
                  7:'dhoom',
                  8:'tanu weds manu',
                  9:'baar baar dekho',
                  10:'hum saath saath hain',
                  11:'kuch kuch hota hai',
                  12:'ek tha tiger',
                  13:'dil bole hadippa',
                  14:'ok jaanu',
                  15:'airlift',
                  16:'raees',
                  17:'baby',
                  18:'pink',
                  19:'khoobsurat',
                  20:'jolly llb',
                  21:'dear zindagi',
                  22:'sarkar',
                  23:'bahubali',
                  24:'bhaag milkha bhaag',
                  25:'housefull'}}
    if m==1:
        print '\nHollywood:\n'
    elif m==2:
        print '\nBollywood:\n'
    ques=""
    vowels=0
    spaces=0
    movie1=movietype[m][randint(1,25)]
    movie=movie1.upper()
    for i in range(len(movie)):
        if  movie[i]=='A' or movie[i]=='E' or movie[i]=='I' or movie[i]=='O' or movie[i]=='U':
            ques+=movie[i]
            vowels+=1
        elif movie[i]==' ':
            ques+=' '
            spaces+=1
        else:
            ques+='_'
            continue
    blanks=len(ques)-spaces-vowels
    return ques

def play():
    letters1=[]
    letters2=[]
    global letter
    ques1=ques
    chances=10
    while chances>0:
        letter1=raw_input('\nEnter a letter:')
        ifletter=letter1.isalpha()
        letter=letter1.upper()
        letters1+=list(letter)
        letters2+=list(letter)
        c1=letters1.count(letter)
        c2=letters2.count(letter)
        find=re.search(letter, movie)
        number=re.findall(letter,movie)

        if find!=None:
            position=find.start()

        if len(letter)>=2:
            if letter=='RULES':
                for w in letter:
                    letters1.remove(w)
                    letters2.remove(w)
                print '\n',rules
                print '\nLetters that have been used are',letters1
                print '\n',ques1
                continue

            elif letter=='QUIT':
                Quit=raw_input('\nAre you sure you wanna quit. You still have '+str(chances)+' chances left.\n If yes enter \'Y\' and if no enter \'N\'\n:')
                if Quit=='Y' or Quit=='y':
                    print 'The movie was \'',movie,'\'\nThanks for playing'
                    quit()
                    
                elif Quit=='n' or Quit=='N':
                    for v in letter:
                        letters1.remove(v)
                        letters2.remove(v)
                    print '\nLetters that have been used are',letters1
                    print '\n',ques1
                    continue

                else:
                    for v in letter:
                        letters1.remove(v)
                        letters2.remove(v) 
                    print 'Invalid input'
                    print '\nLetters that have been used are',letters1
                    print '\n',ques1
                    continue

            else:
                print '\nOne letter at a time'
                for i in letter:
                    letters1.remove(i)
                    letters2.remove(i)
                print '\nLetters that have been used are',letters1
                print '\n',ques1
                continue

        if letter.isdigit():
            print '\nNumbers not allowed'
            letters1.remove(letter)
            print '\nLetters that have been used are',letters1
            print '\n',ques1
            print '\nYou still have', chances ,'chances left'
            continue

        if letter=='' or not ifletter:
            letters1.remove(letter)
            letters2.remove(letter)
            print '\nPlease enter a letter and not anything else'
            print '\nLetters that have been used are',letters1
            print '\n',ques1
            continue

        if chances==1:
            print '\nSorry but you have no more chances left. Thanks for playing. The movie was \''+movie+'\''
        else:
            if c2>=2:
                if c2==2 or c2==3:
                    print '\nThis letter has already been used'
                    letters1.remove(letter)
                    print '\nLetters that have been used are',letters1
                    print '\n',ques1
                    print '\nYou have',chances, 'chances left'
                    continue

                elif c2>3:
                    chances-=1
                    print '\nThis letter has been used more than thrice'
                    letters1.remove(letter)
                    print '\nLetters that have been used are',letters1
                    print'\n',ques1
                    print '\nYou have',chances, 'chances left'
                    continue

            elif letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
                print '\nVowels are not allowed'
                letters1.remove(letter)
                letters2.remove(letter)
                print '\nLetters that have been used are',letters1
                print '\n',ques1
                print '\nYou still have', chances ,'chances left'
                continue

            else:
                if find==None:
                    print '\nIncorrect'
                    print '\nLetters that have been used are',letters1
                    print '\n',ques1
                    chances-=1
                    print '\nYou have', chances ,'chances left'
                    continue

                elif position<len(movie):
                    print '\nCorrect'
                    print '\nLetters that have been used are',letters1
                    if len(number)>=2:
                        find2=re.finditer(letter,movie)
                        for match in find2:
                            ques1=ques1[:(match.span()[0])]+letter+ques1[(match.span()[1]):]
                        print '\n',ques1
                        position=None
                        if ques1==movie:
                            print '\nYou win with a score of', chances
                            quit()
                        else:
                            print '\nYou still have', chances, 'chances left'
                            continue

                    else:
                        ques1=ques1[:(position)]+letter+ques1[(position+1):]
                        print '\n',ques1
                        position=None
                        if ques1==movie:
                            print '\nCongratulations. You win with a score of', chances,'\n'
                            break
                        else:
                            print '\nYou still have', chances, 'chances left'
                            continue
def main():
    global rules
    rules='The rules of this game are as follows: \na) You have to give one letter at a time (even if you guess the whole movie in one go). \nb) You have 10 chances for guessing a letter. \nc) One incorrect guess reduces 1 chance. \nd) No reduction in chances for guess letters being a vowel or a number.\ne) If a letter(correct or incorrect) is given more than thrice then chances will reduce by 1.\nf) To know the rules of the game in between, enter \'rules\'\ng) If you want to end the game in between, enter \'quit\'\n'
    print "\n|-x-x-x-x-x-x-x-x-x-x-Hollywood-Bollwood movie guessing game.-x-x-x-x-x-x-x-x-x-x-|"
    choice=raw_input('Enter \n\'P\' for Playing the game.\n\'R\' for reading the rules of the game.\n\'Q\' to quit the game\n:')
    if choice=='r' or choice=='R':
        print '\n', rules
        main()
    elif choice=='p' or choice=='P':
        while True:
            global t
            t1=raw_input('Enter \n\'1\' for getting a Hollywood movie \n\'2\' for getting a Bollywood movie \n:')
            if t1.isdigit():
                t=int(t1)
                if t==1 or t==2:
                    print movieselect(t), '\nThere are',blanks,'blanks in this movie and', spaces, 'space(s)'
                    play()
                else:
                    print '\nPlease enter 1 or 2 only'
            elif t1=='quit':
                surity=raw_input('Are you sure you want to quit. Enter \'Y\' if yes and \'N\' if no\n:')
                if surity=='y' or surity=='Y':
                    quit()
                elif surity=='n' or surity=='N' :
                    continue
                else:
                    print 'Invalid Input'
                    continue
            elif t1=='rules':
                print '\n', rules
                continue
            else:
                print '\nInvalid input'
                continue
    elif choice=='q' or choice=='Q':
        surity2=raw_input('Are you sure you want to quit. Enter \'Y\' if yes and \'N\' if no\n:')
        if surity2=='y' or surity2=='Y':
            quit()
        elif surity2=='n' or surity2=='N' :
            main()
        else:
            print 'Invalid input'
            main()
    else:
        print 'Invalid input'
        main()        
main()

        


    
    
