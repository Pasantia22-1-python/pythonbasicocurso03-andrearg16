import random

def binary_serch(data,target,low,high):
    if low > high:
        return False
    
    mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_serch(data,target,low,mid -1)
    else:
        return binary_serch(data,target,mid + 1, high)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]
    data.sort()
    print(data)

    target = int(input('What number would you like to fiend?'))
    found = binary_serch(data,target,0,len(data) -1)
    print(found)