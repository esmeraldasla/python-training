#Make a list of the numbers from one to one million, and then use a for loop to print the numbers

one_million = list(range(1, 1000001))
for individual_number in one_million:
    print(individual_number)

print(min(one_million))
print(max(one_million))
print(sum(one_million))