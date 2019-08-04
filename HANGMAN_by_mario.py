print('----------------------HANGMAN----------------------')
print()
print('Rules:Total 6 guesses \n      User Have To Give the Abstract')
print()
print('Note:Enter the Movie name without spaces\nAnd you will not see your typed movie letters as it is hidden\nSo type it correctly')
import time
from colorama import Fore,Back,Style
time.sleep(4)
import getpass  

q=getpass.getpass(prompt='Enter The Movie : ')
f=len(q)*'*'
print(f)
f=list(f)
print()
d=input('Enter The Description : \n Language: ')
y=input('Release Date: ')
print()
print('Length Of the Movie Name: {}\nLanguage: {}\nYear Of release: {}'.format(len(q),d,y))
print('Start Guessing!! You Have 6 Tries :')
print(f)
time.sleep(2)
t=6
def indexes(word,letter):
    result = list()
    for i,x in enumerate(word):
        if x == letter:
            result.append(i)
    return result
while t>0:
    rt=input('enter the character:')
    
    corr=0
    
    if rt in q:
        i=indexes(q,rt)
        for j in i:
            f[j]=rt
        corr+=1
        
    else:
        print('oops-------Not There :)')
        t=t-1
        print('You Have {0} Tries left'.format(t))
        
    
    print(f)
    if t==0:
        print('--------------YOU LOST-----------------')
        
        break
    else :
        
        if '*' not in f:
            print('Congratulations.....................'.upper())
            print('--------------YOU WON--------------')
            break
        else:
            
            continue
time.sleep(5)


    
    


   





