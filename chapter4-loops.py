# LOOPS
# for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#     print("Hi", name, "Please come to my party on Saturday!")
    
for cat_name in ["Moose", "Ashes", "Boo", "Smokey", "Lizzo", "GaGa", "Trooper"]:
    print("Hi", cat_name, "Please come to the vet for your check-up")

# name in this for statement is called the loop variable.

# The list of names in the square brackets is called a Python list. Lists are very useful. We will have much more to say about them later.

# Line 2 is the loop body. The loop body is always indented. The indentation determines exactly what statements are “in the loop”. The loop body is performed one time for each name in the list.

# On each iteration or pass of the loop, a check is done to see if there are still more items to be processed. If there are none left (this is called the terminating condition of the loop), the loop has finished. Program execution continues at the next statement after the loop body.

# If there are items still to be processed, the loop variable is updated to refer to the next item in the list. This means, in this case, that the loop body is executed here 7 times, and each time name will refer to a different friend.

# At the end of each execution of the body of the loop, Python returns to the for statement, to see if there are more items to be handled.