"""Please save the changes that you have done to Google drive also.thank you ."""
#-----------------------------------------------------------------------Legal_Import_statement_section----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk
import random 
from collections import Counter
import mysql.connector
import datetime
import pygame
#***************************************SQL_DETAILS********************************************************************
"""|^_^|change the details according to your system|^_^|!"""
global sql_host,sql_pass,sql_database,sql_user
sql_host="localhost"
sql_pass="M@1708sharma"
sql_database="hangman(player details)"
sql_user="root"
#------------------------------------------------------------------------------Create_main_window------------------------------------------------------------------------------------------------------------------------------------------------------------------------
window=tk.Tk()
window.title("Hangman|welcome|")
# window.iconbitmap("hangman1.png")
window.geometry("800x550")
window.configure(bg="navy")
pygame.mixer.init()
#-----------------------------------------------------------------------------Main_program---------------------------------------------------------------------------------------------------------------------------------------------------------------
class playgame:
     def __init__(s):
          s.score=0
          s.correct = 0
     def main_working(s):
               s.letterGuessed = ''# list for storing the letters guessed by the player 
               s.chances =8
               s.flag = 0
               s.wrong_count=0
               playgame. button_function(s)
     def work(s):               
               s.flag = 0
               s.hint_used=0
               s.guess_string=s.guess.get()
               if (s.chances != 0) and s.flag == 0: #flag is updated when the word is correctly guessed
                           # Validation of the guess 
                           if   s.guess_string.isalpha()==False: 
                                 messagebox.showwarning("Message",'Enter only a LETTER')                                
                           elif len(s.guess_string) > 1:
                                messagebox.showwarning("Message",'Enter only a SINGLE letter')                                
                           elif s.guess_string in s.guessedletter:
                                 messagebox.showinfo("Message",'You have already guessed that letter')                              
                           global label_letterguessed
                           s.guessedletter=s.guessedletter+s.guess_string+","                           
                           label_letterguessed.config(text="Letters Used:"+s.guessedletter)
                           # If letter is guessed correctly
                           if s.guess_string in s.word:
                                    s.k = s.word.count(s.guess_string) #k stores the number of times the guessed letter occurs in the word   
                                    for _ in range(s.k):     
                                             s.letterGuessed += s.guess_string# The guess letter is added as many times as it occurs
                         # Print the word
                           s.x=Counter(s.letterGuessed)
                           s.y=Counter(s.word)
                           wrong=False#to check if wrong guess
                           newword=""
                           for char in s.word:
                               if char in s.letterGuessed and (s.x != s.y):#going rt on track
                                   if char==s.guess_string:
                                        global label__
                                        newword=""
                                        for i in s.word:#required for the word to update on the screen
                                             if char ==i:
                                                newword=newword+char# For printing the empty spaces for letters of the word
                                             elif i in s.letterGuessed and char!=i :
                                                  newword=newword+i
                                             else:
                                                newword=newword+'_ '  
                                        label__.config(text=newword)
                                   s.correct += 1                               
                               # If user has guessed all the letters 
                               elif  s.x == s.y  : # Correct Guessed                            
                                   label__.config(text=s.word) 
                                   global globnum
                                   globnum+=1
                                   s.buton_entry.config(state=DISABLED)                            
                                   label_word=tk.Label(s.mainwindow,text="Congratulation, you saved the hangman|^o^|"+"The word was: "+s.word,fg="blue",bg="orange",font=("Ink Free",16,"bold")).pack()
                                   s.flag = 1
                                   global sql_host,sql_pass,sql_database,sql_user
                                   db_conn=mysql.connector.connect(
                                        host=sql_host,
                                        user=sql_user,
                                        passwd=sql_pass,
                                        database= sql_database)                                  
                                   s.score=s.correct -s.hint_used
                                   global playerid,given_id
                                   global resume,new
                                   c=db_conn.cursor()
                                   q="INSERT INTO  SCORE_TABLE VALUES(%s,%s,%s)"
                                   if resume== True:
                                        data=(given_id,globnum,s.score)
                                   elif new==True:
                                        data=(playerid,globnum,s.score)
                                   c.execute(q,data)
                                   db_conn.commit()
                                   c.close()
                                   db_conn.close()                                   
                                   player_sql_entry.delete_savedgame(s)
                                   playgame.bestscore_function(s)
                                   playgame.button_playagain(s)
                                   break# To break out of the for loop
                                   return 
                               else :
                                   wrong=True       
                           if s.guess_string not in s.word  and wrong== True:
                                s.chances = s.chances -1
                                s.wrong_count+=1      
                                if s.wrong_count==1:
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                elif s.wrong_count==2 :
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                                     global hint1
                                     label_hint=tk.Label(s.mainwindow,text=hint1,fg="blue",bg="orange",font=("Ink Free",20,"bold"))
                                     label_hint.pack()
                                     s.hint_used=1
                                elif s.wrong_count==3 :
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,200,100,fill="orange",width=3)
                                elif s.wrong_count==4 :
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,200,100,fill="orange",width=3)
                                     s.canvas_main.create_line(200,100,200,175,fill="orange",width=3)
                                elif s.wrong_count==5 :
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,200,100,fill="orange",width=3)
                                     s.canvas_main.create_line(200,100,200,175,fill="orange",width=3)
                                     s.canvas_main.create_oval(175,175,225,225,width=3,fill="orange")#head
                                elif s.wrong_count==6 :
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,200,100,fill="orange",width=3)
                                     s.canvas_main.create_line(200,100,200,175,fill="orange",width=3)
                                     s.canvas_main.create_oval(175,175,225,225,width=3,fill="orange")#head
                                     s.canvas_main.create_line(200,225,200,275,fill="orange",width=3)#body
                                     s.canvas_main.create_line(200,225,150,175,fill="orange",width=3)#hand1
                                     global hint2
                                     label_hint2=tk.Label(s.mainwindow,text=hint2,fg="blue",bg="orange",font=("Ink Free",20,"bold"))
                                     label_hint2.pack()
                                     s.hint_used=2
                                elif s.wrong_count==7 :
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,200,100,fill="orange",width=3)
                                     s.canvas_main.create_line(200,100,200,175,fill="orange",width=3)
                                     s.canvas_main.create_oval(175,175,225,225,width=3,fill="orange")#head
                                     s.canvas_main.create_line(200,225,200,275,fill="orange",width=3)#body
                                     s.canvas_main.create_line(200,225,150,175,fill="orange",width=3)#hand
                                     s.canvas_main.create_line(200,225,250,175,fill="orange",width=3)
                                elif s.wrong_count==8 :
                                     s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                                     s.canvas_main.create_line(100,100,200,100,fill="orange",width=3)
                                     s.canvas_main.create_line(200,100,200,175,fill="orange",width=3)
                                     s.canvas_main.create_oval(175,175,225,225,width=3,fill="orange")
                                     s.canvas_main.create_line(200,225,200,275,fill="orange",width=3)
                                     s.canvas_main.create_line(200,225,150,175,fill="orange",width=3)#hand
                                     s.canvas_main.create_line(200,225,250,175,fill="orange",width=3)#hand
                                     s.canvas_main.create_line(200,275,250,290,fill="orange",width=3)#leg
                                     s.canvas_main.create_line(200,275,150,290,fill="orange",width=3)#leg                                  
                           if s.chances <= 0 and (s.x != s.y):
                               globnum+=1
                               label_lost=tk.Label(s.mainwindow,text="You Lost.Better Luck Next Time!",fg="blue",bg="orange",font=("Freestyle Script",16,"bold")).pack()
                               label_word=tk.Label(s.mainwindow,text=s.word+" was the word.",fg="blue",bg="orange",font=("small fonts",16,"bold")).pack()
                               s.buton_entry.config(state=DISABLED)
                               playgame.button_playagain(s)
                               s.canvas_main.create_line(100,300,300,300,fill="orange",width=3)
                               s.canvas_main.create_line(100,100,100,300,fill="orange",width=3)
                               s.canvas_main.create_line(100,100,200,100,fill="orange",width=3)
                               s.canvas_main.create_line(200,100,200,175,fill="orange",width=3)
                               s.canvas_main.create_oval(175,175,225,225,fill="orange",width=2)#head
                               s.canvas_main.create_line(200,225,200,275,fill="orange",width=3)#body
                               s.canvas_main.create_line(200,225,150,175,fill="orange",width=3)#hand
                               s.canvas_main.create_line(200,225,250,175,fill="orange",width=3)#hand
                               s.canvas_main.create_line(200,275,250,290,fill="orange",width=3)#leg
                               s.canvas_main.create_line(200,275,150,290,fill="orange",width=3)#leg
                               player_sql_entry.delete_savedgame(s)                               
                               return                               
     def bestscore_function(s):#the best score function to store the former.
          global sql_host,sql_pass,sql_database,sql_user
          db_conn=mysql.connector.connect(
                                        host=sql_host,
                                        user=sql_user,
                                        passwd=sql_pass,
                                        database=sql_database)                                   
          global resume,new,playerid,given_id
          c=db_conn.cursor(buffered=True)
          best_datetime=datetime.datetime.now()
          best_date=datetime.date(best_datetime.year,best_datetime.month,best_datetime.day)
          if resume==True:
                                            data=(given_id,)
                                            q="SELECT BESTSCORE FROM RECORD_TABLE WHERE PLAYERID=(%s)"
                                            c.execute(q,data)
                                            bestscore=c.fetchone( )                                            
                                            if s.score>bestscore[0]:
                                                 q="UPDATE RECORD_TABLE  SET BESTSCORE=%s,SCOREDATE=%s WHERE  PLAYERID=%s"
                                                 data=(s.score,best_date,given_id)
          elif new==True:
                                            data=(playerid,)    
                                            q="SELECT BESTSCORE FROM RECORD_TABLE WHERE PLAYERID=(%s)"
                                            c.execute(q,data)
                                            bestscore=c.fetchone( )                                            
                                            if s.score>bestscore[0]:
                                                 q="UPDATE RECORD_TABLE  SET BESTSCORE=%s,SCOREDATE=%s WHERE  PLAYERID=%s"
                                                 data=(s.score,best_date,playerid)
          c.execute(q,data)
          db_conn.commit()
          c.close()
          db_conn.close()                           
     def button_function(s):
          s.guess_variable=tk.StringVar()
          s.guess= ttk.Entry(s.mainwindow,textvariable=s.guess_variable,width=10,justify="center")
          s.guess.pack()
          s.buton_entry=tk.Button(s.mainwindow,text="Enter",command= lambda:playgame.work(s),fg="navy",bg="orange",font=("small fonts",16,"bold"),activeforeground="orange",activebackground="navy")
          s.buton_entry.pack()
     def button_playagain(s):
          if globnum==1:
               buton_again=tk.Button(s.mainwindow,text="Next Round!",command= lambda:playgame.level(s,1),fg="blue",bg="orange",font=("Freestyle Script",16,"bold"),activeforeground="blue",activebackground="blue").pack()
          elif globnum==2 or globnum==3:
               buton_again=tk.Button(s.mainwindow,text="Next Round!",command= lambda:playgame.level(s,2),fg="blue",bg="orange",font=("Freestyle Script",16,"bold"),activeforeground="blue",activebackground="blue").pack()
     def play(s,num_of_letters):
          s.mainwindow=tk.Tk()
          s.mainwindow.title("Hangman|Play area|")
          s.mainwindow.geometry("700x700")
          s.mainwindow.configure(bg="orange")
          label_hangman=tk.Label(s.mainwindow,text="HANGMAN",font=("small fonts",50),fg="navy",bg="orange").pack()
          global sql_host,sql_pass,sql_database,sql_user
          db_conn=mysql.connector.connect(
               host=sql_host,
               user=sql_user,
               passwd=sql_pass,
               database=sql_database)
          c=db_conn.cursor()
          q="SELECT * FROM HINT_TABLE WHERE LEVELNUM=(%s)"  
          data=(num_of_letters,)
          c.execute(q,data)
          rows=c.fetchmany(60)
          n1=random.randint(1,len(rows))#can leave the empty it reads one record (doubt!)
          global saved
          global globalword
          if saved==True:
               s.word=globalword#varialbe to have the saved word
          else:
               try:
                    s.word=rows[n1][1]
               except:
                    messagebox.showwarning("Message",'|#_@|Sorry our hangman ran off . Please try again.|@_#|')
          #The main canvas for mr.hangman
          s.canvas_main=tk.Canvas(s.mainwindow,width=350,height=350,background="navy")
          s.canvas_main.pack()#s.canvas_main.create_line(x1,y1,x2,y2,fill="colour")
          global hint1,hint2
          hint1=rows[n1][2]#basic hint to tell about the word type
          hint2=rows[n1][3]#a more related hint 
          global label__,label_letterguessed      
          blankword=""
          s.guessedletter=""
          for i in s.word: 
             blankword=blankword+'_ ' # For printing the empty spaces for letters of the word 
          label__=tk.Label(s.mainwindow,text=blankword,fg="blue",bg="orange",font=("Freestyle Script",25))
          label__.pack()
          label_letterguessed=tk.Label(s.mainwindow,text="Guessed Letters: ",fg="blue",bg="orange",font=("Freestyle Script",20))
          label_letterguessed.pack()
          button_save= Button(s.mainwindow, text = "Save!",command=lambda:player_sql_entry.save_play(s,num_of_letters,s.word),fg="navy",bg="orange",font=("small fonts",16,"bold"),activeforeground="orange",activebackground="navy")
          button_save.place(relx = 1, x =-2, y = 2, anchor = NE) 
          playgame.main_working(s)
          s.mainwindow.mainloop()
     def level(s,level_num):
           if level_num==1:
                     playgame.play(s,1)
           elif level_num==2:
                     playgame.play(s,2)                    
#---------------------------------------------------------------------------Connecting_to_MYSQL---------------------------------------------------------------------------------------------------------------------------------------------------- 
"""|^_^|main sql conections ahead|^_^|!"""
class player_sql_entry :
     def __init__(s):
          s.rid=100
     def create_player(s):
          global playername_variable, playerage_variable,playergender_variable,button_submit,new
          new=True
          button_submit.config(state=DISABLED)
          name=playername_variable.get()
          age=playerage_variable.get()
          gender=playergender_variable.get()
          p=playgame()
          global sql_host,sql_pass,sql_database,sql_user
          db_conn=mysql.connector.connect(
               host=sql_host,
               user=sql_user,
               passwd=sql_pass,
               database= sql_database)
          s.num= random.randint(10,900)
          global playerid
          playerid=100+s.num+int(age)
          c=db_conn.cursor()
          q="INSERT INTO  PLAYER_TABLE VALUES(%s,%s,%s,%s)"
          data=(playerid,name,age,gender)
          c.execute(q,data)
          db_conn.commit()
          c.close()
          db_conn.close()
          db_conn=mysql.connector.connect(
                                        host=sql_host,
                                        user=sql_user,
                                        passwd=sql_pass,
                                        database= sql_database)                                
          c=db_conn.cursor()
          best_datetime=datetime.datetime.now()
          best_date=datetime.date(best_datetime.year,best_datetime.month,best_datetime.day)
          q="INSERT INTO RECORD_TABLE VALUES(%s,%s,%s)"
          data=(playerid,0,best_date)
          c.execute(q,data)
          db_conn.commit()
          c.close()
          db_conn.close() 
          s.create_new_window2=tk.Tk()
          s.create_new_window2.title("Hangman|Create Player|")
          s.create_new_window2.geometry("300x300")
          s.create_new_window2.configure(bg="orange")
          label_id=tk.Label(s.create_new_window2,text="YourID:"+str(playerid),font=("small fonts",17),fg="navy",bg="orange").pack()
          label_rem=tk.Label(s.create_new_window2,text="Please remember your ID!",font=("small fonts",12),fg="navy",bg="orange").pack()
          button_play=Button(s.create_new_window2,text="Play",command=lambda: p.level(1),bg="navy",fg="orange")
          button_play.pack()
          s.create_new_window2.mainloop()
     def resume_player(s):
          p=playgame()
          global playerid_checkvariable,playername_checkvariable
          global given_id,resume
          resume=True
          given_id=playerid_checkvariable.get()
          given_name=playername_checkvariable.get()
          global sql_host,sql_pass,sql_database,sql_user
          db_conn=mysql.connector.connect(
               host=sql_host,
               user=sql_user,
               passwd=sql_pass,
               database= sql_database)
          c1=db_conn.cursor()
          q1="SELECT PLAYERNAME FROM  PLAYER_TABLE  WHERE PLAYERID = %s ;"
          data=(given_id,)
          c1.execute(q1,data)
          row=c1.fetchone()
          db_conn.commit()
          c1.close()
          db_conn.close()
          if row!=None:
             if row[0]!= None  and  row[0] == given_name:
                    global button_continue
                    button_continue.config(state=DISABLED)
                    s.create_new_window2=tk.Tk()
                    s.create_new_window2.title("Hangman|Saved Player|")
                    s.create_new_window2.geometry("200x150")
                    s.create_new_window2.configure(bg="orange")
                    label_hangman=tk.Label(s.create_new_window2,text="HANGMAN",font=("small fonts",29),fg="navy",bg="orange").pack()
                    label_welcome=tk.Label(s.create_new_window2,text="Welcome "+given_name+" !",font=("small fonts",17),fg="navy",bg="orange").pack()
                    button_play=Button(s.create_new_window2,text="Play",command=lambda: p.level(1),fg="navy",bg="orange").pack()
                    s.create_new_window2.mainloop()
             else:
               s.create_new_window2=tk.Tk()
               s.create_new_window2.title("Hangman|Create Player|")
               s.create_new_window2.geometry("400x150")
               s.create_new_window2.configure(bg="orange")
               label_hangman=tk.Label(s.create_new_window2,text="HANGMAN",font=("small fonts",50),fg="navy",bg="orange").pack()
               label_welcome=tk.Label(s.create_new_window2,text="Sorry wrong username !",font=("small fonts",17),fg="navy",bg="orange").pack()
               s.create_new_window2.mainloop()
          else:
               messagebox.showwarning("Message",'|#_@|You have enter a wrong ID or username|@_#|')
     def saved_game(s):
          p=playgame()
          global playerid_checkvariable,playername_checkvariable,given_id,resume        
          resume=True
          given_id=playerid_checkvariable.get()
          given_name=playername_checkvariable.get()
          global sql_host,sql_pass,sql_database,sql_user
          db_conn=mysql.connector.connect(
               host=sql_host,
               user=sql_user,
               passwd=sql_pass,
               database= sql_database)
          c1=db_conn.cursor()
          q1="SELECT PLAYERNAME,SAVED_WORD,LEVELPLAYED FROM  SAVED_GAME  WHERE PLAYERID = %s ;"
          data=(given_id,)
          c1.execute(q1,data)
          row=c1.fetchone()
          db_conn.commit()
          c1.close()
          db_conn.close()          
          if row!=None:
             global globalword,saved
             globalword=row[1]
             saved=True
             if row!= None  and  row[0] == given_name:
                    global button_continue
                    button_continue.config(state=DISABLED)
                    s.create_new_window2=tk.Tk()
                    s.create_new_window2.title("Hangman|Create Player|")
                    s.create_new_window2.geometry("200x150")
                    s.create_new_window2.configure(bg="orange")
                    label_hangman=tk.Label(s.create_new_window2,text="HANGMAN",font=("small fonts",29),fg="navy",bg="orange").pack()
                    label_welcome=tk.Label(s.create_new_window2,text="Welcome "+given_name+" !",font=("small fonts",17),fg="navy",bg="orange").pack()
                    button_play=Button(s.create_new_window2,text="Play",command=lambda: p.level(1),fg="navy",bg="orange").pack()
                    s.create_new_window2.mainloop()
             else:
               s.create_new_window2=tk.Tk()
               s.create_new_window2.title("Hangman|Create Player|")
               s.create_new_window2.geometry("400x150")
               s.create_new_window2.configure(bg="orange")
               label_hangman=tk.Label(s.create_new_window2,text="HANGMAN",font=("small fonts",50),fg="navy",bg="orange").pack()
               label_welcome=tk.Label(s.create_new_window2,text="Sorry wrong username !",font=("small fonts",17),fg="navy",bg="orange").pack()
               s.create_new_window2.mainloop()
          else:
               messagebox.showwarning("Message",'|#_@|You have enter a wrong ID or username|OR|You donot have a saved game|@_#|')
     def delete_savedgame(s):
          global saved
          global given_id,resume,new,playerid
          if saved==True:
                                        db_conn=mysql.connector.connect(
                                             host=sql_host,
                                             user=sql_user,
                                             passwd=sql_pass,
                                             database= sql_database)
                                        c=db_conn.cursor()
                                        q="DELETE SAVED_GAME WHERE PALYERID=(%s)"
                                        if resume== True:
                                             data=(given_id,)
                                        elif new==True:
                                             data=(playerid,)
                                        c.execute(q,data)
                                        db_conn.commit()
                                        c.close()
                                        db_conn.close()
                                        saved=False
     def save_play(s,level,word):
          global sql_host,sql_pass,sql_database,sql_user
          db_conn=mysql.connector.connect(
               host=sql_host,
               user=sql_user,
               passwd=sql_pass,
               database= sql_database)
          c1=db_conn.cursor()
          q1="INSERT INTO SAVED_GAME  VALUES(%s,%s,%s,%s);"
          global playerid_checkvariable,playername_checkvariable
          global resume,new
          global globnum,playerid,given_id
          if resume==True:
               given_id=playerid_checkvariable.get()
               given_name=playername_checkvariable.get()
               data=(given_id,given_name,word,level)
          elif new==True:
               global playerid,playername_variable
               given_id=playerid
               data=(playerid,given_name,word,level)
          c1.execute(q1,data)
          db_conn.commit()
          c1.close()
          db_conn.close()
          
#---------------------------------------------------------------------------Creating_New_Player|OR|Resume_Old_Game------------------------------------------------------------------------------------------------------------------------------------------------------------ 
"""|^_^|Entry code of game.kind of like a login screen for the user|@_@|!"""
class player_entry :          
     def __init__(s):
          s.something=0
     def create_new_player(s):
          global b_createplayer,b_resume,b_savedplay
          b_createplayer.config(state=DISABLED)
          b_resume.config(state=DISABLED)
          b_savedplay.config(state=DISABLED)
          global new
          new=True
          s.create_new_window=tk.Tk()
          s.create_new_window.title("Hangman|Create Player|")
          s.create_new_window.geometry("400x150")
          s.create_new_window.configure(bg="navy")
          global playername_variable, playerage_variable,playergender_variable
          playername_variable=tk.StringVar(s.create_new_window)
          playerage_variable=tk.IntVar(s.create_new_window)
          playergender_variable=tk.StringVar(s.create_new_window)          
          s.label_name=tk.Label(s.create_new_window,text="Name:",font=("small fonts",17),fg="orange",bg="navy").grid(column=1,row=1)
          s.player_name= tk.Entry(s.create_new_window,textvariable=playername_variable,width=17,justify="center",font=("small fonts",17),bg="orange",fg="navy")
          s.player_name.grid(column=2,row=1)
          s.label_age=tk.Label(s.create_new_window,text="Age:",font=("small fonts",17),fg="orange",bg="navy").grid(column=1,row=2)
          s.player_age= tk.Entry(s.create_new_window,textvariable=playerage_variable,width=17,justify="center",font=("small fonts",17),bg="orange",fg="navy")
          s.player_age.grid(column=2,row=2)
          s.label_gender=tk.Label(s.create_new_window,text="Gender:",font=("small fonts",17),fg="orange",bg="navy").grid(column=1,row=3)
          s.player_gender= tk.Entry(s.create_new_window,textvariable=playergender_variable,width=17,justify="center",font=("small fonts",17),bg="orange",fg="navy")
          s.player_gender.grid(column=2,row=3)
          global button_submit
          button_submit=Button(s.create_new_window,text="Submit",command=lambda: player_sql_entry.create_player(s),bg="navy",fg="orange")
          button_submit.grid(column=2,row=4)
          s.create_new_window.mainloop()
     def resume_old_player(s):
          global b_createplayer,b_resume,b_savedplay
          b_createplayer.config(state=DISABLED)
          b_resume.config(state=DISABLED)
          b_savedplay.config(state=DISABLED)
          global resume
          resume=True
          p=playgame()
          s.create_new_window3=tk.Tk()
          s.create_new_window3.title("Hangman|Create Player|")
          s.create_new_window3.geometry("300x150")
          s.create_new_window3.configure(bg="orange")
          global playerid_checkvariable,playername_checkvariable
          playerid_checkvariable=tk.IntVar(s.create_new_window3)
          playername_checkvariable=tk.StringVar(s.create_new_window3)
          s.label_age=tk.Label(s.create_new_window3,text="Your ID:",font=("small fonts",17),fg="navy",bg="orange").grid(column=1,row=2)
          s.playerid_check= tk.Entry(s.create_new_window3,textvariable=playerid_checkvariable,font=("small fonts",13),bg="navy",fg="orange",width=17,justify="center")
          s.playerid_check.grid(column=2,row=2)
          s.label_gender=tk.Label(s.create_new_window3,text="Your name:",font=("small fonts",17),fg="navy",bg="orange").grid(column=1,row=3)
          s.playername_check= tk.Entry(s.create_new_window3,textvariable=playername_checkvariable,font=("small fonts",15),bg="navy",fg="orange",width=17,justify="center")
          s.playername_check.grid(column=2,row=3)
          global button_continue
          button_continue=Button(s.create_new_window3,text="Continue",command=lambda: player_sql_entry.resume_player(s),font=("small fonts",15),bg="orange",fg="navy",activebackground="navy",activeforeground="orange")
          button_continue.grid(column=2,row=4)
          s.create_new_window3.mainloop()
     def saved_play(s):
          global b_createplayer,b_resume,b_savedplay
          b_createplayer.config(state=DISABLED)
          b_resume.config(state=DISABLED)
          b_savedplay.config(state=DISABLED)
          global resume
          resume=True
          p=playgame()
          s.create_new_window3=tk.Tk()
          s.create_new_window3.title("Hangman|Create Player|")
          s.create_new_window3.geometry("300x150")
          s.create_new_window3.configure(bg="orange")
          global playerid_checkvariable,playername_checkvariable
          playerid_checkvariable=tk.IntVar(s.create_new_window3)
          playername_checkvariable=tk.StringVar(s.create_new_window3)
          s.label_age=tk.Label(s.create_new_window3,text="Your ID:",font=("small fonts",17),fg="navy",bg="orange").grid(column=1,row=2)
          s.playerid_check= tk.Entry(s.create_new_window3,textvariable=playerid_checkvariable,font=("small fonts",13),bg="navy",fg="orange",width=17,justify="center")
          s.playerid_check.grid(column=2,row=2)
          s.label_gender=tk.Label(s.create_new_window3,text="Your name:",font=("small fonts",17),fg="navy",bg="orange").grid(column=1,row=3)
          s.playername_check= tk.Entry(s.create_new_window3,textvariable=playername_checkvariable,font=("small fonts",15),bg="navy",fg="orange",width=17,justify="center")
          s.playername_check.grid(column=2,row=3)
          global button_continue
          button_continue=Button(s.create_new_window3,text="Continue",command=lambda: player_sql_entry.saved_game(s),font=("small fonts",15),bg="orange",fg="navy",activebackground="navy",activeforeground="orange")
          button_continue.grid(column=2,row=4)
          s.create_new_window3.mainloop()     
#------------------------------------------------------------------------------Front_Page_code----------------------------------------------------------------------------------------------------------------------------------------------------------------------
logo_1=tk.PhotoImage(file="C:\Sanskar\Python Works\drive-download-20240330T055410Z-001\hangman1.png")
logo_label=ttk.Label(window ,image=logo_1,border=0).pack()
p=player_entry()
global b_createplayer,b_resume,b_savedplay
b_createplayer=Button(window,text="Create New Player",command=lambda: p.create_new_player(),bg="navy",fg="orange",font=("small fonts",20),activeforeground="navy",activebackground="orange",border=0)
b_createplayer.pack()
b_resume=Button(window,text="Countinue The Journey",command=lambda: p.resume_old_player(),font=("small fonts",20),bg="navy",fg="orange",activeforeground="navy",activebackground="orange",border=0)
b_resume.pack()
b_savedplay=Button(window,text="Countinue Playing",command=lambda: p.saved_play(),font=("small fonts",20),bg="navy",fg="orange",activeforeground="navy",activebackground="orange",border=0)
b_savedplay.pack()
global globnum,resume,new,saved#this global var are used to check for old/new player
globnum=0
resume=False
new=False
saved=False
#quotes games
quotes=["Games are the most elevated form of investigation. --Albert Einstein",
        "The game itself is bigger than the winning.--Dejan Stojanovic",
        "Games lubricate the body and mind.--Benjamin Franklin",
        "We do not stop playing because we grow old. \nWe grow old because we stop playing.-- Benjamin Franklin",
        "Life is more fun if you play games.--Roald Dahl"]
no_quote=random.randint(0,4)
pygame.mixer.music.load("C:\Sanskar\Python Works\drive-download-20240330T055410Z-001\Tobu - Hope [NCS Release].mp3")
pygame.mixer.music.play(loops=2)
label_quote=tk.Label(window,text=quotes[no_quote],font=("Harrington",20),fg="orange",bg="navy").pack()
label_thank=tk.Label(window,text="|^_^|Hope You Have A Great Day|^_^|.",font=("small fonts",25),fg="orange",bg="navy").pack()
label_made=tk.Label(window,text="Made by : \n Sanskar Sharma ",font=("small fonts",25),bg="navy",fg="orange").pack()
#---------------------------------------------------------------------------Mainloop_ahead---------------------------------------------------------------------------------------------------------------------------------------------------------------          
window.mainloop()
#-----------------------------------------------------------------------------Dead_End--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------