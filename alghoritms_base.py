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

    def update(self,colorArray,swap1=None,swap2=None):
        main.Draw_data(self.data,colorArray)
        
    def check(self):
        passed = True
        for i in range(len(self.data)-1):
            if self.data[i] <= self.data[i+1]:
                main.Draw_data(self.data,[c_green if i >= x else c_light_blue for x in range(len(self.data))])
            else:
                passed = False
                main.Draw_data(self.data,[c_red if i >= x else c_light_blue for x in range(len(self.data))])
        if passed:
            main.Draw_data(self.data,[c_green for x in range(len(self.data))])
        else:
            main.Draw_data(self.data,[c_red for x in range(len(self.data))])

        
class bubble_sort(Algorithm):
    def __init__(self,name):
        super().__init__('Bubble Sort')

    def sorting(self):
        n = len(self.data)
        for i in range(n):
            for j in range(n-1-i):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
                    self.update([c_turquoise if x == j else c_green if x==j+1 else c_light_blue for x in range(n)]) 
                else:
                    self.update([c_green if x == j else c_turquoise if x==j+1 else c_light_blue for x in range(n)])         
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
                    self.update([c_turquoise if x == i else c_green if x==j else c_light_blue for x in range(n)])
                    min_val_idx = j
                else:
                    self.update([c_green if x == i else c_turquoise if x==j else c_light_blue for x in range(n)])

            self.data[i],self.data[min_val_idx] = self.data[min_val_idx],self.data[i]

        self.check()


class insertion_sort(Algorithm):
    def __init_(self,name):
        super().__init__('Insertion Sort')

    def sorting(self):
        n = len(self.data)
        for i in range(1,n):
            key = self.data[i]
            idx = i
            self.update([c_turquoise if x == i-1 or x==i else c_orange if x==idx else c_light_blue for x in range(n)])
            while self.data[i-1] > key and i>0:
                self.data[i],self.data[i-1] = self.data[i-1],self.data[i]
                self.update([c_turquoise if x == i-1 or x==i else c_orange if x==idx else c_light_blue for x in range(n)])
                i-=1
         

        self.check()

class merge_sort(Algorithm):
    def __init__(self,name):
        super().__init__('Merge Sort')   

    def sorting(self):
        self.alg(0,len(self.data)-1)
        self.check()

    def alg(self,left,right):
        if left < right:
            center = (left+right)//2
            self.alg(left,center)
            self.alg(center+1,right)
            self.merge(left, center ,right)

    def merge(self,left,center,right):

        self.update(self.get_clr(left,center,right))

        left_part = self.data[left:center+1]
        right_part = self.data[center+1:right+1]

        l_idx = r_idx = 0
        
        for_loop_range = len(left_part)+len(right_part)
        
        for x in range(for_loop_range//2):
            left_red_square_idx = center - (len(left_part) - x)+1
            right_part_red_square_idx = center+x+1
            checking_values_indexes = [*range(center-len(left_part)+1,center+len(right_part)+1)]
        
            self.update([c_turquoise if y in checking_values_indexes and y != left_red_square_idx else c_red if y == left_red_square_idx else c_light_blue for y in range(len(self.data))])
            self.update([c_turquoise if y in checking_values_indexes and y != right_part_red_square_idx else c_red if y == right_part_red_square_idx else c_light_blue for y in range(len(self.data))])
         
        for idx in range(left,right+1):
            
            if l_idx < len(left_part) and r_idx < len(right_part):
            
                if left_part[l_idx]<= right_part[r_idx]:
                    self.data[idx] = left_part[l_idx]
                    l_idx+=1

                else:
                    self.data[idx] = right_part[r_idx]
                    r_idx+=1

                pom = self.data.index(self.data[idx])  
                colorArray = self.get_clr(left,pom,right)
                colorArray[idx] = c_orange
                self.update(colorArray)
                
            elif l_idx < len(left_part):
                self.data[idx] = left_part[l_idx]
                l_idx+=1
            else:
                self.data[idx] = right_part[r_idx]
                r_idx+=1
                    
        
        self.update([c_green if x>= left and x<= right else c_light_blue for x in range(len(self.data))])
        
    def get_clr(self,left,center,right):
        colorArray = []

        for i in range(len(self.data)):
            if i>= left and i<=right:
                if i>= left and i<=center:
                    colorArray.append(c_turquoise)
                else:
                    colorArray.append(c_turquoise)
            else:
                colorArray.append(c_light_blue)

        return colorArray
            

class heap_sort(Algorithm):
    def __init_(self,name):
        super().__init__('Heap Sort')

    def sorting(self):
        n = len(self.data)
        for i in range(1,n):
            key = self.data[i]
            idx = i
            self.update([c_turquoise if x == i-1 or x==i else c_orange if x==idx else c_light_blue for x in range(n)])
            while self.data[i-1] > key and i>0:
                self.data[i],self.data[i-1] = self.data[i-1],self.data[i]
                self.update([c_turquoise if x == i-1 or x==i else c_orange if x==idx else c_light_blue for x in range(n)])
                i-=1
         

        self.check()        

if __name__ == "__main__":

    meh = merge_sort("")
    meh.add_data([1,2,5,7,1,3,7,9,13,4,87,8,0,3,213,12])
 
    meh.print_values()
    meh.sorting()
    meh.print_values()


