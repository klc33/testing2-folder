def SelectionSort(myList):
    
    for i in range(len(myList)-1):
        
        min_index = i
        
        for j in range(i,len(myList)-1):
            
            if myList[min_index]>=myList[j+1]:
                
                min_index = j+1
        
        
        temp = myList[i]
        myList[i] = myList[min_index]
        myList[min_index] = temp
    
    return myList

        













myList = [2,1,3,6,5,4,7,8,9]

print(SelectionSort(myList))