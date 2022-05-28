#sets are used to store multiple elements into a single variable

#a set is unordered, unindexed and immutable

thislist = set(("apple", "banana", "cherry"))



print(thislist)

#sets can be of any data type

set1 = {"abc", 34, True, 40, "male"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# set() constructor turns list into sets

thisset1 = {"apple", "banana", "cherry"}

for x in thisset1:
  print(x)

  #since you can't index a set, you must call the whole set

thisset2 = {"apple", "banana", "cherry"}

print("banana" in thisset2)


thisset3 = {"apple", "banana", "cherry"}

thisset3.add("orange")

print(thisset3)

##this is how you append a list to a set

thisset4 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset4.update(tropical)

print(thisset4)


#the update method uses lists too

thisset5 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset5.update(mylist)

print(thisset5)

##you can apply all remove, pop, and discoard methods to sets too


