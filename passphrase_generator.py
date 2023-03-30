#!/usr/bin/python

import sys
import random
import string 

from passwd import *

class passphrase_generator():
    
    def get_word(self):
        
        # Get 5 random number between 1-6
        a = random.sample(range(1,6),5)
        
        output = str(a)
        output = output.replace(',', '')
        output = output.replace(' ', '')
        output = output.replace('[', '')
        output = output.replace(']', '')

        word = passwd_dict.get(output)

        return word
    
    def capitalize_passphrase(self, input):
        return [i.capitalize() for i in input]

#Display usage for this script
def display_help():
    print("\nusage: passphrase_generator.py number_words capitalize include_number\n")

def main(number_words, capitalize, include_number):

    passphrase_list = []

    for _ in range(int(number_words)):
        passwd = passphrase_generator()
        passphrase_list.append(passwd.get_word())

    if capitalize == 'True':
        passphrase_list = passwd.capitalize_passphrase(passphrase_list)

    passphrase = ' '.join(passphrase_list)

    if include_number == 'True':
        passphrase = passphrase + str(random.randint(0,9))

    print(f"Your passprase is: {passphrase}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        display_help()
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])