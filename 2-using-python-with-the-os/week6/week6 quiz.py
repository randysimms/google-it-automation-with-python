def highlight_word(sentence, word):
    return(sentence[:sentence.index(word)] + word.upper() + sentence[sentence.index(word)+len(word):])

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def format_address(address_string):
    # Declare variables
    number = ""
    street = ""
    # Separate the address string into parts
    words = address_string.split()

    # Traverse through the address parts
    for word in words:
        # Determine if the address part is the
        # house number or part of the street name
        if (word.isnumeric()):
            number = word
        else:
            street +=  word + " "
        # Does anything else need to be done
        # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(number,street)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


def combine_lists(list1, list2):
    # Followed by the elements of jamie's list in reverse order
    list1.reverse()
    newlist = list2 + list1
    #assert isinstance(newlist, list)
    return newlist

Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
print(combine_lists(Jamies_list, Drews_list))



def squares(start, end):
	return [i*i for i in range(start,end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]




def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    guests2.update(guests1)
    return (guests2)


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))


def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        if letter.isalpha():
            # Add or increment the value in the dictionary
            lower = letter.lower()
            if lower not in result:
                result[lower] = 1
            else:
                result[lower] += 1

    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}





def car_listing(car_prices):
  result = ""
  for car,price in car_prices.items():
    result += "{} costs {} dollars".format(car,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))