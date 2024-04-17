def linear_search(list1,target):
    found=False
    for i in range (len(l)):
        if list1[i]==target and not found:
          print("Element ",target,"found at index",i,".")
          
    if target!=list1[i]:
        print("Element is not present in List.")
    
l=[3,4,6,2,8,1,99]
print(l)
linear_search(l,5)
        