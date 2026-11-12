from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background = 'white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()

txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),
                   bg='black',fg='white',
                   bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,
                          bg='black',fg='white',
                          font=('Helvetica',20,'bold'),
                          bd=4,text=numberpad[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1
      
btnClear = Button(calc, text=chr(67),width=6,
                  height=2,bg='powder blue',
                  font=('Helvetica',20,'bold')
                  ,bd=4, command=added_value.Clear_Entry
                 ).grid(row=1, column= 0, pady = 1)

btnAllClear = Button(calc, text=chr(67)+chr(69),
                     width=6, height=2,
                     bg='powder blue', 
                     font=('Helvetica',20,'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                    ).grid(row=1, column= 1, pady = 1)

btnsq = Button(calc, text="\u221A",width=6, height=2,
               bg='powder blue', font=('Helvetica',
                                       20,'bold'),
               bd=4,command=added_value.squared
              ).grid(row=1, column= 2, pady = 1)

btnAdd = Button(calc, text="+",width=6, height=2,
                bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("add")
                ).grid(row=1, column= 3, pady = 1)

btnSub = Button(calc, text="-",width=6,
                height=2,bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("sub")
                ).grid(row=2, column= 3, pady = 1)

btnMul = Button(calc, text="x",width=6, 
                height=2,bg='powder blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("multi")
                ).grid(row=3, column= 3, pady = 1)

btnDiv = Button(calc, text="/",width=6, 
                height=2,bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("divide")
                ).grid(row=4, column= 3, pady = 1)

btnZero = Button(calc, text="0",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=lambda:added_value.numberEnter(0)
                 ).grid(row=5, column= 0, pady = 1)

btnDot = Button(calc, text=".",width=6,
                height=2,bg='powder blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.numberEnter(".")
                ).grid(row=5, column= 1, pady = 1)
btnPM = Button(calc, text=chr(177),width=6, 
               height=2,bg='powder blue', font=('Helvetica',20,'bold'),
               bd=4,command=added_value.mathPM
              ).grid(row=5, column= 2, pady = 1)

btnEquals = Button(calc, text="=",width=6,
                   height=2,bg='powder blue',
                   font=('Helvetica',20,'bold'),
                   bd=4,command=added_value.sum_of_total
                  ).grid(row=5, column= 3, pady = 1)
# ROW 1 :
btnPi = Button(calc, text="pi",width=6,
               height=2,bg='black',fg='white', 
               font=('Helvetica',20,'bold'),
               bd=4,command=added_value.pi
              ).grid(row=1, column= 4, pady = 1)

btnCos = Button(calc, text="Cos",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.cos
               ).grid(row=1, column= 5, pady = 1)

btntan = Button(calc, text="tan",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.tan
               ).grid(row=1, column= 6, pady = 1)

btnsin = Button(calc, text="sin",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.sin
               ).grid(row=1, column= 7, pady = 1)

# ROW 2 :
btn2Pi = Button(calc, text="2pi",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.tau
               ).grid(row=2, column= 4, pady = 1)

btnCosh = Button(calc, text="Cosh",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.cosh
                ).grid(row=2, column= 5, pady = 1)

btntanh = Button(calc, text="tanh",width=6, 
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.tanh
                ).grid(row=2, column= 6, pady = 1)

btnsinh = Button(calc, text="sinh",width=6, 
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.sinh
                ).grid(row=2, column= 7, pady = 1)

# ROW 3 :
btnlog = Button(calc, text="log",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.log
               ).grid(row=3, column= 4, pady = 1)

btnExp = Button(calc, text="exp",width=6, height=2,
                bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.exp
               ).grid(row=3, column= 5, pady = 1)

btnMod = Button(calc, text="Mod",width=6,
                height=2,bg='black',fg='white', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("mod")
                ).grid(row=3, column= 6, pady = 1)

btnE   = Button(calc, text="e",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.e
               ).grid(row=3, column= 7, pady = 1)

# ROW 4 :
btnlog10 = Button(calc, text="log10",width=6, 
                  height=2,bg='black',fg='white', 
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log10
                 ).grid(row=4, column= 4, pady = 1)

btncos   = Button(calc, text="log1p",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log1p
                 ).grid(row=4, column= 5, pady = 1)

btnexpm1 = Button(calc, text="expm1",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd = 4,command=added_value.expm1
                 ).grid(row=4, column= 6, pady = 1)

btngamma = Button(calc, text="gamma",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.lgamma
                 ).grid(row=4, column= 7, pady = 1)
# ROW 5 :
btnlog2 = Button(calc, text="log2",width=6, 
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.log2
                ).grid(row=5, column= 4, pady = 1)

btndeg = Button(calc, text="deg",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.degrees
               ).grid(row=5, column= 5, pady = 1)

btnacosh = Button(calc, text="acosh",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.acosh
                 ).grid(row=5, column= 6, pady = 1)

btnasinh = Button(calc, text="asinh",width=6, 
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.asinh
                 ).grid(row=5, column= 7, pady = 1)

lblDisplay = Label(calc, text = "Scientific Calculator",
                   font=('Helvetica',30,'bold'),
                   bg='black',fg='white',justify=CENTER)

lblDisplay.grid(row=0, column= 4,columnspan=4)

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

# ManuBar 2 :
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

root.config(menu=menubar)

root.mainloop()
# import all functions from the tkinter   
from tkinter import *

# import messagebox class from tkinter
from tkinter import messagebox

# Function for clearing the  
# contents of all text entry boxes
def clearAll() :

    # deleting the content from the entry box
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)

# function for checking error
def checkError() :

    # if any of the entry field is empty
    # then show an error message and clear 
    # all the entries
    if (dayField.get() == "" or monthField.get() == ""
        or yearField.get() == "" or givenDayField.get() == ""
        or givenMonthField.get() == "" or givenYearField.get() == "") :

        # show the error message
        messagebox.showerror("Input Error")

        # clearAll function calling
        clearAll()
        
        return -1

# function to calculate Age 
def calculateAge() :

    # check for error
    value = checkError()

    # if error is occur then return
    if value ==  -1 :
        return
    
    else :
        
        # take a value from the respective entry boxes
        # get method returns current text as string
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())
        
        
        # if birth date is greater then given birth_month 
        # then donot count this month and add 30 to the date so 
        # as to subtract the date and get the remaining days 
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1] 
                    
                    # i
        # if birth month exceeds given month, then 
        # donot count this year and add 12 to the 
        # month so that we can subtract and find out 
        # the difference 
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
                    
        # calculate day, month, year 
        calculated_day = given_day - birth_day; 
        calculated_month = given_month - birth_month; 
        calculated_year = given_year - birth_year;

        # calculated day, month, year write back
        # to the respective entry boxes

        # insert method inserting the  
        # value in the text entry box.
        
        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))
    

# Driver Code
if __name__ == "__main__" :

    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window  
    gui.configure(background = "light green")

    # set the name of tkinter GUI window 
    gui.title("Age Calculator")

     # Set the configuration of GUI window
    gui.geometry("525x260")

    # Create a Date Of Birth : label 
    dob = Label(gui, text = "Date Of Birth", bg = "blue")

    # Create a Given Date : label
    givenDate = Label(gui, text = "Given Date", bg = "blue")

    # Create a Day : label
    day = Label(gui, text = "Day", bg = "light green")

    # Create a Month : label
    month = Label(gui, text = "Month", bg = "light green")

    # Create a Year : label
    year = Label(gui, text = "Year", bg = "light green")

    # Create a Given Day : label
    givenDay = Label(gui, text = "Given Day", bg = "light green")

    # Create a Given Month : label
    givenMonth = Label(gui, text = "Given Month", bg = "light green")

    # Create a Given Year : label
    givenYear = Label(gui, text = "Given Year", bg = "light green")

    # Create a Years : label
    rsltYear = Label(gui, text = "Years", bg = "light green")

    # Create a Months : label
    rsltMonth = Label(gui, text = "Months", bg = "light green")

    # Create a Days : label
    rsltDay = Label(gui, text = "Days", bg = "light green")

    # Create a Resultant Age Button and attached to calculateAge function
    resultantAge = Button(gui, text = "Resultant Age", fg = "Black", bg = "Red", command = calculateAge)

    # Create a Clear All Button and attached to clearAll function
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)

    # Create a text entry box for filling or typing the information.  
    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)
    
    givenDayField = Entry(gui)
    givenMonthField = Entry(gui)
    givenYearField = Entry(gui)
    
    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)


    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure .
    dob.grid(row = 0, column = 1)
    
    day.grid(row = 1, column = 0)
    dayField.grid(row = 1, column = 1)
    
    month.grid(row = 2, column = 0)
    monthField.grid(row = 2, column = 1)
    
    year.grid(row = 3, column = 0)
    yearField.grid(row = 3, column = 1)
    
    givenDate.grid(row = 0, column = 4)
    
    givenDay.grid(row = 1, column = 3)
    givenDayField.grid(row = 1, column = 4)
    
    givenMonth.grid(row = 2, column = 3)
    givenMonthField.grid(row = 2, column = 4)
    
    givenYear.grid(row = 3, column = 3)
    givenYearField.grid(row = 3, column = 4)
    
    resultantAge.grid(row = 4, column = 2)
    
    rsltYear.grid(row = 5, column = 2)
    rsltYearField.grid(row = 6, column = 2)
    
    rsltMonth.grid(row = 7, column = 2)
    rsltMonthField.grid(row = 8, column = 2)
    
    rsltDay.grid(row = 9, column = 2)
    rsltDayField.grid(row = 10, column = 2)

    clearAllEntry.grid(row = 12, column = 2)

    # Start the GUI
    gui.mainloop()
   # Import tkinter
from tkinter import *
class LoanCalculator:

    def __init__(self):

        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title
        # create the input boxes.
        Label(window, text = "Annual Interest Rate").grid(row = 1,
                                          column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2,
                                      column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3,
                                  column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4,
                                      column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5,
                                    column = 1, sticky = W)

        # for taking inputs
        self.annualInterestRateVar = StringVar() 
        Entry(window, textvariable = self.annualInterestRateVar,
                     justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()

        Entry(window, textvariable = self.numberOfYearsVar,
                 justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()

        Entry(window, textvariable = self.loanAmountVar,
              justify = RIGHT).grid(row = 3, column = 2)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
                           self.monthlyPaymentVar).grid(row = 4,
                           column = 2, sticky = E)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = 
                       self.totalPaymentVar).grid(row = 5,
                       column = 2, sticky = E)
        
        # create the button
        btComputePayment = Button(window, text = "Compute Payment",
                                  command = self.computePayment).grid(
                                  row = 6, column = 2, sticky = E) 
        window.mainloop() # Create an event loop


    # compute the total payment.
    def computePayment(self):
                
        monthlyPayment = self.getMonthlyPayment(
        float(self.loanAmountVar.get()),
        float(self.annualInterestRateVar.get()) / 1200,
        int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                                * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears): 
        # compute the monthly payment.
        monthlyPayment = loanAmount * monthlyInterestRate / (1
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
        root = Tk() # create the widget

 # call the class to run the program.
LoanCalculator()
from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background = 'white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def pi(self):
        self.result =  False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()

txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),
                   bg='black',fg='white',
                   bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,
                          bg='black',fg='white',
                          font=('Helvetica',20,'bold'),
                          bd=4,text=numberpad[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1
      
btnClear = Button(calc, text=chr(67),width=6,
                  height=2,bg='powder blue',
                  font=('Helvetica',20,'bold')
                  ,bd=4, command=added_value.Clear_Entry
                 ).grid(row=1, column= 0, pady = 1)

btnAllClear = Button(calc, text=chr(67)+chr(69),
                     width=6, height=2,
                     bg='powder blue', 
                     font=('Helvetica',20,'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                    ).grid(row=1, column= 1, pady = 1)

btnsq = Button(calc, text="\u221A",width=6, height=2,
               bg='powder blue', font=('Helvetica',
                                       20,'bold'),
               bd=4,command=added_value.squared
              ).grid(row=1, column= 2, pady = 1)

btnAdd = Button(calc, text="+",width=6, height=2,
                bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("add")
                ).grid(row=1, column= 3, pady = 1)

btnSub = Button(calc, text="-",width=6,
                height=2,bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("sub")
                ).grid(row=2, column= 3, pady = 1)

btnMul = Button(calc, text="x",width=6, 
                height=2,bg='powder blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("multi")
                ).grid(row=3, column= 3, pady = 1)

btnDiv = Button(calc, text="/",width=6, 
                height=2,bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("divide")
                ).grid(row=4, column= 3, pady = 1)

btnZero = Button(calc, text="0",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=lambda:added_value.numberEnter(0)
                 ).grid(row=5, column= 0, pady = 1)

btnDot = Button(calc, text=".",width=6,
                height=2,bg='powder blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.numberEnter(".")
                ).grid(row=5, column= 1, pady = 1)
btnPM = Button(calc, text=chr(177),width=6, 
               height=2,bg='powder blue', font=('Helvetica',20,'bold'),
               bd=4,command=added_value.mathPM
              ).grid(row=5, column= 2, pady = 1)

btnEquals = Button(calc, text="=",width=6,
                   height=2,bg='powder blue',
                   font=('Helvetica',20,'bold'),
                   bd=4,command=added_value.sum_of_total
                  ).grid(row=5, column= 3, pady = 1)
# ROW 1 :
btnPi = Button(calc, text="pi",width=6,
               height=2,bg='black',fg='white', 
               font=('Helvetica',20,'bold'),
               bd=4,command=added_value.pi
              ).grid(row=1, column= 4, pady = 1)

btnCos = Button(calc, text="Cos",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.cos
               ).grid(row=1, column= 5, pady = 1)

btntan = Button(calc, text="tan",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.tan
               ).grid(row=1, column= 6, pady = 1)

btnsin = Button(calc, text="sin",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.sin
               ).grid(row=1, column= 7, pady = 1)

# ROW 2 :
btn2Pi = Button(calc, text="2pi",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.tau
               ).grid(row=2, column= 4, pady = 1)

btnCosh = Button(calc, text="Cosh",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.cosh
                ).grid(row=2, column= 5, pady = 1)

btntanh = Button(calc, text="tanh",width=6, 
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.tanh
                ).grid(row=2, column= 6, pady = 1)

btnsinh = Button(calc, text="sinh",width=6, 
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.sinh
                ).grid(row=2, column= 7, pady = 1)

# ROW 3 :
btnlog = Button(calc, text="log",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.log
               ).grid(row=3, column= 4, pady = 1)

btnExp = Button(calc, text="exp",width=6, height=2,
                bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.exp
               ).grid(row=3, column= 5, pady = 1)

btnMod = Button(calc, text="Mod",width=6,
                height=2,bg='black',fg='white', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("mod")
                ).grid(row=3, column= 6, pady = 1)

btnE   = Button(calc, text="e",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.e
               ).grid(row=3, column= 7, pady = 1)

# ROW 4 :
btnlog10 = Button(calc, text="log10",width=6, 
                  height=2,bg='black',fg='white', 
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log10
                 ).grid(row=4, column= 4, pady = 1)

btncos   = Button(calc, text="log1p",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.log1p
                 ).grid(row=4, column= 5, pady = 1)

btnexpm1 = Button(calc, text="expm1",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd = 4,command=added_value.expm1
                 ).grid(row=4, column= 6, pady = 1)

btngamma = Button(calc, text="gamma",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.lgamma
                 ).grid(row=4, column= 7, pady = 1)
# ROW 5 :
btnlog2 = Button(calc, text="log2",width=6, 
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=added_value.log2
                ).grid(row=5, column= 4, pady = 1)

btndeg = Button(calc, text="deg",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.degrees
               ).grid(row=5, column= 5, pady = 1)

btnacosh = Button(calc, text="acosh",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.acosh
                 ).grid(row=5, column= 6, pady = 1)

btnasinh = Button(calc, text="asinh",width=6, 
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=added_value.asinh
                 ).grid(row=5, column= 7, pady = 1)

lblDisplay = Label(calc, text = "Scientific Calculator",
                   font=('Helvetica',30,'bold'),
                   bg='black',fg='white',justify=CENTER)

lblDisplay.grid(row=0, column= 4,columnspan=4)

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit ?")
    if iExit>0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

# ManuBar 2 :
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

root.config(menu=menubar)

root.mainloop()
import tkinter as tk
from tkinter import *
import tkinter.messagebox

def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates # pyright: ignore[reportMissingImports]
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if Amount1_field.get() == "":
        tkinter.messagebox.showinfo("Error", "Amount Not Entered.\nPlease enter a valid amount.")
    elif from_currency == "currency" or to_currency == "currency":
        tkinter.messagebox.showinfo("Error", "Currency Not Selected.\nPlease select both currencies.")
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))

def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Currency Converter - GeeksforGeeks")
root.configure(background='#e6e5e5')
root.geometry("700x400")

# Frame and labels
Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'),
                     text='Currency Converter : GeeksforGeeks',
                     bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
variable1.set("currency")
variable2.set("currency")

# Currency list
CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

# UI Elements
Label(root, font=('lato black', 15, 'bold'), text="\tAmount:", bg="#e6e5e5", fg="black").grid(row=2, column=0, sticky=W)
Label(root, font=('lato black', 15, 'bold'), text="\tFrom Currency:", bg="#e6e5e5", fg="black").grid(row=3, column=0, sticky=W)
Label(root, font=('lato black', 15, 'bold'), text="\tTo Currency:", bg="#e6e5e5", fg="black").grid(row=4, column=0, sticky=W)
Label(root, font=('lato black', 15, 'bold'), text="\tConverted Amount:", bg="#e6e5e5", fg="black").grid(row=8, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrencyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrencyCode_list)
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount2_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Button(root, font=('arial', 15, 'bold'), text="Convert", padx=2, pady=2,
       bg="lightblue", fg="white", command=RealTimeCurrencyConversion).grid(row=6, column=0)

Button(root, font=('arial', 15, 'bold'), text="Clear All", padx=2, pady=2,
       bg="lightblue", fg="white", command=clear_all).grid(row=10, column=0)

root.mainloop()
