#!/usr/bin/env python
import os
from random import randint
import string
max_lives=6

def print_gallows(lives):
	if lives==max_lives:
		print " _________     "
		print "|         |    "
		print "|              "
		print "|              "
		print "|              "
		print "|              "
		print "|              "
	elif lives==max_lives-1:
		print " _________     "
		print "|         |    "
		print "|         0    "
		print "|              "
		print "|              "
		print "|              "
		print "|              "
	elif lives==max_lives-2:
		print " _________     "
		print "|         |    "
		print "|         0    "
		print "|         |    "
		print "|              "
		print "|              "
		print "|              "
	elif lives==max_lives-3:
		print " _________     "
		print "|         |    "
		print "|         0    "
		print "|        /|    "
		print "|              "
		print "|              "
		print "|              "
	elif lives==max_lives-4:
		print " _________     "
		print "|         |    "
		print "|         0    "
		print "|        /|\   "
		print "|              "
		print "|              "
		print "|              "
	elif lives==max_lives-5:
		print " _________     "
		print "|         |    "
		print "|         0    "
		print "|        /|\   "
		print "|        /     "
		print "|              "
		print "|              "
	elif lives==max_lives-6:
		print " _________     "
		print "|         |    "
		print "|         0    "
		print "|        /|\   "
		print "|        / \   "
		print "|              "
		print "|              "

def random_word():
	words = [line.rstrip('\n') for line in open('wordsEn.txt')]
	word=words[randint(0, len(words)-1)]
	return word

def take_guess():
	while True:
	    userInput = raw_input('Take a guess:')
	    if len(userInput) == 1:
	        if userInput in string.letters:
	            break
	        print 'Please enter only letters\n'
	    else:
	        print 'Please enter only one character\n'
	guessInLower = userInput.lower()

	return guessInLower


def print_word(word):
	for char in word:
		print char


def obscure_word(word, correct_chars):
	obscured_word=list("")
	for char in word:
		obscured_word.append("_")


	for char in correct_chars:
		if char in word:
			obscured_word[word.find(char)]=char

	return "".join(obscured_word)

#Had to use the os.system method because entering the ansi escape sequence doesnt
#work in windows cmd prompt
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')


def game():
	cur_lives=max_lives
	the_word=random_word()
	total_chars=len(the_word)
	correct_chars=[]
	incorrect_chars=[]


	while cur_lives>0:
		clear_screen()
		print "HANGMAN\n"
		print_gallows(cur_lives)
		print "\nStatus:"
		print obscure_word(the_word, correct_chars)+"\n"
		print "\nIncorrect guesses:"
		print "".join(incorrect_chars)
		guess = take_guess()
		if guess in incorrect_chars or guess in correct_chars:
			print "Already tried "+guess
		else:
			if guess in the_word:
				correct_chars.append(guess)
			else:
				incorrect_chars.append(guess)
				cur_lives-=1
			if len(correct_chars)==len(the_word):
				print "YOU WIN!"
				return

	clear_screen()
	print "HANGMAN\n"
	print_gallows(cur_lives)
	print "\nStatus:"
	print "The word was: "+the_word
	print "GAME OVER"


def main():
	game()


if __name__ == '__main__':
	main()
