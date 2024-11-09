#First take input from the user
str = input(“Enter a string: ”)

result = “ ”

#iterate string one by one

for i in str:

   if i!= ‘ ’:

      result +=i

print(“The given string after removing all spaces is: ”, result)
