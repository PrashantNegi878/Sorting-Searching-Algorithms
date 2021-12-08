def binarysearch(arr,l,r,x):
    mid=(l+r)//2
    if arr[mid]==x:
        print(f"Element {x} is at Index {mid}")
        return
    elif arr[mid]<x:
        binarysearch(arr,mid+1,r,x)
    elif arr[mid]>x:
        binarysearch(arr,l,mid-1,x)


arr=[1,4,5,6,8,10,15]
binarysearch(arr,0,9,6)



