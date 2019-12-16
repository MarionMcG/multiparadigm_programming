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
#Remove Odd numbers
def odd_out(arr):  
    if len(arr) == 0:

        return arr2 
    else:
        if arr[0] % 2 == 0:
            arr2.append(arr[0]) 
            return odd_out(arr[1:])
        else:
            return odd_out(arr[1:])

#Remove Even numbers
def even_out(arr):
    if len(arr) == 0:
        return arr2  
    else:
        if arr[0]%2!=0:
            arr2.append(arr[0]) 
            return even_out(arr[1:])
        else:
            return even_out(arr[1:])


new_arr = []
def replace_char(arr):
    if len(arr)==0:
        return 0
    else:
        new_arr.append(arr[0].replace('o', '*'))
        replace_char(arr[1:])
    return new_arr

def searc_ndex(arr, inte, loc = 0):
    while  len(arr) > 0:
        if inte not in arr:
            return -1
        elif arr[loc] == inte:
            return loc
        else:
            return searc_ndex(arr, inte, loc+1)

def sum_digits(inte, sum_=0):
    if inte == 0:
        return sum_
    else:
        digit = inte % 10 #gives value of digit in the tens position
        sum_ += digit #add to sum
        inte //= 10 #inte is now the value in the hundreds position
        return sum_digits(inte, sum_)
     
def print_array(arr):
    if len(arr)==0:
        return 0
    else:
        print(arr[0])
        print_array(arr[1:])

def min_value(arr):
    if len(arr)==0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[1] < arr[0]:
            return (min_value(arr[1:]))
        else:
            arr[1]=arr[0]
            return (min_value(arr[1:]))

            
a = [1, 2, 4, -36, 5, 3]
print('Array A: ', a)
b = ['hello', 'world']
print('Array B: ', b)
print('-----------------------')
print('Sum of Array A: ',sum_(a))
print('Product of Array A: ', product(a))
print('-----------------------')
print('Array A without odd numbers', odd_out(a))

del arr2
arr2=[]

print('Array A without even numbers', even_out(a))
print('-----------------------')
print('Array B, replacing char o with * , ',replace_char(b))
print('-----------------------')
print('In Array A the number 2 is at index ',searc_ndex(a, 2))
print('-----------------------')
print('The sum of the digits of 78 is ', sum_digits(78))
print('-----------------------')
print('Printing every value in Array A, each on a new line')
print_array(a)
print('-----------------------')
print('Minimum value in Array A: ',min_value(a))
print('-----------------------')