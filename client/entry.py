import tkinter as tk
from tkinter import Widget, ttk
import time
from datetime import datetime
import calendar
from TrieTree import TrieTree

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', password = "no"):
        super().__init__(master)
        __BGENTRY = "#fafafa"
        __FGENTRY = "#494b59"
        self.__PASSWORD = password
         
        self.placeholder = placeholder
        self.placeholder_color = color
        self['fg'] = __FGENTRY
        self['bg'] = __BGENTRY
        self.default_fg_color = self['fg']

        self['font'] = "roboto 10 normal"
        self['highlightthickness'] = 1
        self.configure(highlightbackground="#c5c7d7", highlightcolor="#c5c7d7")
        

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
            if self.__PASSWORD == "yes":
                self['show'] = "*"

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

    def clear(self, *args):
        if self['fg'] == self.default_fg_color:
            self.delete('0', 'end')
            self.put_placeholder()
            if self.__PASSWORD == "yes":
                self['show'] = "*"
    def refocus(self):
        self.focus_set()
class EntryWithPickerDay(tk.Entry):
    def __init__(self, master=None, placeholder="dd/mm/yyyy", color='grey'):
        super().__init__(master)
        __BGENTRY = "#fafafa"
        __FGENTRY = "#494b59"
        
        self.placeholder = placeholder
        self.placeholder_color = color
        self['fg'] = __FGENTRY
        self['bg'] = __BGENTRY
        self.default_fg_color = self['fg']

        self['font'] = "roboto 10 normal"
        self['highlightthickness'] = 1
        self.configure(highlightbackground="#c5c7d7", highlightcolor="#c5c7d7")
        

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.initPicker(formatStr='%02d/%s/%s')

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

    def clear(self, *args):
        if self['fg'] == self.default_fg_color:
            self.delete('0', 'end')
            self.put_placeholder()

    def initPicker(self, widget=None, formatStr=None):
        self.picker = tk.Toplevel()
        self.widget = widget
        self.formatStr = formatStr
        self.picker.title("Date Picker")
        self.picker.resizable(width=False, height=False)
        self.picker.geometry("+630+390")
        self.initFrames()
        self.initNeededVars()
        self.initMonthYearLabels()
        self.initButtons()
        self.spaceBetweenWidgets()
        self.fillDays()
        self.makeCalendar()

    def initFrames(self):
        self.bgFrame = tk.Frame(self.picker)
        self.bgFrame.pack()
        self.frameDays = tk.Frame(self.picker)
        self.frameDays.pack()

    def initNeededVars(self):
        self.monthNames = tuple(calendar.month_name)
        self.dayNames = tuple(calendar.day_abbr)
        self.year = time.strftime("%Y")
        self.month = time.strftime("%B")

    def initMonthYearLabels(self):
        self.yearStr = tk.StringVar()
        self.monthStr = tk.StringVar()

        self.yearStr.set(self.year)
        self.yearLabel = tk.Label(self.bgFrame,
            textvariable=self.yearStr,
            width=3)
        self.yearLabel.grid(row=0, column=5)

        self.monthStr.set(self.month)
        self.monthLabel = tk.Label(self.bgFrame,
            textvariable=self.monthStr,
            width=8)
        self.monthLabel.grid(row=0, column=1)

    def initButtons(self):
        self.leftYearPointer = ttk.Button(self.bgFrame, text="←",
            width=5, command=self.prevYearFunc)
        self.leftYearPointer.grid(row=0, column=4)

        self.rightYearPointer = ttk.Button(self.bgFrame, text="→",
            width=5, command=self.nextYearFunc)
        self.rightYearPointer.grid(row=0, column=6)

        self.leftMonthPointer = ttk.Button(self.bgFrame, text="←",
            width=5, command=self.prevMonthFunc)
        self.leftMonthPointer.grid(row=0, column=0)

        self.rightMonthPointer = ttk.Button(self.bgFrame, text="→",
            width=5, command=self.nextMonthFunc)
        self.rightMonthPointer.grid(row=0, column=2)

    def spaceBetweenWidgets(self):
        self.bgFrame.grid_columnconfigure(3, minsize=40)
    
    def prevYearFunc(self):
        self.prevYear = int(self.yearStr.get()) - 1
        self.yearStr.set(self.prevYear)
    
        self.makeCalendar()
    
    def nextYearFunc(self):
        self.nextYear = int(self.yearStr.get()) + 1
        self.yearStr.set(self.nextYear)

        self.makeCalendar()

    def prevMonthFunc(self):
        idCurrentMonth = self.monthNames.index(self.monthStr.get())
        idPrevMonth = idCurrentMonth - 1

        if idPrevMonth == 0:
            self.monthStr.set(self.monthNames[12])
        else:
            self.monthStr.set(self.monthNames[idCurrentMonth - 1])
        
        self.makeCalendar()

    def nextMonthFunc(self):
        idCurrentMonth = self.monthNames.index(self.monthNames.get())

        try:
            self.monthStr.set(self.monthNames[idCurrentMonth + 1])
        except IndexError:
            self.monthStr.set(self.monthNames[1])

        self.makeCalendar()

    def fillDays(self):
        col = 0
        # creates days label
        for day in self.dayNames:
            self.dayLabels = tk.Label(self.frameDays, text=day)
            self.dayLabels.grid(row=0, column=col)
            col += 1

    def makeCalendar(self):
        # delete date buttons if already present
        # each button must have its own instance attribute for this to work
        try:
            for dates in self.monthCalendar:
                for date in dates:
                    if date == 0:
                        continue

                    self.deleteButton(date)
        except AttributeError:
            pass

        year = int(self.yearStr.get())
        month = self.monthNames.index(self.monthStr.get())
        self.monthCalendar = calendar.monthcalendar(year,month)
        
        #build dates button
        for dates in self.monthCalendar:
            row = self.monthCalendar.index(dates) + 1
            for date in dates:
                col = dates.index(date)

                if date == 0:
                    continue

                self.makeButton(str(date), str(row), str(col))

    def makeButton(self, date, row, column):
        exec(
            "self.btn_" + date + " = ttk.Button(self.frameDays, text=" + date + ", width=5)\n"
            "self.btn_" + date + ".grid(row=" + row + ", column=" + column + ")\n"
            "self.btn_" + date + ".bind(\"<Button-1>\", self.getDate)"
        )
    
    def deleteButton(self, date):
        exec(
            "self.btn_" + str(date) + ".destroy()"
        )

    def getDate(self, clicked=None):
        clickedButton = clicked.widget
        year = self.yearStr.get()
        month = self.monthNames.index(self.monthStr.get())
        date = clickedButton['text']

        self.full_date = self.cleanTime(self.formatStr % (date, month, year))
        self['fg'] = self.default_fg_color
        self.delete('0', 'end')
        self.insert(0, self.full_date)

        # replace with parent 'widget' of your choice
        try: 
            self.widget.delete(0, tk.END)
            self.widget.insert(0, self.full_date)
        except AttributeError:
            pass
    
    def cleanTime(self, dateStr):
        __format = "%d/%m/%Y"
        __dtObj = datetime.strptime(dateStr, __format) 
        return __dtObj.strftime(__format)


