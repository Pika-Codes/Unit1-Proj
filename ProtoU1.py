from tkinter import *
from tkinter import filedialog

#1a2634
#203e5f
#eec550
#f9e3a3

main = Tk()
main.title('Prototype Alpha Doubble Prime')
main.geometry('500x350')
main.configure(background='#E5C99C')

def test():
    print('yeet')
    
topframe = Frame(main, bg='grey',height='30')
topframe.grid(row=0, column=0) # make as wide as main
can1 = Canvas(topframe,height='20',width='125',bg='gray',highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.bind('test',test )
bu1 = Button(topframe, text='Callender', highlightbackground='grey', command='test')
bu2 = Button(topframe, text='Add A Recepie', highlightbackground='grey', command='test')
bu3 = Button(topframe, text='Shopping List', highlightbackground='grey', command='test')
can1.grid(row=0, column=0)
bu1.grid(row=0, column=1)
bu2.grid(row=0, column=2)
bu3.grid(row=0, column=3, padx=(1, 130))

cal = Frame(main, bg='gray', height='50', width='350')
cal.grid(row=1, column=0)
day1 = Label(cal, text='Monday')
day2 = Label(cal, text='Tuesday')
day3 = Label(cal, text='Wendsday')
day4 = Label(cal, text='Thursday')
day5 = Label(cal, text='Friday')
day6 = Label(cal, text='Saturday')
day7 = Label(cal, text='Sunday')
day1.grid(row=0, column=0)
day2.grid(row=0, column=1)
day3.grid(row=0, column=2)
day4.grid(row=0, column=3)
day5.grid(row=0, column=4)
day6.grid(row=0, column=5)
day7.grid(row=0, column=6)

day1f = Label(cal, text='Food1')
day2f = Label(cal, text='Food2')
day3f = Label(cal, text='Food3')
day4f = Label(cal, text='Food4')
day5f = Label(cal, text='Food5')
day6f = Label(cal, text='Food6')
day7f = Label(cal, text='Food7')
day1f.grid(row=1, column=0)
day2f.grid(row=1, column=1)
day3f.grid(row=1, column=2)
day4f.grid(row=1, column=3)
day5f.grid(row=1, column=4)
day6f.grid(row=1, column=5)
day7f.grid(row=1, column=6)

units1 = StringVar(main)
units2 = StringVar(main)
choices = [
    'Choose',
    'Meters',
    'Miles'
]
units1.set('Choose')
units2.set('Choose')

otr = Frame(main, bg='gray', height='50', width='50')
otr.grid(row=2, column=0, pady=(10,0))
conl = Label(otr, text='Easy Converter')
con1 = OptionMenu(otr, units1, *choices)
con2 = OptionMenu(otr, units2, *choices)
conin1 = Entry(otr,)
conin2 = Entry(otr,)
conl.grid(row=0, column=0)
con1.grid(row=1, column=0)
con2.grid(row=1, column=1)
conin1.grid(row=2, column=0)
conin2.grid(row=2, column=1)

pr = Frame(main, bg='gray', height='50', width='50')
pr.grid(row=3, column=0, pady=(10,0))
p1 = Button(pr, text='Print Callender', highlightbackground='grey', command='test')
p2 = Button(pr, text='Print List', highlightbackground='grey', command='test')
p3 = Button(pr, text='Print Recipie', highlightbackground='grey'
            , command='test')
p1.grid(row=0, column=0)
p2.grid(row=1, column=0)
p3.grid(row=2, column=0)

rate = StringVar()

rd = Frame(main, bg='gray', height='50', width='50')
rd.grid(row=4, column=0, pady=(10,0))
la = Label(rd, text='How would you rate your most recent meal?')
r1 = Radiobutton(rd, text='1', variable=rate, value='1')
r2 = Radiobutton(rd, text='2', variable=rate, value='2')
r3 = Radiobutton(rd, text='3', variable=rate, value='3')
r4 = Radiobutton(rd, text='4', variable=rate, value='4')
r5 = Radiobutton(rd, text='5', variable=rate, value='5')
la.grid(row=0, column=0)
r1.grid(row=1, column=1)
r2.grid(row=1, column=2)
r3.grid(row=1, column=3)
r4.grid(row=1, column=4)
r5.grid(row=1, column=5)
