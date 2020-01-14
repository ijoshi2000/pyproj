 # Mad Libs
def madlibs():
    proper_name1 = input("Enter a name: ")

    proper_name2 = input("Enter another name: ")

    noun1 = input("Enter a proper title: ")

    place1 = input("Enter a place: ")

    place2 = input("Enter another place: ")

    verb1 = input("Enter a present-tense verb: ")

    noun3 = input("Enter a noun: ")

    noun2 = input("Enter a plural noun: ")

    noun4 = input("Enter another plural noun: ")

    num2 = input("Enter a number: ")

    num1 = input("Enter another number: ")

    percent1 = input("Enter another number: ")

    print("\nDear {},\n It is my pleasure to {} to you today. I am {} the great and I'm the mother of"

      "{} &{}. I have danced {} in {} but I want to dance more in {}. "

      "Please send me your {} and a sum of $ {}, {} to get started, and I will "

      "resume my work. \nYours truly, {}".format(

          proper_name1, verb1, proper_name2, noun1, place1, num1, noun2, 

          place2, noun3, num2, noun4, percent1, proper_name2))
madlibs()

