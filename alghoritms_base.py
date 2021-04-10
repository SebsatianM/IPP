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
        
        
        
class bubble_sort(Algorithm):
    def __init__(self,name):
        super().__init__('Bubble Sort')

    def sorting(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n-1-i):
                #self.update(self.data,[c_turquoise if i == j or i==j+1 else c_light_blue for i in range(0,len(self.data))])
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
        
                    self.update(self.data,[c_turquoise if i == j else c_green if i==j+1 else c_light_blue for i in range(0,len(self.data))]) 
                else:
                    self.update(self.data,[c_green if i == j else c_turquoise if i==j+1 else c_light_blue for i in range(0,len(self.data))])         
                


   

if __name__ == "__main__":
    meh = bubble_sort("")
    meh.add_data([1,3,4,5])
    meh.alghoritm()


