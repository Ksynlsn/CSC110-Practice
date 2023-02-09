def printGreeting(cat_name):
    if cat_name != "Ashes":
        msg = print(f"Hi, {cat_name}, this is your message")
    elif cat_name == "Ashes":
        msg = print(f"Hi, {cat_name}, this is your message. You have been very bad!")

    # return print(f"Hi, {cat_name}, this is your message")

def reverseCatName(cat_name):
    for element in cat_name[ : :-1]:
        print(element, end =' ')
    print('\n')