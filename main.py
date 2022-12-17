import re

print("SimplyEvalCalculator")
print("You can do anything with operators")
print("Addition'+',subtraction '-'")
print("Multiplication '*', division '/'")
print(" ")
print("Enter 'exit' to close the calculator\n")

starting = 0
run = True

def actionmath():
    global run
    global starting
    task = ""
    if starting == 0:
        task = input("input your number: ")
    else:
        task = input(str(float(starting)))


    if task == 'exit':
        print("Goodbye bro")
        run = False
    else:
        task = re.sub('[a-zA-Z,:()" "]', '', task)
# use re to limit the characters that the user can enter. An unchecked eval() function can lead to a security hole in a larger application.

        if starting == 0:
            starting = eval(task)
        else:
            starting = eval(str(starting) + task)
        print("your result: ")


while run:
    actionmath()
