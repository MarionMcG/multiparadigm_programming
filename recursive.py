
#Sum of an array (Recursive)
def sum_(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0] + sum_(arr[1:]) 

#Product of an array (Recursive)
def product(arr):
    if len(arr)==0:
        return 1
    else:
        return arr[0]*(product(arr[1:])) 

arr2 = []
#Remove Odd numbers (Recursive but only works with an intenal print statement)
def odd_out(arr):  
    if len(arr) == 0:
        print(arr2)
        #return arr2 
    else:
        if arr[0] % 2 == 0:
            arr2.append(arr[0]) 
            odd_out(arr[1:])
        else:
            odd_out(arr[1:])

#Remove Even numbers
def even_out(arr):
    if len(arr) == 0:
        print(arr2)
        return arr2  
    else:
        if arr[0]%2!=0:
            arr2.append(arr[0]) 
            even_out(arr[1:])
        else:
            even_out(arr[1:])

new_arr = []
def replace_char(arr):
    if len(arr)==0:
        return 0
    else:
        new_arr.append(arr[0].replace('o', '*'))
        replace_char(arr[1:])

    return new_arr


def searc_ndex(arr):
    #if len(arr)==0:
        #return 
    #else:
        index = 0
        for index, j in enumerate(arr):
            if j == 2:
                print(index)
            else: 
                index = index +1
                searc_ndex(arr)


def search_ndex(arr):
    i = -1
    if len(arr ==0):
        return i
    else:
        index = 0
        for index, j in enumerate(arr):
            if j == 2:
                i = j
            else: 
                index = index +1
                searc_ndex(arr)

           

            


a = [1, 2, 4, 5, 3]
print('Array: ', a)
print('Sum of the Array: ',sum_(a))
print('Product of the Array: ', product(a))
odd_out(a)

del arr2
arr2=[]

even_out(a)

b = ['hello', 'world']
#print(b)
print(replace_char(b))
searc_ndex(a)