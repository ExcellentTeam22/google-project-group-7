from AutoCompleteData import AutoCompleteData
import re
from operator import itemgetter

my_dict = {
    "i": (("i have a brand new bag", "./"), ("do i have a dog", "./"), ("you and i", "./") ),
    "have": (("i have a brand of channel", "./"), ("do i have a dog big", "./"), ("you have me", "./") ),
    "a": (("i have a brand new monkey", "./")
           , ("do i have a dog", "./"), ("a monster was born", "./") ),
    "brand": ("i have a brand new book", "./"),
    "new": ("i have a brand new car", "./"),
    "bag":( ("i have a brand new phone", "./"), ("big bag", "./") ),
    "hat": ("the dog in the hat", "./"),
    "the": (("the cat in the hat", "./"), ("the weather is", "./"),
               ("the water is cold", "./"),
           ("i have the umbrella", "./") ),
    "and": ("the water is cold and dirty", "./"),
    "cat": ("the cat in the hat", "./")
}
#------------------------------------------------------------------------------------------------------------------
def check_for_sentence(word, wordList):
#worldList the sentence from the user , word that we are gonna check


  res = list(my_dict[word])


  for index in my_dict.keys() :
        if index != word:
            for index2 in my_dict[index] :
               if wordList in index2 and index2 not in res:
                print("added", index2)
                res.append(index2)



  for temp in res:
    if wordList in temp or  wordList in temp[0]:
       print("the sentence is: ", temp)

#------------------------------------------------------------------------------------------------------------------
if _name_ == '_main_':


   x = str(input("Enter a sentence, please:"))


   #aqui dividimos en palabras
   divide_x = re.sub("[^\w]", " ", x).split()


   for word in divide_x:
       for word2 in my_dict.keys():
           if word == word2:
              check_for_sentence(word, x)