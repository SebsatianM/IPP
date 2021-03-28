from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import random

#define colors palette
c_black = "#0B0C10"
c_dark_grey = "#1F2833"
c_grey = "#C5C6C7"
c_light_blue = "#66FCF1"
c_turquoise = "#45A29E"

#Mainwindows settings
root = Tk()
root.title('Sorting Algorithms Visualizer')

root.maxsize(1200,1000)
root.minsize(600,500)
root_width = 500

"""
Function that create upper frame with 3 buttons
"""

def show_main_bar():

    btn_frame = Frame(root_frame,bg=c_dark_grey)

    s_btn = Button(btn_frame,text="Sortowanie",bg =c_grey,fg=c_black,pady=1,width= 5,command=show_sorting_options) 
    i_btn = Button(btn_frame,text="Całkowanie",bg =c_grey,fg=c_black,pady=1, width= 1,command=show_integration_options)
    r_btn = Button(btn_frame,text="Miejsca zerowe",bg =c_grey,fg=c_black,pady=1,width= 5,command=show_sorting_options)

    s_btn.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")
    i_btn.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
    r_btn.grid(row=0,column=2,padx=10,pady=10,sticky="nsew")
    
    btn_frame.grid_columnconfigure(0,weight=1)
    btn_frame.grid_columnconfigure(1,weight=1)
    btn_frame.grid_columnconfigure(2,weight=1)

    btn_frame.pack(fill="x")


"""
Function for destroying conetent of ui_frame when frame already exists and user change option 
"""
def destroy_frame():
    widget = root_frame.winfo_children()
    if len(widget)>1:
        widget[1].destroy()

    
"""
Function that show options frame with setting to sorting visualization part of program
"""

def show_sorting_options():

    f_col_pad_x= 5  #setting up size of gaps between buttons and sliders horizontally 
    pad_y = 1    #setting up size of gaps between buttons and sliders vertically 

    destroy_frame()
    ui_frame = Frame(root_frame,bg=c_dark_grey)

    Label(ui_frame,
        text="Wybierz algorytm:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=0, padx=(5,f_col_pad_x), pady=0, sticky="sew")

    type_combobox = ttk.Combobox(ui_frame,
        foreground=c_black,  
        background=c_grey,
        values=['Bubble Sort',
                'Selection Sort',
                'Insertion Sort',
                'Merge Sort',
                'Heap Sort',
                'Quick Sort'
            ],
        height=20,state="readonly")

    type_combobox.grid(row=1,column=0,padx=(5,f_col_pad_x), sticky="new")

    Label(ui_frame,
        text="Ustaw prędkość(s):",
        foreground=c_black,  
        background=c_grey).grid(row=2, column=0, padx=(5,f_col_pad_x), pady=0, sticky="sew")

    speed_scale = Scale(ui_frame,
        foreground=c_black,  
        background=c_grey,
        from_=float(0.0),
        to=float(5.0),
        orient = HORIZONTAL, 
        resolution=0.01)

    speed_scale.grid(row=3, column=0, padx=(5,f_col_pad_x), pady=0, sticky="new")

    Label(ui_frame,
        text="Rozmiar tablicy:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=1, padx=(5,f_col_pad_x), pady=(pad_y,0), sticky="sew")

    size_scale = Scale(ui_frame,
        foreground=c_black,  
        background=c_grey,
        from_=0,
        to= 100,
        orient = HORIZONTAL, 
        resolution=1)

    size_scale.grid(row=1, column=1, padx=(5,f_col_pad_x), pady=0, sticky="new") 
          
    Label(ui_frame,
        text="Minimalna warotść:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=2, padx=(5,f_col_pad_x), pady=(pad_y,0), sticky="nsew")

    min_val_scale = Scale(ui_frame,
        foreground=c_black,  
        background=c_grey,
        from_= 0,
        to= 99,
        orient = HORIZONTAL, 
        resolution=1)       

    min_val_scale.grid(row=1, column=2, padx=(5,f_col_pad_x), pady=0, sticky="nsew")

    Label(ui_frame,
        text="Maksymalna warotść:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=3, padx=(5,f_col_pad_x), pady=(pad_y,0), sticky="nsew")

    max_val_scale = Scale(ui_frame,
        foreground=c_black,  
        background=c_grey,
        from_= 0,
        to= 100,
        orient = HORIZONTAL, 
        resolution=1)

    max_val_scale.grid(row=1, column=3, padx=(5,f_col_pad_x), pady=0, sticky="nsew")        

    generate_button = Button(ui_frame,text="Generuj",bg =c_grey,fg=c_black,pady=1,width= 15,command=generate)
    load_button = Button(ui_frame,text="Importuj dane",bg =c_grey,fg=c_black,pady=1,width= 15,command=imoprt_data)
    start_button = Button(ui_frame,text="Start",bg =c_grey,fg=c_black,pady=1,width= 15,command=show_sorting_options)
    

    generate_button.grid(row=3,column=1,columnspan=3, padx=(f_col_pad_x,0), pady=10, sticky="nsw")
    load_button.grid(row=3,column=1,columnspan=3, padx=(10,10), pady=10, sticky="ns")
    start_button.grid(row=3,column=1,columnspan=3, padx=(0,f_col_pad_x+10), pady=10, sticky="nse")
    

    ui_frame.grid_columnconfigure(0,weight=1)
    ui_frame.grid_columnconfigure(1,weight=1)
    ui_frame.grid_columnconfigure(2,weight=1)
    ui_frame.grid_columnconfigure(3,weight=1)

    
    ui_frame.pack(fill="x")

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
    print('Wybrany algorymt ' + type_combobox.get())
    try:
        minVal = int(min_val_scale.get())
    except:
        minVal = 1
    try:
        maxVal = int(max_val_scale.get())
    except:
        maxVal = 10
    try:
        size = int(size_scale.get())
    except:
        size = 10

    if minVal < 0 : minVal = 0
    if maxVal > 100 : maxVal = 100
    if size > 30 or size < 3: size = 30
    if minVal > maxVal : minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    for x in range(len(data)):
        print(data[x])

"""
Function that show options frame with setting to integrate visualization part of program
"""  
def show_integration_options():
    destroy_frame()
    ui_frame = Frame(root_frame,bg=c_dark_grey)
    Label(ui_frame,
        text="Wybierz całkę:",
        foreground=c_black,  
        background=c_grey,  
    ).grid(row=2, column=0, padx=5, pady=5, sticky=W)
    Label(ui_frame,
        text="Wybierz metodę:",
        foreground=c_black,  
        background=c_grey).grid(row=3, column=0, padx=5, pady=5, sticky=W)
        
    ui_frame.pack(fill="x")

def width_info(event):
    root.update()
    global root_width
    if root_width!=root.winfo_width():
        root_width=root.winfo_width()

   
if __name__ == "__main__":
    
    #creating main frame on main window analogue of main div in html
    root_frame=Frame(root,bg=c_black)
    root_frame.pack(fill="both",expand=True)   
    
    show_main_bar()

    
    root.mainloop()
    