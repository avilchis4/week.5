#collection = single "variable" used to store multiple values 
#list = [] ordered and changeable. Duplicates OK
#set = {} unordered and imutable, but add/remove OK. NO duplicates
#tuple = () ordered and unchangable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut", "kiwi", "strawberry", "grape"]

 # print(fruits[::-1]) #reverses order

# for fruit in fruits:
#     print(fruit)

# print (dir(fruits)) #prints out methods
# print (help(fruits)) 
# print (len(fruits)) #how many in your list
# print("pineapple" in fruits)

# fruits[0] = "pineapple" #i can reassign values with this
# fruits.append ("pineapple") #add items at the end
# fruits.remove("apple")
# fruits.insert(0,"pineapple") #insert as certain index
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))

# print(fruits)



cars = ["bmw", "masterati", "audi", "mercedes", "ferrari"]
print(f"these are a list of cars {cars}")
print(f"the first car is {cars[0]}")

#changing value of list
cars[0] = "toyota"
print(f"the first car is {cars[0]}")

print(f"the last car is {cars[-1]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")

#adding a new value to the list
cars.append("bugatti")
print(cars)

#loopingthrough the list
#otherwise called iterating through the list
for car in cars:
    # print(len(car))
    # print(car)
    carRequest = input ("add a new car please: ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    #print(cars.upper())
    print (cars)
    if len(cars) >= 10:
        break

#create a list of friends
#make sure the intial is none
friends = []

