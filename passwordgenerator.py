# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:29:49 2020

@author: Bhanu
"""

from random import choice,shuffle

letter_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
             "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

number_list=["0","1","2","3","4","5","6","7","8","9"]

symbols_list=["!","#","$","%","&","(",")","*","+"]


print("Welcome to the Python Random Password Generator")
n_letters=int(input("How many letters you want in your password\n"))
n_numbers=int(input("How many numbers you want in your password\n"))
n_symbols=int(input("How many symbols you want in your password\n"))

password=[]

for char in range(0,n_letters):
    password.append(choice(letter_list))

for num in range(0,n_numbers):
    password.append(choice(number_list))
for sym in range(0,n_symbols):
    password.append(choice(symbols_list))
   
shuffle(password)

randompassword=""
for char in password:
    randompassword+=char
print(f"your password is {randompassword}")
