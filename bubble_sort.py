arr = [2,3,5,1,4]
n = len(arr)
for i in range (n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)