#Gibberish_Hangman.py
#
#Description: A game of gibberish hangman
#
#Programmed by: John Chan

import random as ran;
import turtle as stylus;
import turtle as prompt;


#Helper Functions
def move_pen(xcoord=0, ycoord=0):
    stylus.penup();
    stylus.setpos(xcoord, ycoord);
    stylus.pendown();
    return None;

def set_angle(default=0):
    angle = default-stylus.heading();
    stylus.left(angle);
    return None;

#Builder Functions
def word_builder(vow, con):

    chance = 35;
    length = ran.randint(4,9);
    syllable = ran.randint(2,3);
    wordsplit = length//syllable;
    word = list()

    for letter in range(length):
        if(letter<wordsplit):
            pick_letters(letter,0,word,chance,vow,con);
            if(word[letter] in con):
                chance=chance-25;
            else:
                chance=chance+25;
        elif(letter<wordsplit*2):
            pick_letters(letter,wordsplit,word,chance,vow,con);
            if(word[letter] in con):
                chance=chance-25;
            else:
                chance=chance+25;
        else:
            pick_letters(letter,wordsplit*2,word,chance,vow,con);
            if(word[letter] in con):
                chance=chance-25;
            else:
                chance=chance+25;
        chance=35;
        
    word = odds(word, vow, con);
    word = overload(word, vow, con);
    word = repetition(word, vow, con);
    word = endings(word,con);
        
    
    result = "";
    for character in range(len(word)):
        result = result + str(word[character]);   
    return result;
        
def pick_letters(state, threshold, word, chance, vow, con):
    if(state==threshold):
        word.append(con[ran.randint(0,len(con)-1)]);
    else:
        if(ran.randint(1,100)<chance):
            word.append(con[ran.randint(0,len(con)-1)]);
        else:
            word.append(vow[ran.randint(0,len(vow)-1)]);
    return word;

def repetition(word, vow, con):
    for each in range(len(word)-1):
        while(word[each]==word[each+1]):
            if(word[each+1] in con):
                word[each+1] = con[ran.randint(1,len(con)-1)];                                  
            else:
                word[each+1] = vow[ran.randint(1,len(vow)-1)];
    return word;

def overload(word, vow, con):
    for each in range(len(word)-2):
        if(word[each] and word[each+1] and word[each+2] in con):
            word[each+1] = vow[ran.randint(1,len(vow)-1)];
        else:
            word[each+1] = con[ran.randint(1,len(con)-1)];
    return word;

def odds(word, vow, con):   
    unusual = ['x','z','p','f','v','q','g','j']    
    for each in range(len(word)-1):
        if(word[each] in con):
            while(word[each+1] in unusual):
                word[each+1] = con[ran.randint(1,len(con)-1)];
    return word;

def endings(word,con):
    unusual = ['k','w','v','j','q']
    while(word[len(word)-1] in unusual):
        word[len(word)-1] = con[ran.randint(1,len(con)-1)];
    return word;

#Game
def game(word):
    stylus.hideturtle();
    stylus.speed(5);
    guess = "";
    invalid = True;
    position = 250;
    stage = 1;
    step = 10//len(word);
    
    lives = len(word);
    checker = list();

    for elements in range(len(word)):
        checker.append(False);
        
    draw_frame();
    move_pen(position, -250);
    set_angle(180);
    draw_blanks(lives)

    while (lives>0 and (False in checker)):      
        while(invalid):
            guess = prompt.textinput("Guess","Guess a character:");
            if(guess is None):      
                print("Console: Please enter an argument.");
                invalid=False;
            elif(len(guess)!=1):
                print("Console: Please enter a character only.");
            elif(guess.isnumeric()):
                print("Console: Please enter only one character.");
            else:
                invalid = False;

        for letter in range(-1,-(len(word)+1),-1):
            if(guess==word[letter]):
                checker[letter]=True;
                position = 225-(45+get_space(len(word)))*(-(letter+1));
                move_pen(position,-235);
                stylus.pendown();
                stylus.write(guess);              

        if(guess not in word):
            while(stage<=step and step<=step*len(word)):
                hang_man(stage);
                stage=stage+1;
            step=step+(10//len(word));
            if(step>(10//len(word))*len(word)):
                while (stage<=10):
                    hang_man(stage)
                    stage=stage+1;
            
            lives=lives-1;
            print(guess,"is incorrect!",lives,"lives remaining!");
        invalid = True;

    if(False not in checker):
        print("You win!");
        print("The word was indeed ",word,"!");
    else:
        print("You lose!");
        print("The correct word was: ",word);
    stylus.bye();
    prompt.bye();
    return None;

def hang_man(step=1):
    
    if(step==1):
        move_pen(0,-125);
        set_angle(180);
        stylus.forward(125);
    elif(step==2):   
        move_pen(0,-125);
        set_angle();
        stylus.forward(125);
    elif(step==3):
        move_pen(0,-125);
        set_angle(90);
        stylus.forward(250);
    elif(step==4):    
        move_pen(0,125);
        set_angle();
        stylus.forward(100);
    elif(step==5):
        move_pen(100, 125);
        set_angle(270);
        stylus.forward(25);
    elif(step==6):
        move_pen(100,90);
        set_angle();
        stylus.circle(5)
    elif(step==7):
        move_pen(100,90);
        set_angle(270);
        stylus.forward(25);
    elif(step==8):
        move_pen(100,80);
        set_angle();
        stylus.forward(10);
        move_pen(100,80);
        set_angle(180);
        stylus.forward(10);
    elif(step==9):
        move_pen(100,65);
        set_angle(225);
        stylus.forward(15);
        move_pen(100,65);
        set_angle(315);
        stylus.forward(15);
    elif(step==10):
        stylus.color("red");
        move_pen(125,-75);
        set_angle(135);
        stylus.forward(335);
        move_pen(-125,-75);
        set_angle(45);
        stylus.forward(335);
        stylus.color("black");
    
    return None;

def draw_frame():
    move_pen(310,-310);
    angle = 90;
    
    stylus.fillcolor("white");
    stylus.begin_fill();
    for square in range(4):
        set_angle(angle)
        stylus.forward(620);
        angle=angle+90;
    stylus.end_fill();
    return None

def draw_blanks(lives):

    spacing = get_space(lives);
    for guesses in range(lives):
        stylus.pendown();
        stylus.forward(45);
        stylus.penup();
        stylus.forward(spacing);
    return None

def get_space(lives):
    spacing = (500-(lives*45))//lives
    return spacing

def analysis(word):
    vowels = ['a','e','i','o','u']
    vowel_count = 0;
    vowel_focus = 0;
    consonant_count = 0;
    latter = 0;
    former = 0;
    for character in word:
        if(character in vowels):
            vowel_count+=1;
            if(character > 'm'):
                vowel_focus+=1;
            else:
                vowel_focus-=1;              
        if(character > 'm'):
            latter = latter+1;
        else:
            former = former+1;
        
    print("Hint:");
    print("There are",vowel_count,"vowels in the word.");
    if(vowel_focus>0):
        print("Vowels are focused on the latter end of the alphabet. (after m)");
    elif(vowel_focus<0):
        print("Vowels are focused on the former end of the alphabet. (before m)");
    else:
        print("Vowels are equally focused on the alphabet.");
    print(former,"characters are on the former end.");
    print(latter,"characters are on the latter end.");
    print("good luck!");
    print("-------------------");    
    return None;

########  Main Part of Program ########
playing = True;
option = 0;
validity = False;
word = [];

file = "";
filePath = "";
fileList = [];

vowels = [chr(97),chr(101),chr(105),chr(111),chr(117)];
consonants = list();

#Building consonants
for alphabet in range(26):
    if(chr(alphabet+97) not in vowels):
        consonants.append(chr(alphabet+97));

print("Welcome to the game of hangman.",end="");
while(playing):
     print("What would you like to do?");
     print("(1) Start Game [default]");
     print("(2) Start Game [Import File]");
     print("(3) Instructions");
     print("(4) Quit");
     
     while(validity==False):
        option = str(input("Enter the number of your choice: "));
        if(option.isnumeric()):
            option = int(option);
            if(option>0 and option<5):
                 validity = True;
                 if(option==1):
                     print("-------------------");
                     print("----- Playing -----");
                     print("-------------------");
                     word = word_builder(vowels,consonants);
                     try:
                        analysis(word);
                        game(word);
                        stylus.mainloop();
                        prompt.mainloop();
                     except:
                        print("-------------------\n"); 
                 elif(option==2):
                     filePath = input("Enter the path of the word list: ");
                     if(".txt" not in filePath[len(filePath)-4:len(filePath)]):
                         filePath = filePath + ".txt";

                     try:
                         file = open(filePath, 'r');

                         for line in file:
                             if(" " not in line.strip()):
                                 fileList.append(line.strip());
                         if(len(fileList)==0):
                             print("Unable to extract words. Make sure there is only one word per line.");
                         else:
                             print("-------------------");
                             print("----- Playing -----");
                             print("-------------------");
                             word = fileList[ran.randint(1,len(fileList))];
                             try:
                                analysis(word);
                                game(word);
                                stylus.mainloop();
                                prompt.mainloop();
                             except:
                                print("-------------------\n");
                     except:
                         print("The file '{}' cannot be read.\n".format(filePath));
                 elif(option==3):
                     print("\n-----Instructions-----");
                     print("The game of hangman has a simple objective.");
                     print("A word is chosen at random, and the player must make an attempt to guess the word.");
                     print("Each guess will be a character. A succesful guess will fill out all blanks of that character.");
                     print("An unsuccessful guess will result in a penalty, where a stickman drawing will be hanged.");
                     print("The objective is to complete the word before the drawing finishes, in which case the player wins.");
                     print("There are two modes in this version of hangman: Defaulted and imported.");
                     print("If playing the default mode, the computer will attempt to simulate a word.");
                     print("The word is randomly constructed; it may not be a real word.");
                     print("Imported mode will attempt to read a file which contains a list of words.");
                     print("---------------------\n");
                 else:
                     playing=False;
                     print("Exiting. Thanks for playing.");                 
            else:
                print("%s is not a recognized menu option."%(option));
        else:
            print("%s is not a recognized menu option."%(option));

     validity=False;
     
         

     
        




