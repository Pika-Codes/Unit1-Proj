#Credit To Mr. Miskew

from tkinter import *
from tkinter import filedialog


#1a2634
#203e5f
#eec550
#f9e3a3

#VARIABLES

#This list stores menu items using the format [day,food]

menuItems = []

days = [
        'Enter Day',
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday'
    ]
    
choices = [
    'Choose',
    'Meters',
    'Miles'
]


#FUNCTIONS

def print(*args):
    try:
        wb.open_new(r'C:/Users/will.finlayson/Desktop/Design/Python/calender.pdf')

    except:  
        callenr = open('calender.txt', 'r')
        callentest = callenr.readlines()
        callenr.close
        calt = open('calender.pdf','w')
        callenprint = str(callentest)
        calt.write(callenprint)
        calt.close()

def ezcal(*args):
    callenr = open('calender.txt', 'r')
    callentest = callenr.readlines()
    callenr.close
    "for f in callentest:"
        
def leavecal(*args):
    main.deiconify()
    cal.withdraw()
    days1.set('Enter Day')
    cale.delete(0, 'end')

def runMe(*args):
    print(cale.get())
    menuItems.append(days1.get())
    menuItems.append(cale.get())
    print(days1.get())
    print(menuItems)
    callen = open('calender.txt', 'a')
    callen.write(days1.get() + ':')
    callen.write(cale.get() + ', ')
    callen.close()
    callenr = open('calender.txt', 'r')
    callentest = callenr.readlines()
    callenr.close
    print(callentest)
    x = days1.get()
    print(x)
    y = cale.get()
    print(y)

    if x == 'Monday':
        day1f.config(text=y)
    elif x == 'Tuesday':
        day2f.config(text=y)
    elif x == 'Wednesday':
        day3f.config(text=y)
    elif x == 'Thursday':
        day4f.config(text=y)
    elif x == 'Friday':
        day5f.config(text=y)
    elif x == 'Saturday':
        day6f.config(text=y)
    elif x == 'Sunday':
        day7f.config(text=y)

def cal():
   cal.deiconify() #display cal
   main.withdraw() #hides main window

def test():
    print('yeet')


#BUILD MAIN WINDOW
main = Tk()
main.title('Prototype Beta')
main.geometry('400x150')
main.configure(background='#1a2634')

topframe = Frame(main, bg='#eec550', height='30')
topframe.grid()
can1 = Canvas(topframe,height='20',width='125',bg='#eec550',highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='#203e5f')
can1.create_line(0, 10, 20, 10,fill='#203e5f')
can1.create_line(0, 15, 20, 15,fill='#203e5f')
can1.bind('test',test )
bu1 = Button(topframe, text='Calender', highlightbackground='#eec550', command=cal)
inv1 = Label(topframe, text='                              ', bg='#eec550')
inv2 = Label(topframe, text='                              ', bg='#eec550')
can1.grid(row=0, column=0)
bu1.grid(row=0, column=1)
inv1.grid(row=0, column=2)
inv2.grid(row=0, column=3)
cal = Frame(main, bg='#203e5f', height='50', width='350')
cal.grid(row=1, column=0)


day1 = Label(cal, text='Monday', bg='#203e5f')
day2 = Label(cal, text='Tuesday', bg='#203e5f')
day3 = Label(cal, text='Wendsday', bg='#203e5f')
day4 = Label(cal, text='Thursday', bg='#203e5f')
day5 = Label(cal, text='Friday', bg='#203e5f')
day6 = Label(cal, text='Saturday', bg='#203e5f')
day7 = Label(cal, text='Sunday', bg='#203e5f')


day1.grid(row=0, column=0)
day2.grid(row=0, column=1)
day3.grid(row=0, column=2)
day4.grid(row=0, column=3)
day5.grid(row=0, column=4)
day6.grid(row=0, column=5)
day7.grid(row=0, column=6)

day1f = Label(cal, text='Food1', bg='#203e5f')
day2f = Label(cal, text='Food2', bg='#203e5f')
day3f = Label(cal, text='Food3', bg='#203e5f')
day4f = Label(cal, text='Food4', bg='#203e5f')
day5f = Label(cal, text='Food5', bg='#203e5f')
day6f = Label(cal, text='Food6', bg='#203e5f')
day7f = Label(cal, text='Food7', bg='#203e5f')

day1f.grid(row=1, column=0)
day2f.grid(row=1, column=1)
day3f.grid(row=1, column=2)
day4f.grid(row=1, column=3)
day5f.grid(row=1, column=4)
day6f.grid(row=1, column=5)
day7f.grid(row=1, column=6)

pr = Frame(main, bg='#203e5f', height='50', width='50')
pr.grid(row=3, column=0, pady=(10,0))
p1 = Button(pr, text='Print Calender', highlightbackground='#203e5f', command=print)
p1.grid(row=0, column=0)

#BUILD CALENDAR POPUP**********
cal = Tk()
cal.title('Calender')
cal.configure(background='#1a2634')

days1 = StringVar(cal)
days1.set('Enter Day')

calfr = Frame(cal, bg='#203e5f', height='50', width='50')
calfr.grid(row=0, column=0)

call = Label(calfr, text='Enter Food And Day', bg='#203e5f')
call.grid(row=0, column=0)

cald = OptionMenu(calfr, days1, *days)
cald.grid(row=1, column=0)

cale = Entry(calfr, highlightbackground='#203e5f')
cale.bind('<Return>', runMe)
cale.grid(row=2, column=0)
cal.bind('<Escape>', leavecal)


cal.withdraw() #This hides your window 
main.mainloop()
