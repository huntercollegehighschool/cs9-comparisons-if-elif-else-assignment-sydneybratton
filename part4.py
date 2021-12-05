'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''

#start writing your code below
integer_1= int(input("Enter a number: "))
integer_2 = int(input("Enter another number: "))

if integer_1 > 0 and integer_2 > 0:
  print("positive")
elif integer_1 < 0 and integer_2 < 0:
  print("negative")
elif integer_1 == 0 or integer_2 == 0:
  print("zero")
else:
  print("opposite")