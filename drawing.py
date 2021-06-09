from tkinter import *
from tkinter import ttk
from colors import *
import main

#Mainwindows settings
root = Tk()
root.title('Sorting Algorithms Visualizer')

root.maxsize(1920,1080)
root.minsize(600,400)
#Function that create upper frame with 3 buttons
def init():
    global root_frame

    root_frame=Frame(root,bg=c_black)
    root_frame.pack(fill="both",expand=True)   

def show_main_bar():
    btn_frame = Frame(root_frame,bg=c_dark_grey)

    s_btn = Button(btn_frame,text="Sortowanie",bg =c_grey,fg=c_black,width= 5,command=show_sorting_options) 
    r_btn = Button(btn_frame,text="Informacje o algorytmach",bg =c_grey,fg=c_black,width= 5,command=show_sorting_info)

    s_btn.grid(row=0,column=0,padx=(30,5),pady=5,sticky="nsew")
    r_btn.grid(row=0,column=2,padx=(5,30),pady=5,sticky="nsew")
    
    btn_frame.grid_columnconfigure(0,weight=1)
    btn_frame.grid_columnconfigure(1,weight=1)
    btn_frame.grid_columnconfigure(2,weight=1)

    btn_frame.pack(fill="x")

#Function for destroying conetent of ui_frame when frame already exists and user change option 
def destroy_frame():
    widget = root_frame.winfo_children()
    if len(widget)>1:
        widget[1].destroy()


#Function that show options frame with setting to sorting visualization part of program
def show_sorting_options():
    global type_combobox,speed_scale,size_scale,min_val_scale,max_val_scale,canvas,ui_frame
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
        values=[x for x in list(main.alghoritms_dict.keys())],
        height=20,state="readonly")
    type_combobox.current(0)
    type_combobox.grid(row=1,column=0,padx=(5,f_col_pad_x), sticky="new")

    Label(ui_frame,
        text="Ustaw prędkość(s):",
        foreground=c_black,  
        background=c_grey).grid(row=2, column=0, padx=(5,f_col_pad_x), pady=0, sticky="sew")

    speed_scale = Scale(ui_frame,
        foreground=c_black,  
        background=c_grey,
        from_=float(0.0),
        to=float(1.0),
        orient = HORIZONTAL, 
        resolution=0.005)

    speed_scale.grid(row=3, column=0, padx=(5,f_col_pad_x), pady=0, sticky="new")

    Label(ui_frame,
        text="Rozmiar tablicy:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=1, padx=(5,f_col_pad_x), pady=(pad_y,0), sticky="sew")

    size_scale = Scale(ui_frame,
        foreground=c_black,  
        background=c_grey,
        from_=0,
        to= 120,
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

    generate_button = Button(ui_frame,text="Generuj",bg =c_grey,fg=c_black,pady=1,width= 15,command=main.generate_data)
    load_button = Button(ui_frame,text="Importuj dane",bg =c_grey,fg=c_black,pady=1,width= 15,command=main.imoprt_data)
    start_button = Button(ui_frame,text="Start",bg =c_grey,fg=c_black,pady=1,width= 15,command=main.start)
    
    generate_button.grid(row=3,column=1,columnspan=3, padx=(f_col_pad_x,0), pady=10, sticky="nsw")
    load_button.grid(row=3,column=1,columnspan=3, padx=(10,10), pady=10, sticky="ns")
    start_button.grid(row=3,column=1,columnspan=3, padx=(0,f_col_pad_x+10), pady=10, sticky="nse")

    ui_frame.grid_columnconfigure(0,weight=1)
    ui_frame.grid_columnconfigure(1,weight=1)
    ui_frame.grid_columnconfigure(2,weight=1)
    ui_frame.grid_columnconfigure(3,weight=1)
    ui_frame.grid_rowconfigure(4,weight= 1)

    canvas = Canvas(ui_frame, width=800, height=400, bg=c_grey)
    canvas.grid(row=4, column=0, padx=5, pady=5,columnspan=4,sticky="news")
    
    ui_frame.pack(fill="both",expand=True)



#Function that show options frame with setting to integrate visualization part of program
def show_sorting_info():
    global type_combobox2,Best_time_label_Text,Avg_time_label_Text,Worst_time_label_Text,Space_label_Text,Description_label_Text
    f_col_pad_x= 5  #setting up size of gaps between buttons and sliders horizontally 
    pad_y = 3    #setting up size of gaps between buttons and sliders vertically 

    destroy_frame()
    ui_frame = Frame(root_frame,bg=c_dark_grey)
    root_frame.configure(background=c_dark_grey)

    
    Label(ui_frame,
        text="Wybierz algorytm:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=0, padx=(5,f_col_pad_x), pady=0, sticky="sew")

    type_combobox2 = ttk.Combobox(ui_frame,
        foreground=c_black,  
        background=c_grey,
        values=[x for x in list(main.alghoritms_dict.keys())],
        height=20,state="readonly")
    type_combobox2.current(0)
    type_combobox2.grid(row=1,column=0,padx=(5,f_col_pad_x),pady=(pad_y,0), sticky="new")
    type_combobox2.bind('<<ComboboxSelected>>', changed_alghorithm)  

    Label(ui_frame,
        text="Złożoność czasowa:",
        foreground=c_black,  
        background=c_grey).grid(row=2, column=0, padx=(5,f_col_pad_x), pady=(pad_y*5,0), sticky="new")

    Label(ui_frame,
        text="Najlepsza:",
        foreground=c_black,  
        background=c_grey).grid(row=3, column=0, padx=(5,f_col_pad_x), pady=(pad_y,0), sticky="new")

    Best_time_label_Text = StringVar(value="")

    Label(ui_frame,textvariable=Best_time_label_Text,
        foreground=c_black,  
        background=c_white).grid(row=4,column=0, padx=(5,f_col_pad_x),pady=(0,pad_y), sticky="new")

    Label(ui_frame,
        text="Średnia:",
        foreground=c_black,  
        background=c_grey).grid(row=5, column=0, padx=(5,f_col_pad_x), pady=(pad_y,0), sticky="new")

    Avg_time_label_Text = StringVar(value="")

    Label(ui_frame,textvariable=Avg_time_label_Text,
        foreground=c_black,  
        background=c_white).grid(row=6,column=0, padx=(5,f_col_pad_x),pady=(0,pad_y), sticky="new")

    Label(ui_frame,
        text="Najgorsza:",
        foreground=c_black,  
        background=c_grey).grid(row=7, column=0, padx=(5,f_col_pad_x), pady=(pad_y,0), sticky="nesw")

    Worst_time_label_Text = StringVar(value="")

    Label(ui_frame,textvariable=Worst_time_label_Text,
        foreground=c_black,  
        background=c_white).grid(row=8,column=0, padx=(5,f_col_pad_x),pady=(0,pad_y), sticky="new")

    Label(ui_frame,
        text="Złożoność pamięciowa:",
        foreground=c_black,  
        background=c_grey).grid(row=9, column=0, padx=(5,f_col_pad_x), pady=(pad_y*5,0), sticky="new")

    Space_label_Text = StringVar(value="")

    Label(ui_frame,textvariable=Space_label_Text,
        foreground=c_black,  
        background=c_white).grid(row=10,column=0, padx=(5,f_col_pad_x),pady=(0,pad_y), sticky="new")

    Label(ui_frame,
        text="Opis algorytmu:",
        foreground=c_black,  
        background=c_grey).grid(row=0, column=1, columnspan=6, padx=(f_col_pad_x*2,f_col_pad_x), pady=(pad_y*5,0), sticky="new")

    Description_label_Text = StringVar(value="")

    Label(ui_frame,textvariable=Description_label_Text,
        foreground=c_black,  
        background=c_white,wraplength=300, justify="center",
        font="helvetica 11").grid(row=1,column=1, columnspan=6,rowspan=10, padx=(f_col_pad_x*2,f_col_pad_x),pady=(0,pad_y), sticky="nesw")

    ui_frame.grid_columnconfigure(0,weight=1)
    ui_frame.grid_columnconfigure(1,weight=1)
    ui_frame.grid_columnconfigure(2,weight=1)
    ui_frame.grid_columnconfigure(3,weight=1)

        
    ui_frame.pack(fill="both",expand=True)

def changed_alghorithm(event):
    alghoritm_type = type_combobox2.get()

    for key,value in main.alghoritms_dict.items():
        if key == alghoritm_type:
            information = value.show_info()

    
    Best_time_label_Text.set(information[0])
    Avg_time_label_Text.set(information[1])
    Worst_time_label_Text.set(information[2])
    Space_label_Text.set(information[3])
    Description_label_Text.set(information[4])

    