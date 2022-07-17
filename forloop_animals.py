#Think of at least three different animals that have a common characteristic.
#Store the names of these animals in a list,and then use a for loop to print out the name of each animal.

birds = ['Parrots', 'Bluebirds', 'Crows', 'Eagles']
for bird in birds:
     print(bird)

#Modify your program to print a statement about each animal, such as A dog would make a great pet.
#Add a line at the end of your program stating what these animals have in common.

birds = ['Parrots', 'Bluebirds', 'Crows', 'Eagles']
for bird in birds:
     print(f'{bird} are beautiful animals. \n')

print("Birds shouldn't be pets. They were not born to be in cages")