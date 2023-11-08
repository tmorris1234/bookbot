
def count_words(my_string):
  word_count = my_string.split()
  return len(word_count)

def letter_count(my_string):
  letter_dictionary = {}
  for letter in my_string:
    letter = letter.lower()
    #print(letter)
    if letter in letter_dictionary:
      letter_dictionary[letter] = letter_dictionary[letter]+1
    else:
      letter_dictionary[letter] = 1
  return letter_dictionary



with open("books/frankenstein.txt") as f:
    file_contents = f.read()

number_of_words = count_words(file_contents)
print(str(number_of_words) + " words were found in the document")
letters = letter_count(file_contents)
letter_list = [(number_letters,letter) for letter,number_letters in letters.items()]
letter_list.sort(reverse = True)
#print(letter_list)
for item in letter_list:
  if item[1].isalpha():
    print("the letter " + item[1] + " appears " + str(item[0]) + " times.")
