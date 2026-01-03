


# # a = input('Rock, Paper or Scissors? ')
# # b = input('Rock, Paper or Scissors? ')
# # if a == b:
# #     print ('draw')
# # elif (a=='rock' and b =='scissors') or (a=='paper' and b == 'rock') or (a=='scissors' and b == 'paper'):
# #     print ('a wins')
# # else:
# #     print ('b wins')
# # print ('Do you want to play again?')

# # import random
# # a = int(input('Guess a number: '))
# # b = random.randint(0,10)
# # if a==b:
# #     print (' exactly right')
# # elif a<b:
# #     print ('too low')
# # else: 
# #     print ('too high')

# # def greet(name):
# #     return "Hello " + name
# # a = greet(input('Enter your name: '))
# # print (a)


# # def square(num):
# #     return num*num
# # a = square(int(input('enter a number: ')))
# # print (a)
# # def range_tempt(x):
# #   if 0 < x < 10 :
# #     return True
# # list_tempt =[]
# # list_negative =[]
# # while True:         
# #  tempt1 = input('Enter tempt: ')
# #  if tempt1 == ('q' or 'Q'):
# #   break
# #  tempt=int(tempt1)
# #  list_tempt.append(tempt)
# # for i in list_tempt:
# #   if range_tempt(i):
# #     list_negative.append(i)
# # print ('Negative tempt is: ', list_negative)
# # a=[]
# # print('demo - break, continue and pass')
# # for i in range(1, 10):
# #     if i == 4:
# #         continue
# #     if i == 7:
# #         break
# #     a.append(i)
# # print(a)
# # pass # do nothing
# # print('This is the end of program')

        
# # import numpy as np


# names = []
# scores = []
# grade = []
# cek = True
# #start with input of number of students
# while True:
#     try:
#         students = int(input("How many students? "))
#         if students <= 0:
#             print("Please enter a positive integer.")
#         elif students < 3:
#             print("Number of students should be at least 3.")
#         elif students > 10:
#             print("Number of students should not exceed 10.")
#         else:
#             break
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")

# for i in range(students):
#     name = input(f"Student {i+1} name: ")
#     # Keep asking until the user enters a valid integer score
#     while True:
#         score_input = input(f"{name} score: ")
#         try:
#             score = int(score_input)
#             break
#         except ValueError:
#             print("Please enter a valid integer for the score.")

#     names.append(name)
#     scores.append(score)

# for i in range(len(scores)):
#     if scores[i] >= 85 and scores[i] <= 100:
#         grade.append('HD')
#     elif scores[i] >= 75 and scores[i] <= 84:
#         grade.append('D')
#     elif scores[i] >= 65 and scores[i] <= 74:
#         grade.append('C')
#     elif scores[i] >= 50 and scores[i] <= 64:
#         grade.append('P')
#     else:
#         grade.append('F')


# print("Students, Scores, and Grade:")
# for n, s, g in zip(names, scores, grade):
#     print(f"- {n}: {s} ({g})")

# if scores:
#     average = sum(scores) / len(scores)
#     max_score = max(scores)
#     min_score = min(scores)

#     # Collect names of students with the highest and lowest scores (handles ties)
#     highest_students = [(n, s) for n, s in zip(names, scores) if s == max_score]
#     lowest_students = [(n, s) for n, s in zip(names, scores) if s == min_score]

#     print("average score:", average)
#     print("highest score:", ", ".join([f"{n} ({s})" for n, s in highest_students]))
#     print("lowest score:", ", ".join([f"{n} ({s})" for n, s in lowest_students]))



def calculate_grade(n):
    if 85 <= n <= 100:
        return 'HD'
    elif 75 <= n <= 84:
        return 'D'
    elif 65 <= n <= 74:
        return 'C'
    elif 50 <= n <= 64:
        return 'P'
    else:
        return 'F'

 


# Check number of students


while True:
    num_std = input('How many students are there? ')
    try:
        int(num_std)
        if num_std > 10 or num_std < 3:
            print('Please enter a number between 3 and 10')
        else:
            break
    except ValueError:
        print('Please enter a number between 3 and 10')
# loop through student index
names = []
scores = []

for i in range (num_std):
    print(f'Student {i+1}:')
    name = input ('Enter student name: ')
    while True:
        score = int(input(f'Enter {name} score: '))
        if score <0 or score >100:
            print ('Please enter score between 0 and 100')
        else:
            break
    names.append(name)
    scores.append(score)
 #calculate 

average = round(sum(scores) / int (num_std),2)
highest = max (scores)
lowest = min (scores)
#print outcome
print("\n=== RESULTS ===")
for n in range(len(names)):
    print(f'{names[n]}: {scores[n]} ({calculate_grade(scores[n])})')
print("Average score:", average)
print("Highest score:", highest, "Student:", names[scores.index(highest)])
print("Lowest score:", lowest, "Student:", names[scores.index(lowest)])


