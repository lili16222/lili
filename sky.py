
# # bai tap 1
# pasword = input ('enter your pw')
# if len (pasword)>10 and any (x.isdigit() for x in pasword) and any (x.upper() for x in pasword):
#  print ('strong')
# elif 6 < len (pasword) <= 10 and any (x.isdigit() for x in pasword):
#  print ('medium')
# else: 
#  print ('weak')



# Kitty = input ('Enter your number')
# def is_prime(n):
#     if n < 2:
#         return False         # số < 2 không phải số nguyên tố
#     for i in range(2, n):
#         if n % i == 0:      # nếu chia hết cho i → không phải số nguyên tố
#             return False
#     return True              # không tìm thấy ước → là số nguyên tố

# Mickey = []
# if Kitty.isdigit() and int (Kitty) <=100:
#    for i in range (2, int(Kitty)):
#     if is_prime(i):
#       Mickey.append (i)
# else: 
#  print (' not a integer')
# print ('the total count of prime number is ', Mickey)


# Sum = 0
# for j in Mickey: 
#    Sum += int(j)
# print ('total of prime number is ', Sum)

# smallest = min (Mickey)
# print ('smallest prime number is ', smallest)
# largest = max (Mickey)
# print (' largest prime number is ', largest)


# # bai tap 2 other way
# input1 = int(input("Input a number: "))
# prime=[]

# for i in range(2,input1+1):
#     isprime = True
#     for a in range (2,i):
#         if i % a == 0:
#             isprime = False
#     if isprime == True:
#         prime.append(i)

# # if len(prime) > 0:
# #     print('Prime numbers found',':',prime)
# #     print('Total primes found',':',len(prime))
# #     print('Largest prime',':',max(prime))
# #     print('Smallest prime',':',min(prime))
# #     print('Sum of all primes',':',sum(prime))
# # else: 
# #     print('no prime')


# # bai tap 3


# def calculate_grade(score):
#     if 85 <= score <= 100:
#         return 'HD'
#     elif 75 <= score <= 84:
#         return 'D'
#     elif 65 <= score <= 74:
#         return 'C'
#     elif 50 <= score <= 64:
#         return 'P'
#     else:
#         return 'F'

  
# num_std = []
# score = []
# names = []
# scores = []

# # Numstudents


# while True:
#     num_std = int(input('How many students are there? '))

#     if num_std > 10 or num_std < 3:
#         print('Please enter a number between 3 and 10')
#     else:
#         break

# for i in range (num_std):
#    print('\nStudent ' , str(i+1) , ":")
#    name = input ('Enter name student: ')
#    while True:
#     score = float(input('Enter score student: '))
#     if score <0 or score >100:
#        print ('Please enter score between 0 and 100')
#     else:
#         break
#    names.append(name)
#    scores.append(score)
 

# average = sum(scores) / int (num_std)
# highest = max (scores)
# lowest = min (scores)
# print("\n=== RESULTS ===")
# for n in range(len(names)):
#     print("Student" , names[n] , "has grade" , calculate_grade(scores[n]))
# print("Average score:", average)
# print("Highest score:", highest, "Student:", names[scores.index(highest)])
# print("Lowest score:", lowest, "Student:", names[scores.index(lowest)])


# Bai tap 4

# a = input ('Enter a sentence ')
# b = a.split()
# print('total words is ', len(b))
# print('longest words is ', max(b, key = len))
# print('uppercase is ', a.upper())
# print('lowercase is ', a.lower())
# print(a.title())
# print
cvdvd
# bai tap 4 other way
# user input the sentence
# sentence = input('sentence: ')

# # split the sentence to words

# splitword = sentence.split()
# print('Total words',':',len(splitword)) 

# print(splitword)

# # Find the longest word
# if len(splitword) > 0:
#     longestword = max(splitword,key=len)
#     print('Longest word',':',longestword,'(',len(longestword),'letters',')')
# else:
#     print ('no word found')

# #Print the outcome

# print(sentence.upper())
# print(sentence.lower())
# print(sentence.title())
# print(sentence[::-1])


# # ass1- ex1
# with open("raw_text.txt", "r") as a:
#     text1 = a.read()


# s_1 = int(input('Enter shift 1 value: '))
# s_2 = int(input('Enter shift 2 value: '))
# encrypted = ""
# decrypted = ''



# for i in text1:
#     if i.isalpha():
#         if 97 <= int(ord(i))<= 109:
#             encrypted += chr(((int(ord(i)) + s_1 * s_2)-97)%26+97)
#         elif 110 <= int(ord(i))<= 122:
#             encrypted += chr(((int(ord(i)) - s_1 - s_2)-97)%26+97)
#         elif 65 <= int(ord(i))<= 77:
#             encrypted += chr(((int(ord(i)) - s_1)-65)%26+65)
#         else:
#             encrypted += chr(((int(ord(i)) + s_2*s_2)-65)%26+65)
#     else:
#         encrypted += i


# with open('encrypted.txt', 'w') as b:
#     b.write(encrypted)
# with open ('encrypted.txt', 'r') as c:
#     text2 = c.read()

# for f in text2:
#     if 97<= (ord(f) - (s_1 * s_2)-97)%26+97 <= 109:
#         decrypted += chr((ord(f) - (s_1 * s_2)-97)%26+97)
#     elif 110 <= (ord(f) + s_1 + s_2 - 97)%26+97 <= 122:
#         decrypted += chr((ord(f) + s_1 + s_2 - 97)%26+97)
#     elif 65 <= (ord(f) + s_1 - 65)%26+65 <= 77:
#         decrypted += chr((ord(f) + s_1 - 65)%26+65)
#     elif 78<= (ord(f) - s_2*s_2 - 65)%26+65 <= 90:
#         decrypted += chr(ord(f) - s_2*s_2 - 65)%26+65
#     else:
#         decrypted +=f
            
    
# with open ('decrypted.txt', 'w') as d:
#     d.write(decrypted)
# with open ('decrypted.txt', 'r') as e:
#     text3 = e.read()

# if text1 == text3:
#     print ('Decryption successful')




  



    
            










# with open("encrypted.txt", "w") as f:
#     f.write(encrypted)

# print("Encryption complete! Encrypted file created: encrypted.txt")
