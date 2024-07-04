from tkinter import *

window = Tk()
window.title("Calculator")
i = 0

#Entry
textEntry = Entry(window, font = ("calibri 20"))
textEntry.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)

#Functions

def buttonClick(value):
    global i
    textEntry.insert(i, value)
    i += 1

def clear():
    textEntry.delete(0, END)
    i = 0
    
def operations():
    operation = textEntry.get()
    result = eval(operation)
    textEntry.delete (0, END)
    textEntry.insert(0, result)
    i = 0

#Buttons

button1 = Button(window, text = "1", width = 5, height = 2, command = lambda: buttonClick(1) )
button2 = Button(window, text = "2", width = 5, height = 2, command = lambda: buttonClick(2) )
button3 = Button(window, text = "3", width = 5, height = 2, command = lambda: buttonClick(3) )
button4 = Button(window, text = "4", width = 5, height = 2, command = lambda: buttonClick(4) )
button5 = Button(window, text = "5", width = 5, height = 2, command = lambda: buttonClick(5) )
button6 = Button(window, text = "6", width = 5, height = 2, command = lambda: buttonClick(6))
button7 = Button(window, text = "7", width = 5, height = 2, command = lambda: buttonClick(7) )
button8 = Button(window, text = "8", width = 5, height = 2, command = lambda: buttonClick(8) )
button9 = Button(window, text = "9", width = 5, height = 2, command = lambda: buttonClick(9) )
button0 = Button(window, text = "0", width = 19, height = 2, command = lambda: buttonClick(0) )

buttonClear = Button(window, text = "AC", width = 5, height = 2, command = lambda: clear() )
buttonParenthesis1 = Button(window, text = "(", width = 5, height = 2, command = lambda: buttonClick("(") )
buttonParenthesis2 = Button(window, text = ")", width = 5, height = 2, command = lambda: buttonClick(")") )
buttonPoint = Button(window, text = ".", width = 5, height = 2, command = lambda: buttonClick(".") )

buttonDivision = Button(window, text = "/", width = 5, height = 2, command = lambda: buttonClick("/") )
buttonMultiply = Button(window, text = "*", width = 5, height = 2, command = lambda: buttonClick("*") )
buttonPlus = Button(window, text = "+", width = 5, height = 2, command = lambda: buttonClick("+") )
buttonMinus = Button(window, text = "-", width = 5, height = 2, command = lambda: buttonClick("-") )
buttonEquals = Button(window, text = "=", width = 5, height = 2, command = lambda: operations() )

#Buttons Location

button1.grid(row = 1, column = 0, padx = 5, pady = 5)
button2.grid(row = 1, column = 1, padx = 5, pady = 5)
button3.grid(row = 1, column = 2, padx = 5, pady = 5)
button4.grid(row = 2, column = 0, padx = 5, pady = 5)
button5.grid(row = 2, column = 1, padx = 5, pady = 5)
button6.grid(row = 2, column = 2, padx = 5, pady = 5)
button7.grid(row = 3, column = 0, padx = 5, pady = 5)
button8.grid(row = 3, column = 1, padx = 5, pady = 5)
button9.grid(row = 3, column = 2, padx = 5, pady = 5)
button0.grid(row = 4, column = 0 , columnspan = 2, padx = 5, pady = 5)

buttonClear.grid(row = 5, column = 0, padx = 5, pady = 5)
buttonParenthesis1.grid(row = 5, column = 1, padx = 5, pady = 5)
buttonParenthesis2.grid(row = 5, column = 2, padx = 5, pady = 5)
buttonPoint.grid(row = 4, column = 2, padx = 5, pady = 5)

buttonDivision.grid(row = 3, column = 3, padx = 5, pady = 5)
buttonMultiply.grid(row = 4, column = 3, padx = 5, pady = 5)
buttonPlus.grid(row = 1, column = 3, padx = 5, pady = 5)
buttonMinus.grid(row = 2, column = 3, padx = 5, pady = 5)
buttonEquals.grid(row = 5, column = 3, padx = 5, pady = 5)

window.mainloop()
