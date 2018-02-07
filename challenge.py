# 57 Create a List containing all of the numbers from 1 to 6. Use the sum function to calculate the sum of the contents of the list.

# myList = [1, 2, 3, 4, 5, 6]
# sumNum = sum(myList)
# print(sumNum)

# 58 Use the range function to create a range from 0 to 99, use the list function to convert the range into a list. Print the list.

# myList = list(range(0, 99))
# print(myList)

# 59 Use the range and list functions to create a list of all of the even numbers from 10 to 50 (including 50). Print out the length of that list.

# myList = list(range(10, 51, 2))
# print(myList)

# 60. Create the following list of lists.
# [[0], [0, 1], [0, 1, 2] ... [0, 1, 2, 3, 4, 5, 6]]
# print the 3rd item of the fifth list.

# myList = [list(range(0, 1)), list(range(0, 2)), list(range(0, 3)), list(range(0, 4)), list(range(0, 5)), list(range(0, 6)), list(range(0, ))]
# print(myList)
# print(myList[4])
# print(myList[4][2])

# 61. Create an empty list called evens. Write a for loop that loops through all the numbers from 0 to 10. Append the even numbers to the evens list. Print out the evens list.

# evens = []
# for e in range(0, 11, 2):
#     evens.append(e)
# print(evens)


# 62. Create any list with at least 10 items. Use python's list slicing syntax to print
# The first item
# The last item
# All but the first item
# All but the last item

# myList = list(range(0, 11))
# print(myList)
# print(myList[:1])
# print(myList[-1:])
# print(myList[1:])
# print(myList[:-1])


# 63. Create a dictionary that represents a student. Each student has a name, an age, a nationality, and a list of subjects.

# stud1 = {
#     'name': 'Dan',
#     'age': 40,
#     'nationality': 'Romanian',
#     'subjects': ["Math", "Chemistry", "History"]
#     }
# stud2 = {
#     'name': 'Emma',
#     'age': 38,
#     'nationality': 'Irish',
#     'subjects': ["English", "Chemistry", "Sience"]
#     }
# stud3 = {
#     'name': 'Ann',
#     'age': 20,
#     'nationality': 'Italian',
#     'subjects': ["Literature", "Chemistry", "Arts"]
#     }
# stud4 = {
#     'name': 'Goga',
#     'age': 30,
#     'nationality': 'German',
#     'subjects': ["Biology", "Chemistry", "History"]
#     }
# print(stud1)

# 64. Create a list containing at least 4 of the students described in challenge 63
# Convert the list into a dictionary, use the the students names as the key for the dictionary. (edited)

# listOfStudents = [stud1, stud2, stud3, stud4]
# print(listOfStudents)
# dictionaryOfStudents = dict(listOfStudents)
# print(dictionaryOfStudents)

# 65. Create a dictionary where the keys are words in the english language, and the values are the lengths of the words.
# 66. Data Structures Challenge
# Model the following scenario data using any combination of Lists and Dictionaries that you feel is appropriate.
# A Musician has a name, nationality, and gender. A Musician can play in any number of bands. A Musician can play multiple instruments. For each instrument they have a competency level between 1 and 100.
# Create a data structure that stores the details of each musician along with the bands and instruments.
# It should be possible to get the details of any musician by name, so use a dictionary to store the musician details.

#Feedback
# l = [
#     [0],
#     [0, 1],
#     [0, 1, 2],
#     [0, 1, 2, 3],
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4, 5],
#     [0, 1, 2, 3, 4, 5, 6]
#   ]

# print(l[4][2])

# # ========================================

# evens = []
# odds = []

# for x in range(11):
#   if x % 2 == 0:
#       evens.append(x)
#   else:
#       odds.append(x)
       
# # =======================================

# def is_interesting(n):
#   is_even = n % 2 == 0
#   mult_five = n % 5 == 0
#   is_thirteen = n == 13
#   return is_even or mult_five or is_thirteen

# interesting_lc = [i for i in range(100) if is_interesting(i)]
# print(interesting_lc)

# interesting = []
# for i in range(100):
#   if is_interesting(i):
#       interesting.append(i)

# print(interesting)
       
# print(evens)
# print(odds)

# students = [
#   {
#   'name': 'A. N. Other',
#   'age': 44,
#   'nationality': 'Irish',
#   'subjects': [
#       {'title': 'English', 'teacher': 'Richard'},
#       {'title': 'Maths', 'teacher': 'Richard'},
#       {'title': 'Art', 'teacher': 'Richard'},
#       ]
#   },
#   {
#   'name': 'Tom Thumb',
#   'age': 4,
#   'nationality': 'Irish',
#   'subjects': [
#       {'title': 'English', 'teacher': 'Richard'},
#       {'title': 'Maths', 'teacher': 'Richard'},
#       {'title': 'Art', 'teacher': 'Richard'},
#       ]
#   },
#   {
#   'name': 'Goldilocks',
#   'age': 14,
#   'nationality': 'Irish',
#   'subjects': [
#       {'title': 'English', 'teacher': 'Richard'},
#       {'title': 'Maths', 'teacher': 'Richard'},
#       {'title': 'Art', 'teacher': 'Richard'},
#       ]
#   },
#   {
#   'name': 'Jack',
#   'age': 24,
#   'nationality': 'Irish',
#   'subjects': [
#       {'title': 'English', 'teacher': 'Richard'},
#       {'title': 'Maths', 'teacher': 'Richard'},
#       {'title': 'Art', 'teacher': 'Richard'},
#       ]
#   },
# ]


# Message #bootcamp-jan2018


# words = ["big", "small", "car", "student"]
# d = { word : len(word) for word in words }
# print(d)

# with open("words.txt") as f:
#   words = f.read().split('\n')
   
# d = [ len(word) for word in words ]

# print(max(d))

# =================================================

