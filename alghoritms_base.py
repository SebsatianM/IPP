
class Algorithm:
    def __init__(self, name):
         self.name = name

    def add_data(self,data,data_to_low=None,data_to_high=None):
        self.data = data
        self.data_to_low = data_to_low
        self.data_to_high = data_to_high

    def update(self,swap1=None,swap2=None):
        pass
        
class bubble_sort(Algorithm):
    def __init__(self,name):
        super().__init__('Bubble Sort')
    def alghoritm(self):
        print(self.name)
        print(self.data)
        print(self.data_to_low)
        print(self.data_to_high)

if __name__ == "__main__":
    meh = bubble_sort("")
    meh.add_data([1,3,4,5])
    meh.alghoritm()


