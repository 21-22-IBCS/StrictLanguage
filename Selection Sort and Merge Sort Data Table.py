import time
import random

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1

def selectionSort(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.pop(li.index(minE))
        sortedList.append(minE)

    return sortedList
        
            


def main():
    l1 = []
    l2 = []
    l3 = [100,500,1000,5000,10000]
    ltotalS = []
    ltotalM = []
    for j in range(len(l3)):
        for i in range(l3[j]):
            l1.append(random.randint(1,100))
            l2.append(random.randint(1,100))

        start = time.time()
        result = selectionSort(l1)
        stop = time.time()
        totalSTime = stop - start
        ltotalS.append(round(totalSTime,5))


        start = time.time()
        mergeSort(l2)
        stop = time.time()
        totalMTime = stop - start
        ltotalM.append(round(totalMTime,5))

    print("----------------------------------------------------------------")    
    print("Lengths of the lists\t"+"Selection Sort Time\t"+"Merge Sort Time")
    print("----------------------------------------------------------------")
    for k in range(5):
        print(str(l3[k])+"\t\t\t"+str(ltotalS[k])+"\t\t\t"+str(ltotalM[k]))
        print("----------------------------------------------------------------")

        

if __name__ == "__main__":
    main()
