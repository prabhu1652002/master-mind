import random
import sys
import winsound
import tkinter as tk
from tkinter import *
import time
from time import sleep
import tkinter as tk
from tkinter import messagebox as mb

  


def game():          
  def easy():
      a=[1,2,3,4,5,6,7,8]      # a is set of pegs
      result=["b","b","b","b"]
      return a,result
  def medium():
      a=[1,2,3,4,5,6,7,8,9,10]
      result=["b","b","b","b"]
      return a,result
  def hard():
      a=[1,2,3,4,5,6,7,8,9,10,11,12]
      result=["b","b","b","b","b"]
      return a,result
  def is_unique_value(move,peg,user_input):
      for i in range (0,move-1):
          if user_input[i]==int(peg):
              return False
      return True   
  def progress():
      if turn==1:
          print("Values you have entered in current turn",user_input)
      else:    
       print("OUTPUT DATA")
       for i in range(turn-1):
          print(i+1,"-",r1[i],r2[i],"\n")
       print("Values you have entered in current turn",user_input)    

  def results():
    mb.showinfo("Time(s)",int(e-s))
    mb.showinfo("Rounds",turn-1)
    print("Time taken (seconds): ",int(e-s))
    print("No of rounds: ",turn-1)

  def close_window2 (): 
	
      winsound.PlaySound(None, winsound.SND_ASYNC)    
      window2.destroy()

  print(" ===========================MASTERMIND===========================")
  for i in range(8):
    print("\t\t\t\t.")
    sleep(0.75)

  print("                       ***LEVEL SELECT***")      
  while True:
      
      print("""Enter 
                e for easy mode
                m for intermediate mode  
                h for  hard mode""")
      level=input("Enter difficulty level: ")
      if level.isalpha():
          if level.lower()=="e":
              a,result=easy()
              break
          elif level.lower()=="m":
              a,result=medium()
              break
          elif level.lower()=="h":
              a,result=hard()
              break
          else:
              print("Please enter a correct value \n")

  #STARTING TIMER
  s=time.time()
  print("Timer started!")

              
  hint_set=list()   
   # Number of colours

  secret_code=random.sample(a,len(result))  #sets the code
 # print(secret_code)   #SOLUTION

  user_input=list() #list to store values entered by user
  turn=1

  r1=list()
  r2=list()


  while result!=hint_set:
      
    print("TURN",turn,)
    move=1
  #input

    hint_set.clear()
    user_input.clear()
    while move<=len(result):
       
      peg=input("Enter number"+str(move)+'\t')
      
      
      if peg.isnumeric()==True:
          if move==1:
              if int(peg) in a:
                  user_input.append(int(peg))
              else:
                  print('Enter value within range',a)
                  continue
        	             
                                 
	    	            
          
          elif int(peg) in a:
              if is_unique_value(move,peg,user_input)==True:
                  user_input.append(int(peg))
              else:
                  print("Enter unique values")
                  print("Values that you have already entered",user_input)
                  continue
          
              
              
          
              
          else:
              
              print("Enter value  within the range",a)
              continue
     
      else:
          
          if peg.lower()=="q": # QUIT
            root= tk.Tk()
            root.title("CONFIRMATION")
            

            canvas1 = tk.Canvas(root, width = 300, height = 180,bg="#A7B0D6")
            
            canvas1.pack()

            def ExitApplication():  #confirmation message to exit program
                MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the game',icon = 'warning')
                if MsgBox == 'yes':
                   root.destroy()
                   sys.exit()
                else:
                    root.destroy()
            button1 = tk.Button (root, text='QUIT GAME',command=ExitApplication,bg='brown',fg='white')
            canvas1.create_window(150, 70, window=button1)
            button2 = tk.Button (root, text='HOW TO PLAY',command=rules,bg='grey',fg='white')
            canvas1.create_window(150, 100, window=button2)
  
            root.mainloop()
        

          elif peg.lower()=="u": #UNDO
                  if move==1:
                      print("You cannot use undo option in the first entry")
                      continue
                  else:
                      move=move-1
                      del user_input[move-1]
                      continue
          elif peg.lower()=="p":
              progress()
              continue    
              
          
          print('Enter value within range',a)
          continue
      move=move+1
    print("\n")  
    
   # print(user_input)
  #Output
    turn+=1
    
    task=""
    for k in user_input:
      for j in secret_code:
          if secret_code.ind(j)==user_input.ind(k) and j==k:
              hint_set.append("b")
              task="complete"
              break
          elif j==k:
              hint_set.append("w")
              task="complete"
              break
      if task!="complete":
          hint_set.append("n")
      task=""
    random.shuffle(hint_set)  #Comment this line to reduce difficulty
    #print(hint_set)
    r1.append(tuple(user_input))
    r2.append(tuple(hint_set))
    print("OUTPUT DATA")
    for i in range(turn-1):
        print(i+1,"-",r1[i],r2[i],"\n")
  
  winsound.PlaySound(None, winsound.SND_ASYNC) 
  winsound.PlaySound("test3.wav", winsound.SND_ASYNC + winsound.SND_LOOP| winsound.SND_ALIAS ) 
  e=time.time()
  print("YOU WON.")
  


  print("\n\n\n\n")
  print("Processing result")
  for i in range (6):
    print("\t.")
    sleep(1)
  print("      Wait")
  for i in range(6):
    print("\t.")
    sleep(0.5)
  print("   Almost done!")
  for i in range(6):
    print("\t.")
    sleep(0.2)

  print("   Completed!")


  window2=tk.Tk()
  window2.geometry('200x200')
  window2.title("GAME REPORT")
  label1=tk.Label(window2,font='Helvetica 15', text="RESULT").pack()


  bt4=tk.Button(window2,text="Click Here",width=20,height=2,command=results).pack(side=tk.TOP)


  bt5=tk.Button(window2,text="Close",width=20,height=2,command=close_window2).pack(side=tk.TOP)

def rules():
      mb.showinfo("Game rules","""
================================= **INSTRUCTIONS** =========================================

         You are a code breaker and your goal is to guess the
         secret code.
         
         The code is a sequence of numbers ranging from 1 to 8,
         and in each round after you make a guess, you will get hints
         which will help to improve your guess.Repeat this until
         you figure out the secret code.
         
         
         The hints are w,b,n:
             w- One of your guess pegs has correct number but is in wrong position
             b-One of your guess pegs has correct number and is in the correct position
             n-One of the guess pegs is wrong
             
             
            Don't be fooled by w,b,n peg sequence:they are not in order with 
            your guess pegs.
            
            Using logic and comparing hints from different rounds, you can figure out
            which of your guess pegs are in correct position and which colours are correct
            ,but not in right position.

            
            
            IMPORTANT-
            1) Enter number in between 1 to 8 including 1 and 8 in easy mode
            2) Enter number in between 1 to 10 including 1 and 10 in intermediate mode
            3) Enter number in between 1 to 12 including 1 and 12 in hard mode
            4) Enter unique values in each step
    
            IMPORTANT COMMANDS-
            *to undo a move type u
            *to view current progress type p
            *to quit type q \n""")



      
def play_music():
  winsound.PlaySound("intro.wav", winsound.SND_ASYNC + winsound.SND_LOOP | winsound.SND_ALIAS )

def play_music1():
	winsound.PlaySound("music.wav", winsound.SND_ASYNC + winsound.SND_LOOP | winsound.SND_ALIAS )


play_music()
def close_window ():
	winsound.PlaySound(None, winsound.SND_ASYNC)
	play_music1()
	window.destroy()
	game()







def teaminfo():
  mb.showinfo("ABOUT US","SECTION I     TEAM:20    SEM:1\nBasavaprabhu: PES1UG20CS631\nAlan S Paul:  PES1UG20CS624\nChaithanya Madhav: PES1UG20CS634")




def close_window3 (): 
	
  window.destroy()



sleep(0)	
window=tk.Tk()	
	
window.geometry('800x1000')
window.title("Mastermind (mini project)")
bg2=PhotoImage(file="MASTERMIND.png") 
label4=tk.Label(window,font='Helvetica 50', image=bg2)
label4.place(x=0,y=0,relwidth=1,relheight=1)
bt1 = tk.Button (window, text = "START",bg="black",fg="white",width=25,height=2, command = close_window).place(relx=0.5, rely=0.5, anchor=CENTER)	
bt2=tk.Button(window,text="HOW TO PLAY",bg="black",fg="white",width=20,height=2,command=rules).place(relx=0.5, rely=0.575, anchor=CENTER)
bt3 = tk.Button (window, text = "ABOUT US",bg="black",fg="white",width=25,height=2, command = teaminfo).place(relx=0.5, rely=0.65, anchor=CENTER)
bt4 = tk.Button (window, text = "QUIT",bg="black",fg="white",width=25,height=2, command = close_window3).place(relx=0.5, rely=0.725, anchor=CENTER)
window.mainloop() 




