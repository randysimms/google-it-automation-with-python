

def try_this_out():
    try:
        print("123")
        raise ValueError("don't print")
    except:
        print("got error")
        return None
    print("done")

try_this_out()
print("the end")

