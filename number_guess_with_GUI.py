#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from easygui import *
import random

secret_num = random.randint(1, 99)
guess = 0
tries = 0

msgbox("""Hi, I'm a pirate!  
You have to play this number guessing game. 
I have a secret number which is from 1 to 99. 
You have to get the right answer in 6 times. 
Otherwise, you will die. 
Good luck!""")

while guess != secret_num and tries < 6:
    guess = integerbox("What's your guess, man?")
    if not guess: break
    if guess < secret_num:
        msgbox(str(guess) + " is too low.")
    elif guess > secret_num:
        msgbox(str(guess) + " is too big.")
    tries += 1
if guess == secret_num:
    msgbox("You are so lucky, you find my secret number!")
else:
    msgbox("No more guesses, you will die! The number is " + str(secret_num))