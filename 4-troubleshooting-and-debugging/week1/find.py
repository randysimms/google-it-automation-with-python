
sortme = True

def find_item(items, item):
  global sortme
  #Returns True if the item is in the list, False if not.

  if len(items) == 0:
    return False

  #Is the item in the center of the list OR list size is 1 (with index 0)?
  middle = len(items) // 2
  if items[middle] == item:
    #print("Found item: {}".format(item))
    sortme = True
    return True

  if (sortme):
    items.sort()
    sortme = False #only sort list once per recursion group

  #Is the item in the first half of the list?
  if item < items[middle]:
    #Call the function with the first half of the list
    #print("Searching first {} for: {}".format(middle,item))
    foundme = find_item(items[:middle], item)
    sortme = True
  else:
    #Call the function with the second half of the list
    #print("Searching second {} for: {}".format(middle,item))
    foundme = find_item(items[middle + 1:], item)
    sortme = True  #reset for next recursion group

  # end of recursion
  return foundme


#extra tests
print(find_item(["Alex"], "Alex") )  #only one
print(find_item(["Parker","Alex"], "Alex") )   #size 2, at end of list
print(find_item(["Parker", "Drew","Alex"], "Alex") )   #size 3 (sort required at this point) Alex at end of list
print(find_item(["Parker", "Drew","Alex", "Jordan"], "Alex") )  #at end of list
print(find_item(["Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"], "Alex") ) #at start of list
print("")

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

#sortme = True
print(find_item(list_of_names, "Alex")) # True
#sortme = True
print(find_item(list_of_names, "Andrew")) # False
#sortme = True
print(find_item(list_of_names, "Drew")) # True
#sortme = True
print(find_item(list_of_names, "Jared")) # False