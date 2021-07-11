# Maximum and minimum of an array using minimum number of comparisons
# Difficulty Level : Easy
# Date : 11th July, 2021
def main(arr):
    if len(arr)==1:
        print("Min=",arr[0])
        print("Max=",arr[0])
    else:
        max = arr[0]
        min = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>max:
                max = arr[i]
            if arr[i]<min:
                min = arr[i]
        print("Max=",max)
        print("Min=",min)
arr = [2,4,62,5,2,56]
main(arr)