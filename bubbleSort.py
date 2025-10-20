def bubbleSort(myList):
    
    for i in range(len(myList)-1):
        
        for j in range(len(myList)-i-1):
            
            if myList[j]>=myList[j+1]:
                
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
                
    
    
    return myList

        













myList = [2,1,3,6,5,4,7,8,9]

print(bubbleSort(myList))