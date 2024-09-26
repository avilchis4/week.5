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



# cars = ["bmw", "masterati", "audi", "mercedes", "ferrari"]
# print(f"these are a list of cars {cars}")
# print(f"the first car is {cars[0]}")

# #changing value of list
# cars[0] = "toyota"
# print(f"the first car is {cars[0]}")

# print(f"the last car is {cars[-1]}")
# cars[-1] = "lamborghini"
# print(f"the last car is {cars[-1]}")

# #adding a new value to the list
# cars.append("bugatti")
# print(cars)

# #looping through the list
# #otherwise called iterating through the list
# for car in cars:
#     # print(len(car))
#     # print(car)
#     carRequest = input ("add a new car please: ")
#     cars.append(carRequest)
#     print(cars)
#     print(len(cars))
#     #print(cars.upper())
# print (cars)
    #if len(cars) >= 10:
        #break

#create a list of friends
#make sure the intial is none
friends = []
#add a new friend to the list, add at least 5
friends.append("friend1")
friends.append("friend2")
friends.append("friend3")
friends.append("friend4")
friends.append("friend5")
print(friends)
#remove a friend
friends.remove("friend3")
#insert a friend at a specific index, maybe 2
friends.insert(2, "friend6")
#print the list of friends
print(friends)
#loop through the list and print the friends name
for friend in friends:
    print(len(friends))
    print (friends)
    friendRequest = input ("add another name: ")
    friends.append (friendRequest)
    print(friends)
    if len(friends) > 10:
        break
#see if a particular friend is in the list (boolean value)
#if the list is greater than 10, break the loop
 
