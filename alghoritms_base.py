import main
import time
from colors import *
from random import shuffle
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

    def heapify(self, n, i,sorted_idx):

        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.data[i] < self.data[left]:
            largest = left
        if right < n and self.data[largest] < self.data[right]:
            largest = right
        if largest != i:

            if self.data[-1] != max(self.data):
                sorted_idx = len(self.data)+1

            self.update([c_red if x == i else c_orange if x == largest else c_green if x == sorted_idx else c_turquoise if x < sorted_idx else c_light_blue for x in range(len(self.data))])
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.update([c_red if x == i else c_orange if x == largest else c_green if x== sorted_idx else c_turquoise if x < sorted_idx else c_light_blue for x in range(len(self.data))])
            self.heapify(n, largest,sorted_idx)

    def sorting(self):
        n = len(self.data)
        for i in range(n,-1,-1):
            self.heapify(n, i, i)

        for i in range(n-1,0,-1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0, i)
            self.update([c_light_blue if x >= i else c_turquoise for x in range(len(self.data))])

        self.check()


class quick_sort(Algorithm):
    def __init__(self,name):
        super().__init__(name)

    def sorting(self):
        self.QuickSort(0,len(self.data)-1)
        self.check()

    def QuickSort(self,l,r):
        if l>=r:
            return
        self.update([c_turquoise if x >=l and x <= r else c_light_blue for x in range(len(self.data))])
        p = self.partition(l,r)

        self.QuickSort(l,p-1)
        self.QuickSort(p+1,r)
        
    def partition(self,l,r):
        pivot = self.data[r]
        i = l - 1
        for j in range(l,r):
            self.update([c_turquoise if x >= l and x <r else c_orange if x == r else c_red if x==j else c_light_blue for x in range(len(self.data))])
            if self.data[j] < pivot:
                i+=1
                c_turquoise_list = [x for x in range(l,r) if x!=j and x!=i]
                self.update([c_turquoise if x in c_turquoise_list else c_orange if x == r else c_red if x==j or x==i else c_light_blue for x in range(len(self.data))])
                self.data[i],self.data[j] = self.data[j],self.data[i]
                self.update([c_turquoise if x in c_turquoise_list else c_orange if x == r else c_red if x==j or x==i else c_light_blue for x in range(len(self.data))])

        self.data[i+1],self.data[r] = self.data[r], self.data[i+1]
        
        return i+1


class tim_sort(Algorithm):
    def __init__(self,name):
        super().__init__("Tim Sort")

        self.MIN_MERGE = 32
 
    def calcMinRun(self):

        n = len(self.data)
        r = 0
        while n >= self.MIN_MERGE:
            r |= n & 1
            n >>= 1
        return n + r
        
    def insertion_sort_for_timsort(self,left=0,right=None):

        if right is None:
            right = len(self.data)-1
        
        for i in range(left+1,right+1):
            key_item = self.data[i]
            j = i-1

            while j>= left and self.data[j]>key_item:
                c_turquoise_list = [x for x in range(left,right) if x!=i and x!=j]
                self.data[j+1] = self.data[j]

                self.update([c_turquoise if x in c_turquoise_list else c_orange if x==i or x==j else c_light_blue for x in range(len(self.data))])
                j-=1
            self.data[j+1] = key_item
        
    def tim_merge(self,left,right,first_left_idx,first_right_idx):

        if len(left) == 0:
            return right

        if len(right) == 0:
            return left
        
        result = []
        index_left = index_right = 0
        while len(result) < len(left) + len(right):

            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                self.update([c_orange if x == first_left_idx+index_left else c_turquoise if x>=first_left_idx and x<=first_right_idx+len(left) else c_light_blue for x in range(len(self.data))])
                index_left += 1
                
            else:
                result.append(right[index_right])
                self.update([c_orange if x == first_right_idx+index_right else c_turquoise if x>=first_left_idx and x<=first_right_idx+len(left) else c_light_blue for x in range(len(self.data))])
                index_right += 1

            if index_right == len(right):
                result += left[index_left:]
                break

            if index_left == len(left):
                result += right[index_right:]
                break
            
        return result

    def sorting(self):
        min_run = self.calcMinRun()
        n = len(self.data)
        for i in range(0,n,min_run):
            self.insertion_sort_for_timsort(i,min((i+min_run-1),n-1))
        
        size = min_run
        while size <= n:
            for start in range(0,n,size*2):
                mid = start+size -1
                end = min((start+size*2 -1),(n-1))
                merged_array = self.tim_merge(left=self.data[start:mid + 1],right=self.data[mid + 1:end + 1],first_left_idx=start,first_right_idx=mid + 1)
                self.data[start:start + len(merged_array)] = merged_array
            
        
       
            size *= 2
        self.update([c_light_blue for x in range(len(self.data))])
<<<<<<< HEAD


=======
        
class comb_sort(Algorithm):
    def ___init__(self,name):
        super().__init__(name)

    def calcGap(self,gap):
        gap = (gap * 10)//13
        if gap < 1:
            return 1
        return gap
    
    def sorting(self):
        length = len(self.data)

        gap = length
        swapped = True

        while gap != 1 or swapped == True:
            gap = self.calcGap(gap)

            swapped = False
            for i in range(0,length-gap):
                self.update([c_turquoise if x == i or x==i+gap else c_light_blue for x in range(length)])
                if self.data[i] > self.data[i+gap]:
                    self.update([c_orange if x == i or x==i+gap else c_light_blue for x in range(length)])
                    self.data[i],self.data[i+gap] = self.data[i+gap],self.data[i]
                    self.update([c_green if x == i or x==i+gap else c_light_blue for x in range(length)])
                    swapped = True
                self.update([c_green if x == i or x==i+gap else c_light_blue for x in range(length)])
        
        self.check()


class coctail_sort(Algorithm):
    def __init__(self, name):
        super().__init__(name)

    def sorting(self):
        length = len(self.data)
        swapped = True
        start = 0
        end = length-1
        while (swapped==True):
    
            swapped = False
    

            for i in range (start, end):
                self.update([c_turquoise if x == i or x==i+1 else c_light_blue for x in range(length)])
                if (self.data[i] > self.data[i+1]):
                    self.update([c_orange if x == i or x==i+1 else c_light_blue for x in range(length)])
                    self.data[i], self.data[i+1] = self.data[i+1], self.data[i]
                    self.update([c_green if x == i or x==i+1 else c_light_blue for x in range(length)])
                    swapped=True
    
            if (swapped==False):
                break
    
            swapped = False
    
            end = end-1
    
            for i in range(end-1, start-1,-1):
                self.update([c_turquoise if x == i or x==i+1 else c_light_blue for x in range(length)])
                if (self.data[i] > self.data[i+1]):
                    self.update([c_orange if x == i or x==i+1 else c_light_blue for x in range(length)])
                    self.data[i], self.data[i+1] = self.data[i+1], self.data[i]
                    self.update([c_green if x == i or x==i+1 else c_light_blue for x in range(length)])
                    swapped = True
    
            start = start+1
        self.check()
>>>>>>> fourth_raport
if __name__ == "__main__":

    meh = tim_sort("")
    data =[x for x in range(0,128)]
    shuffle(data)
    meh.add_data(data)
    
    meh.print_values()
    meh.sorting()
    meh.print_values()


