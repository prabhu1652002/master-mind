

import random
import sys
import tkinter as tk
from tkinter import *
import time
from time import sleep
import tkinter as tk
from tkinter import messagebox as mb
import winsound

#from playsound import playsound
#import multiprocessing




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
            
            Using logic and compring hints from different rounds, you can figure out
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



      
window=tk.Tk()
window.geometry('800x1000')
window.title("Mastermind (mini project)")
bg2=PhotoImage(file="MASTERMIND.png") 
label4=tk.Label(window,font='Helvetica 50', image=bg2)
label4.place(x=0,y=0,relwidth=1,relheight=1)

def play_music():
	songs=["sound1.wav","sound2.wav"]
	winsound.PlaySound(random.choice(songs), winsound.SND_ASYNC + winsound.SND_LOOP | winsound.SND_ALIAS )



def close_window ():

  window.destroy()
  
  play_music()
  game()
bt1 = tk.Button (window, text = "START",width=25,height=2, command = close_window).place(relx=0.5, rely=0.5, anchor=CENTER)



bt2=tk.Button(window,text="HOW TO PLAY",width=20,height=2,command=rules).place(relx=0.5, rely=0.575, anchor=CENTER)


def teaminfo():
  mb.showinfo("ABOUT US","Team 20:\nAlan S Paul\nChaithanya Madhav\nBasavaprabhu")
bt3 = tk.Button (window, text = "ABOUT US",width=25,height=2, command = teaminfo).place(relx=0.5, rely=0.65, anchor=CENTER)



def close_window3 (): 
	
  window.destroy()
bt4 = tk.Button (window, text = "QUIT",width=25,height=2, command = close_window3).place(relx=0.5, rely=0.725, anchor=CENTER)


def game():          
  def easy():
      a=[1,2,3,4,5,6,7,8]
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
  def is_unique_value(n1,peg,d):
      for i in range (0,n1-1):
          if d[i]==int(peg):
              return False
      return True   
  def progress():
      if n==1:
          print("Values you have entered in current turn",d)
      else:    
       print("OUTPUT DATA")
       for i in range(n-1):
          print(i+1,"-",r1[i],r2[i],"\n")
       print("Values you have entered in current turn",d)    





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

              
  color=list()
   # Number of colours

  c=random.sample(a,len(result)) 
  #print(c)   #SOLUTION

  d=list()
  n=1

  r1=list()
  r2=list()


  while result!=color:
      
    print("TURN",n,)
    n1=1
  #input

    color.clear()
    d.clear()
    while n1<=len(result):
       
      peg=input("Enter number"+str(n1)+'\t')
      
      
      if peg.isnumeric()==True:
          if n1==1:
              if int(peg) in a:
                  d.append(int(peg))
              else:
                  print('Enter value within range',a)
                  continue
        	             
                                 
	    	            
          
          elif int(peg) in a:
              if is_unique_value(n1,peg,d)==True:
                  d.append(int(peg))
              else:
                  print("Enter unique values")
                  print("Values that you have aldready entered",d)
                  continue
          
              
              
          
              
          else:
              
              print("Enter value  within the range",a)
              continue
     
      else:
          
          if peg.lower()=="q": # QUIT
              sys.exit()
          elif peg.lower()=="u": #UNDO
                  if n1==1:
                      print("You cannot use undo option in the first entry")
                      continue
                  else:
                      n1=n1-1
                      del d[n1-1]
                      continue
          elif peg.lower()=="p":
              progress()
              continue    
              
          
          print('Enter value within range',a)
          continue
      n1=n1+1
    print("\n")  
    
   # print(d)
  #Output
    n+=1
    
    task=""
    for k in d:
      for j in c:
          if c.ind(j)==d.ind(k) and j==k:
              color.append("b")
              task="complete"
              break
          elif j==k:
              color.append("w")
              task="complete"
              break
      if task!="complete":
          color.append("n")
      task=""
    random.shuffle(color)  #Comment this line to reduce difficulty
    #print(color)
    r1.append(tuple(d))
    r2.append(tuple(color))
    print("OUTPUT DATA")
    for i in range(n-1):
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
  window2.geometry('200x300')
  window2.title("GAME REPORT")
  label1=tk.Label(window2,font='Helvetica 15', text="RESULT").pack()

  def results():
    mb.showinfo("Time(s)",int(e-s))
    mb.showinfo("Rounds",n-1)
    print("Time taken (seconds): ",int(e-s))
    print("No of rounds: ",n-1)
  bt4=tk.Button(window2,text="Click Here",width=20,height=2,command=results).pack(side=tk.TOP)

  def close_window2 (): 
    window2.destroy()
  bt5=tk.Button(window2,text="Close",width=20,height=2,command=close_window2).pack(side=tk.TOP)




winsound.PlaySound(None, winsound.SND_ASYNC)
window.mainloop() 