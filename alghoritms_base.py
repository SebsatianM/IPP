import main
import time
from colors import *
class Algorithm:
    def __init__(self, name):
         self.name = name

    def add_data(self,data,data_to_low=None,data_to_high=None):
        self.data = data
        self.data_to_low = data_to_low
        self.data_to_high = data_to_high
    
    def print_values(self):
        print(self.name)
        print(self.data)
        print(self.data_to_low)
        print(self.data_to_high)

    def update(self,data,colorArray,swap1=None,swap2=None):
        main.Draw_data(self.data,colorArray)
        
    def check(self):
        for i in range(len(self.data)-1):
            if self.data[i] < self.data[i+1]:
                main.Draw_data(self.data,[c_green if i >= x else c_light_blue for x in range(len(self.data))])
        main.Draw_data(self.data,[c_green for x in range(len(self.data))])
        
class bubble_sort(Algorithm):
    def __init__(self,name):
        super().__init__('Bubble Sort')

    def sorting(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n-1-i):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
                    self.update(self.data,[c_turquoise if x == j else c_green if x==j+1 else c_light_blue for x in range(n)]) 
                else:
                    self.update(self.data,[c_green if x == j else c_turquoise if x==j+1 else c_light_blue for x in range(n)])         
        self.check()
class selection_sort(Algorithm):
    def __init__(self,name):
        super().__init__('Selection Sort')
    def sorting(self):
        n = len(self.data)
        for i in range(n):
            min_val_idx = i
            for j in range(i+1,n):  
                if self.data[min_val_idx]>self.data[j]:
                    self.update(self.data,[c_turquoise  if x == i else c_green if x==j else c_light_blue for x in range(n)])
                    min_val_idx = j
                else:
                    self.update(self.data,[c_green if x == i else c_turquoise if x==j else c_light_blue for x in range(n)])
            
            self.data[i],self.data[min_val_idx] = self.data[min_val_idx],self.data[i]
        self.check()




   

if __name__ == "__main__":
    meh = bubble_sort("")
    meh.add_data([1,3,4,5])
    meh.alghoritm()


