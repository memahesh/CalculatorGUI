# Importing required modules
from tkinter import *
import tkinter.messagebox

# Button Dimesnions
BUTTON_HEIGHT = 5
BUTTON_WIDTH = 10

# Some global variables
v = ""
operator=None
firstNumber = None
secondNumber = None

# Taking the values
def takeValues(x):
    # Accessing the global variables
    global firstNumber, v, secondNumber, operator

    # if x is one of operations
    if x in "+-*/":
        # Check if firstNumber is given before giving an operator
        if firstNumber:
            # If operator is not set, assign an operator
            if not operator:
                operator = x
                v.set(v.get() + x)
            else:
                # Showing error if operator already populated
                tkinter.messagebox.showerror("Message","[POPULATED_ERROR]:Operator is already given. Press 'C' to clean the previously entered values.")

        else:
            # Showing error to provide firstNumber before giving an operator
            tkinter.messagebox.showerror("Message","[NOT_POPULATED_ERROR]:Provide number first")

    else:
        # If operator is present, start filling the second number
        if operator:
            # If secondNumber is partially filled
            if secondNumber:
                secondNumber=secondNumber+x
                v.set(v.get() + x)
            else:
            # If secondNumber is starting to get filled
                secondNumber=x
                v.set(v.get() + x)
        else:
        # If operator is not present, it means firstNumber is not yet completely filled
            # If firstNumber is partially filled
            if firstNumber:
                firstNumber=firstNumber+x
                v.set(v.get()+x)
            else:
            # If firstNumber is starting to get filled
                firstNumber=x
                v.set(x)


# Emptying all the variables
def clean():
    global firstNumber, v, secondNumber, operator

    firstNumber =None
    secondNumber = None
    operator = None
    v.set("")

# Calculating the two numbers and operation
def calculate():
    global firstNumber, v, secondNumber, operator
    # If all are present
    if firstNumber and secondNumber and operator:

        # Dealing with zero error
        if(secondNumber=="0" and operator=="/"):
            tkinter.messagebox.showinfo("Message","[ZERO_ERROR]:Can't perform operation")
        else:
            # Operator and operation
            operation_dict = {
                "+": int(firstNumber) + int(secondNumber),
                "-": int(firstNumber) - int(secondNumber),
                "*": int(firstNumber) * int(secondNumber),
                "/": int(firstNumber) / float(int(secondNumber))
            }
            for x, y in operation_dict.items():
                if x == operator:
                    v.set("="+str(y)+" (Now press 'C')")
    else:
    # If all are not available

        # Prompting whichever are not available
        required_list = {
            "firstNumber": firstNumber,
            "secondNumber": secondNumber,
            "operator": operator
        }
        for x, y in required_list.items():
            if y == None:
                tkinter.messagebox.showinfo("Message", "[MISSING_VALUE]:Can't find "+x)



def main():
    global v
    root=Tk()
    root.title("MyCalcy")
    v = StringVar(root)
    mainFrame = Frame(root)

    topFrame = Frame(mainFrame)
    Label(text="MyCalcy", font=("arial", 50, "bold")).pack(side=TOP)
    entry = Entry(topFrame, fg="black", textvariable=v, bd=5, state="disabled")
    entry.pack(fill=X, ipady=10)
    topFrame.pack(side=TOP)


    bottomFrame = Frame(mainFrame)

    Button(bottomFrame, text=str(1), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("1")).grid(row=0, column=0)
    Button(bottomFrame, text=str(2), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("2")).grid(row=0, column=1)
    Button(bottomFrame, text=str(3), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("3")).grid(row=0, column=2)
    Button(bottomFrame, text=str(4), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("4")).grid(row=1, column=0)
    Button(bottomFrame, text=str(5), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("5")).grid(row=1, column=1)
    Button(bottomFrame, text=str(6), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("6")).grid(row=1, column=2)
    Button(bottomFrame, text=str(7), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("7")).grid(row=2, column=0)
    Button(bottomFrame, text=str(8), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("8")).grid(row=2, column=1)
    Button(bottomFrame, text=str(9), height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("9")).grid(row=2, column=2)



    Button(bottomFrame, text="+", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("+")).grid(row=0, column=3)
    Button(bottomFrame, text="-", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("-")).grid(row=1, column=3)
    Button(bottomFrame, text="*", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: takeValues("*")).grid(row=2, column=3)
    Button(bottomFrame, text="0", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command= lambda: takeValues("0")).grid(row=3, column=0)
    Button(bottomFrame, text="=", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command= lambda: calculate()).grid(row=3, column=1)
    Button(bottomFrame, text="C", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=lambda: clean()).grid(row=3, column=2)
    Button(bottomFrame, text="/", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command= lambda: takeValues("/")).grid(row=3, column=3)

    bottomFrame.pack(side=BOTTOM)

    statusBar = Frame(mainFrame)
    Message(text="Give a number, then operator, again number and click '=' to perform operation. Then later click 'C' to do new operation", relief=SUNKEN, anchor=W, width=1000).pack(side=BOTTOM, fill=X)
    statusBar.pack(side=BOTTOM)

    mainFrame.pack()

    root.mainloop()

if __name__ == '__main__':
    main()