

from word_lists import *

banner = r'''  /$$$$$$                                          /$$                                        
 /$$__  $$                                        | $$                                        
| $$  \__/  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$$| $$$$$$$  /$$   /$$      /$$$$$$  /$$   /$$
| $$       /$$__  $$| $$  | $$| $$__  $$ /$$_____/| $$__  $$| $$  | $$     /$$__  $$| $$  | $$
| $$      | $$  \__/| $$  | $$| $$  \ $$| $$      | $$  \ $$| $$  | $$    | $$  \ $$| $$  | $$
| $$    $$| $$      | $$  | $$| $$  | $$| $$      | $$  | $$| $$  | $$    | $$  | $$| $$  | $$
|  $$$$$$/| $$      |  $$$$$$/| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$ /$$| $$$$$$$/|  $$$$$$$
 \______/ |__/       \______/ |__/  |__/ \_______/|__/  |__/ \____  $$|__/| $$____/  \____  $$
                                                             /$$  | $$    | $$       /$$  | $$
                                                            |  $$$$$$/    | $$      |  $$$$$$/
                                                             \______/     |__/       \______/ '''

help = '''

Crunchy.py generates custom wordlists that are related to different catagories. An example of use is if the bruteforce
target is a teacher, there are default terms that are added to you spacific target's information...

EXAMPLE: catagory selected: teacher : userinput: "Mr.Bob","Schoolname" -> iloveteaching{SCHOOLNAMEHERE}

The possible catagories of attack are listed below... help add catagories by contributing on github!

teacher


'''


def get_user_words():
	'''Gets the users words and catagory they want to create possible passwords from'''
	catagory_selection = input("What catagory of words would you like to use?>> ")

	if catagory_selection.lower() == "help":
		print(help)

	elif catagory_selection.lower() == "teacher":
		catagory_words = teacher_words

	elif catagory_selection.lower() == '':

		print(help)

	print("NOTE:You only have to put a word in once, 'ex: School, school' does not matter because they are all formated lower")
	user_input = input("Please enter your words seperated by a comma>> ".lower())

	user_list = user_input.split(",")

	user_list = list(user_list)

	print("Category: {}. Words: {}".format(catagory_words, user_input))
	print()
	return catagory_words, user_list


def create_list(catagory_words,user_list):

	with open('wordlist.txt','w') as f:
		for w1 in user_list:
			for w2 in catagory_words:

				f.write(w1+w2)
				f.write(w2 + w1)
				f.write(w1.upper() + w2.upper() + "\n")
				f.write(w2.upper() + w1.upper()+ "\n")
				f.write(w1.lower() + w2.lower()+ "\n")
				f.write(w2.lower() + w1.lower()+ "\n")
				f.write(w1.capitalize() + w2.lower()+ "\n")
				f.write(w2.capitalize() + w2.lower()+ "\n")
	f.close()

def check_for_duplicates():
	'''This does not work'''
	with open('wordlist.txt','w+') as f:
		for word in f:
			for word2 in f:
				if word == word2:
					line = line.replace(word, "")
					f.write(line)
				else:
					pass


def main():
	print(banner)
	print(help)
	catagory_words, user_list = get_user_words()
	create_list(catagory_words,user_list)
	print('List Created')

if __name__ == '__main__':
	main()