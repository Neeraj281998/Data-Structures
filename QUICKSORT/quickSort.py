class QuickSort:
    def __init__(self,data):
        self.data=data

    def sort(self):
        self.quicksort(0,len(self.data)-1)


    #Low is  the First index of the item
    #High is the last index of the item
    def quicksort(self,low,high):
        if low>=high:
            return

        pivot_index=self.partition(low,high)
        # calling the function recursively on the left array

        self.quicksort(low,pivot_index-1)
        self.quicksort(pivot_index+1,high)

    def partition(self,low,high):

        # middel item of the array
        pivot_index=(low+high)//2

        self.data[pivot_index],self.data[high]=self.data[pivot_index],self.data[high]

        #conside all the items and compare them with the pivot
        for j in range(low,high):
            if self.data[j]<=self.data[high]:
                self.data[low],self.data[j]=self.data[j],self.data[low]
                low=low+1

        #we have considered all the items -we have to swap the pivot and the low 
        self.data[low],self.data[high]=self.data[high],self.data[low]

        return low


if __name__=='__main__':
    x=[-1,100,23,45,1,2,12,-12,-23]
    QuickAlgo=QuickSort(x)
    QuickAlgo.sort()
    print(x)