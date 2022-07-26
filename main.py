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
    "hat": ("the cat in the hat", "./"),
    "the": (("the cat in the hat", "./"), ("the weather is", "./"),
               ("the water is cold", "./"),
           ("i have the umbrella", "./") ),
    "and": ("the water is cold and dirty", "./"),
    "cat": ("the cat in the hat", "./")
}
#------------------------------------------------------------------------------------------------------------------
def check_for_sentence(word, wordList):
#worldList the sentence from the user , word that we are gonna check
    print('\n')



    res = list(my_dict[word])



    for index in my_dict.keys() :
        for index2 in my_dict[index]:
             # print("index2", index2)
            # print("world", wordList)
            if wordList in index2 :
                res.append(index2)


    # for i in res:
    #     print("list", i)

    for temp in res:
      # print("1",wordList, " 2", temp)

        if wordList in temp or  wordList in temp[0]:
            print("the sentence is:", temp)







#------------------------------------------------------------------------------------------------------------------
def divide_into_words():
   with open('Archive/python-3.8.4-docs-text/c-api/abstract.txt') as f:
      contents = f.read()
      #print(contents)

   wordList = re.sub("[^\w]", " ", contents).split()

   #print(wordList)

#------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

   divide_into_words()

   x = str(input("Enter a sentence, please:"))


   #aqui dividimos en palabras
   divide_x = re.sub("[^\w]", " ", x).split()




   for word in divide_x:
       for word2 in my_dict.keys():
           if word == word2:
                 check_for_sentence(word, x)

















