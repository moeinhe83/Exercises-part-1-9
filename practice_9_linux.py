# Practice_9

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 9', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value
name = ('m', 'o', 'e', 'i', 'n')

# Convert Tuple To String
name = ''.join(name)
print(name)
# Show Type Name
print(type(name))

# Finish
# Create By Moein Heshmati