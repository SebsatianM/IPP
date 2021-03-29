from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import random
import drawing




"""
Reading and filtering data from file 
"""
def imoprt_data():
    tf = fd.askopenfilename(
        initialdir="C:/dev/IPP", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )

    f = open(tf,'r')
    file_stuff= f.read()

    data_instring=""

    for line in file_stuff:
        data_instring+=line.replace("\n"," ").replace(","," ").replace(";"," ")  #creating one string from all user inserted data and separate everythig with space if its not letter or digit

    data_all = [int(number) for number in data_instring.split() if number.lstrip('-').isdigit()]    #filtering string for find only digit inside and append it to list named data

    data_to_low = [number for number in data_all if number < 1] 
    data = [number for number in data_all if number in range(1,100) ]
    data_to_high = [number for number in data_all if number >= 100]



def generate():
    print('Wybrany algorymt ' + drawing.type_combobox.get())
    try:
        minVal = int(drawing.min_val_scale.get())
    except:
        minVal = 1
    try:
        maxVal = int(drawing.max_val_scale.get())
    except:
        maxVal = 10
    try:
        size = int(drawing.size_scale.get())
    except:
        size = 10

    if minVal < 0 : minVal = 0
    if maxVal < 10 : maxVal = 10
    if maxVal > 100 : maxVal = 100
    if size > 30 or size < 3: size = 30
    if minVal > maxVal : minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    print(len(data))
    for x in range(len(data)):
        print(data[x])


   
if __name__ == "__main__":
    
    #creating main frame on main window analogue of main div in html
    drawing.init()
    drawing.show_main_bar()

    
    drawing.root.mainloop()
    