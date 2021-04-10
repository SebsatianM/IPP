from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
from colors import *
import random
import drawing
import alghoritms_base
import time

data = []
data_to_low = []
data_to_high = []
width_stack = [800]
height_stack = [400]
speed_stack = [0.0]

"""
alghoritms_dict = {'Bubble Sort':alghoritms_base.bubble_sort, 
                'Selection Sort':selection_sort,  
                'Insertion Sort':alghoritms_base,
                'Merge Sort':alghoritms_base,
                'Heap Sort':alghoritms_base,
                'Quick Sort':alghoritms_base}

"""

alghoritms_dict = {'Bubble Sort':alghoritms_base.bubble_sort('Bubble Sort'),
                    'Selection Sort':alghoritms_base.selection_sort('Selection Sort'),
                    'Insertion Sort':alghoritms_base.insertion_sort('Insertion Sort'),}

#Reading and filtering data from file 
def imoprt_data():
    global data,data_to_low,data_to_high

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
    Draw_data(data,[c_light_blue for i in range(0,len(data)+1)])
    
#Checking actual window width and height
def get_width_and_height():
    drawing.root.update()
    return drawing.root.winfo_width()-14,drawing.root.winfo_height()-181

#Drawing data
def Draw_data(data, colorArray,f_call_counter=[0]):
    
    f_call_counter[0]+=1 #mutable variable are evaluated only once

    if f_call_counter[0] % 5 == 0:
        width_stack.pop()
        height_stack.pop()
        speed_stack.pop()
        width_pom,height_pom = get_width_and_height()
        speed = drawing.speed_scale.get()
        speed_stack.append(speed)
        width_stack.append(width_pom)
        height_stack.append(height_pom)
    time.sleep(speed_stack[0])

    drawing.canvas.delete("all")
    x_width = width_stack[0] / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = height_stack[0] - height * (height_stack[0]-10)
        x1 = (i + 1) * x_width + offset
        y1 = height_stack[0]
        drawing.canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    drawing.canvas.update()

#Generating random numbers depends on user choice
def generate_data():
    global data
    data.clear()
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

    if minVal == 0 and maxVal ==0 and size == 0:
        data = [i for i in range(0,101)] #creating list from 0 to 100
        random.shuffle(data)    #shuffle that list
        Draw_data(data,[c_light_blue for i in range(0,101)])
    else:
        if minVal < 0 : minVal = 0
        if maxVal < 10 : maxVal = 10
        if maxVal > 100 : maxVal = 100
        if size > 100 or size < 3: size = 80
        if minVal > maxVal : minVal, maxVal = maxVal, minVal


        for _ in range(size):
            data.append(random.randrange(minVal, maxVal+1))
        
        Draw_data(data,[c_light_blue for i in range(0,len(data))])


def start():
    alg_type = drawing.type_combobox.get()
    obj = alghoritms_dict.get(alg_type)
    try:
        obj.add_data(data,data_to_low,data_to_high)
    except:
        print("dupa") 

    obj.sorting()
    
    
if __name__ == "__main__":
    #creating main frame on main window analogue of main div in html
    drawing.init()

    drawing.show_main_bar()
    
    drawing.root.mainloop()

    