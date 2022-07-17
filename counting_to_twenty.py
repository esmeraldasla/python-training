#use a for loop to print the numers from 1 to 20, inclusive.

numbers = list(range(1, 21))

for number in numbers:
    print(number)

#Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

print("\nOdd numbers")

odd_numbers = list(range(1, 21, 2))
for odd in odd_numbers:
    print(odd)
