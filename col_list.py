#!/usr/bin/python3
# you were missing the / after #! in the shebang

col_list=["blue", "Columbus"]

col_list.append(1492)

# you need a = between user_input and ("What is your name?")

# you didn't have the input() function in there, missing the word "input"
user_input= input("What is your name?")
print(f"In  {col_list[2]} {col_list[1]} sailed the ocean {col_list[0]} . {user_input} fell off the boat.")
