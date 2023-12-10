#Lambda function that doubles the value
print("---The double of the numbers are")
double = lambda x:x * 2
h = int(input("Enter a number :"))
print("The double of the number is :",(double(h)))
print("  ")

#Using map() filter() which are the bulit in functions in lambda functions
#Filter function
#filter out only even numbers in the list
print("---Seprating only even numbers from the list")
num = [1,2,5,2,2,5]
nwe = list(filter(lambda x: (x%2 == 0), num))
print("The even munbers are :",(nwe))
print()

#Doubles the number using map() which is also an inbulit function of lambda
#Map function.
#Doubles the number present in the list

print("""---Doubles the number present in the list :
   num = [1,2,5,2,2,5]""")
mp = list(map(lambda x:x * 2, num))
print(mp)


