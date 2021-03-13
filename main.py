import tkinter as tk
from tkinter import ttk

#define colors palette
c_black = "#0B0C10"
c_dark_grey = "#1F2833"
c_grey = "#C5C6C7"
c_light_blue = "#66FCF1"
c_turquoise = "#45A29E"

root = tk.Tk()
root.title('Sorting Algorithms Visualizer')
root.maxsize(900,600)
root.minsize(500,400)
root.config(bg=c_black,pady=5,padx=5)


ui_frame = tk.Frame(root, bg=c_dark_grey,width=500,height= 200)
ui_frame.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
ui_frame.grid_columnconfigure(0,weight=1)

def show_sorting_options():
    tk.Label(ui_frame,
        text="Wybierz algorytm:",
        foreground=c_black,  
        background=c_grey,  
    ).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    ;asndbaskdfas;l
    tk.Label(ui_frame,
        text="Ustaw prędkość:",
        foreground=c_black,  
        background=c_grey,  
        
    ).grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)




tk.Button(ui_frame,text="Sortowanie",bg =c_grey,fg=c_black,padx=5,pady=5,command=show_sorting_options).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
tk.Button(ui_frame,text="Całkowanie",bg =c_grey,fg=c_black,padx=5,pady=5,command=show_sorting_options).grid(row=0, column=1, padx=5, pady=5)
tk.Button(ui_frame,text="Miejsca zerowe",bg =c_grey,fg=c_black,padx=5,pady=5,command=show_sorting_options).grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)

root.mainloop()