from tkinter import *
from tkinter import ttk

#define colors palette
c_black = "#0B0C10"
c_dark_grey = "#1F2833"
c_grey = "#C5C6C7"
c_light_blue = "#66FCF1"
c_turquoise = "#45A29E"

#Mainwindows settings
root = Tk()
root.title('Sorting Algorithms Visualizer')

root.maxsize(900,600)
root.minsize(500,400)


"""
Function that create upper frame with 3 buttons
"""

def show_main_bar():

    btn_frame = Frame(root_frame,bg=c_dark_grey)

    s_btn = Button(btn_frame,text="Sortowanie",bg =c_grey,fg=c_black,pady=1,width= 5,command=show_sorting_options) 
    i_btn = Button(btn_frame,text="Całkowanie",bg =c_grey,fg=c_black,pady=1, width= 1,command=show_integration_options)
    r_btn = Button(btn_frame,text="Miejsca zerowe",bg =c_grey,fg=c_black,pady=1,width= 5,command=show_sorting_options)

    i_btn.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")
    r_btn.grid(row=0,column=2,padx=10,pady=10,sticky="nsew")
    s_btn.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

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
    destroy_frame()
    ui_frame = Frame(root_frame,bg=c_dark_grey,width=500)

    Label(ui_frame,
        text="Wybierz algorytm:",
        foreground=c_black,  
        background=c_grey,
        width= 15
    ).grid(row=1, column=0, padx=5, pady=0, sticky=W)

    ttk.Combobox(ui_frame,
        foreground=c_black,  
        background=c_grey,
        values=['Bubble Sort',
                'Selection Sort',
                'Insertion Sort',
                'Merge Sort',
                'Heap Sort',
                'Quick Sort'
            ],
        width=14
    ).grid(row=2,column=0,padx=5)

    Label(ui_frame,
        text="Ustaw prędkość(s):",
        foreground=c_black,  
        background=c_grey,
        width=15).grid(row=3, column=0, padx=5, pady=(5,0), sticky=W)

    Scale(ui_frame,
        foreground=c_black,  
        background=c_grey,
        from_=float(0.0),
        to=float(5.0),
        orient = HORIZONTAL, 
        resolution=0.01
        
    ).grid(row=4, column=0, padx=5, pady=0, sticky=W)
    ui_frame.pack(fill="x")


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


if __name__ == "__main__":
    
    #creating main frame on main window analogue of main div in html
    root_frame=Frame(root,bg=c_black)
    root_frame.pack(fill="both",expand=True)   
    
    show_main_bar() 


    root.mainloop()
