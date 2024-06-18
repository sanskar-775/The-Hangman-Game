
"""Please save the changes that you have done to Google drive also. before saving any changes contact me.thank you ."""
#-----------------------------------------------------------------------Import_statement_section----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
import random 
from collections import Counter
#------------------------------------------------------------------------------Create_window--------------------------------------------------------------------------------------------------------------------------------------------------------------
window=tk.Tk()
window.title("Hangman|welcome|")
window.iconbitmap("hangmanicon3.png")
window.geometry("600x500")
window.configure(bg="orange")
#-----------------------------------------------------------------------------Main_program---------------------------------------------------------------------------------------------------------------------------------------------------------------

class playgame:
     def __init__(s):
          s.x=0  
                               
     def main_working(s):
               
               # list for storing the letters guessed by the player
               s.letterGuessed = ''                 
               s.chances = len(s.word) + 2
               s.correct = 0
               s.flag = 0
               
               #s.guess_string1=s.guess_string+s.guess_string
               playgame. button_function(s)
     def work(s):
               s.a=0
               s.guess_string=s.guess.get()
               if (s.chances != 0) and s.flag == 0: #flag is updated when the word is correctly guessed
                           s.chances = s.chances -1
                           # Validation of the guess 
                           if   s.guess_string.isalpha()==False: 
                                 messagebox.showwarning("Message",'Enter only a LETTER')                                
                           elif len(s.guess_string) > 1:
                                messagebox.showwarning("Message",'Enter only a SINGLE letter')                                
                           elif s.guess_string in s.letterGuessed:
                                 messagebox.showwarning("Message",'You have already guessed that letter')                              
                           # If letter is guessed correctly
                           if s.guess_string in s.word:
                                    s.k = s.word.count(s.guess_string) #k stores the number of times the guessed letter occurs in the word   
                                    for _ in range(s.k):     
                                             s.letterGuessed += s.guess_string# The guess letter is added as many times as it occurs
                         # Print the word
                           s.x=Counter(s.letterGuessed)
                           s.y=Counter(s.word)
                           wrong=False#to check if wrong guess
                           #Sl={}
                           for char in s.word:
                               if char in s.letterGuessed and (s.x != s.y):
                                   if char==s.guess_string:
                                        label_ch=tk.Label(s.mainwindow,text=" ✨Bravo correct guess|*o*|😃!"+char,fg="white",bg="orange",font=("Ink Free",16,"bold")).pack()
                                   s.correct += 1                               
                               # If user has guessed all the letters 
                               elif  s.x == s.y  : # Once the correct word is guessed fully,  
                                                                # the game ends, even if chances remain 
                                   label_word=tk.Label(s.mainwindow,text="The word is: "+s.word,fg="white",bg="orange",font=("Ink Free",16,"bold")).pack()
                                   s.flag = 1                     
                                   label_congo=tk.Label(s.mainwindow,text="✨🎊Congratulation🎊✨, You won|^o^|😊!",fg="white",bg="orange",font=("Ink Free",16,"bold")).pack()
                                   playgame.button_playagain(s)
                                   break# To break out of the for loop
                                   return 
                               else :
                                   wrong=True       
                           if s.guess_string not in s.word  and wrong== True:
                                label_wrong=tk.Label(s.mainwindow,text="👎Wrong guess 😵!"+s.guess_string,fg="white",bg="orange",font=("Ink Free",16,"bold")).pack()
                           if s.chances <= 0 and (s.x != s.y):
                               label_lost=tk.Label(s.mainwindow,text="You Lost😥.Better Luck Next Time!",fg="white",bg="orange",font=("Freestyle Script",16,"bold")).pack()
                               label_word=tk.Label(s.mainwindow,text="P.S:"+s.word+" was the word.",fg="white",bg="orange",font=("Pristina",16,"bold")).pack()
                               playgame.button_playagain(s)
                               return
                               
                               
     def button_function(s):
          s.guess_variable=tk.StringVar()
          s.guess= ttk.Entry(s.mainwindow,textvariable=s.guess_variable,width=10,justify="center")
          s.guess.pack()
          buton_entry=tk.Button(s.mainwindow,text="Enter",command= lambda:playgame.work(s),fg="white",bg="orange",font=("Freestyle Script",16,"bold"),activeforeground="white",activebackground="blue").pack()
     def button_playagain(s):
          buton_again=tk.Button(s.mainwindow,text="Play again!",command= lambda:playgame.play(s),fg="white",bg="orange",font=("Freestyle Script",16,"bold"),activeforeground="white",activebackground="blue").pack()
     def play(s):
          s.mainwindow=tk.Tk()
          s.mainwindow.title("Hangman|Play area|")
          s.mainwindow.geometry("600x700")
          s.mainwindow.configure(bg="orange")
          s.someWords = '''apple banana mango strawberry  orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
          s.someWords = s.someWords.split(' ') 
          # randomly choose a secret word from our "someWords" LIST.
          s.word= random.choice(s.someWords)
          #canvas
          canvas_main=tk.Canvas(s.mainwindow,width=400,height=200,background="white")
          canvas_main.pack()
          if __name__ == '__main__': 
                    hint='Guess the word! HINT: word is a name of a fruit'
                    label_hint=tk.Label(s.mainwindow,text=hint,fg="white",bg="orange",font=("Freestyle Script",20,"bold")).pack()
          s.blankspaces=""
          for i in s.word: 
             s.blankspaces=s.blankspaces+'_ ' # For printing the empty spaces for letters of the word 
          label__=tk.Label(s.mainwindow,text=s.blankspaces,fg="white",bg="orange",font=("Freestyle Script",14)).pack()
          playgame.main_working(s)
          s.mainwindow.mainloop()                                       
#---------------------------------------------------------------------------Connecting_to_MYSQL---------------------------------------------------------------------------------------------------------------------------------------------------- 
"""change th edetails according to your system|^_^|!"""
class sql :
     def __init__(self):
          self.a=0
     def create_player():
     def update_player():
             
#------------------------------------------------------------------------------Front_Page_code----------------------------------------------------------------------------------------------------------------------------------------------------------------------
label_hangman=tk.Label(window,text="HANGMAN",font=("Snap ITC",30),bg="orange").pack()
logo_1=tk.PhotoImage(file="hangman1.png")
logo_label=ttk.Label(window ,image=logo_1).pack()
p=playgame()
playername_variable=tk.StringVar()
player_name= ttk.Entry(s.mainwindow,textvariable=playername_variable,width=10,justify="center")
player_name.pack()
b_1=Button(window,text="Start",command=lambda: p.play(),bg="orange",fg="black").pack()
label_thank=tk.Label(window,text="|^o^|Thank You for Using the programe|^o^|.",font=("Freestyle Script",19),fg="black",bg="orange").pack()
label_thank=tk.Label(window,text="Hope You Have A Great Day.😊",font=("Freestyle Script",18),fg="black",bg="orange").pack()
label_made=tk.Label(window,text="Made by : Sanskar Sharma and Devansh Tal@n",font=("small fonts",17),fg="black",bg="orange").pack()
#---------------------------------------------------------------------------Calling_the_functions----------------------------------------------------------------------------------------------------------------------------------------------------          
window.mainloop()
#-----------------------------------------------------------------------------Dead_End-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
