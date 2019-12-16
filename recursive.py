#_____Sum of an array (Recursive)_____
def sum_(arr):
    #if the array is empty then the sum is zero
    #So when I finish my loop, my answer is added to zero
    if len(arr)==0: 
        return 0
    #Recursive loop --> add the first term to the sum of the rest
    else:
        return arr[0] + sum_(arr[1:]) 

#_____Product of an array (Recursive)_____
def product(arr):
    #if the array is empty, return 1
    #So when I finish my loop, my answer is multipled by 1
    if len(arr)==0:
        return 1
    #Recursive loop --> multiply the first term by the product of the rest
    else:
        return arr[0]*(product(arr[1:])) 


arr2 = []
#_____Remove Odd numbers_____
def odd_out(arr):  
    #if arr is empty, return empty array
    #and if my loop is finished return arr2
    if len(arr) == 0:
        return arr2 
    else:
        if arr[0] % 2 == 0: #if the first term is divided evenly by2
            arr2.append(arr[0])  #add the term to arr2
            return odd_out(arr[1:]) #loop through the rest of the array
        else:
            return odd_out(arr[1:]) #if not divisable by 2, continue to loop through array

#_____Remove Even numbers_____
def even_out(arr):
    #if arr is empty, return empty array
    #and if my loop is finished return arr2
    if len(arr) == 0:
        return arr2  
    else:
        if arr[0]%2!=0: #if the first term is not divisible by 2
            arr2.append(arr[0])  #append to arr2
            return even_out(arr[1:]) #loop through rest of array
        else:
            return even_out(arr[1:]) #if it is divisible, continue loop through array


new_arr = []
#_____Replace a character with * _____
def replace_char(arr):
    #if arr is empty, return empty array
    if len(arr)==0:
        return new_arr
    else:
        new_arr.append(arr[0].replace('o', '*')) #first string of array letter o replace with *, append to new_arr
        replace_char(arr[1:]) #Continue to loop through the array of strings
    return new_arr

#_____Return Index of a Value_____
#Three parameters --> arr (the array), inte (the integer/string we're looking for), and loc is the index
def searc_ndex(arr, inte, loc = 0):
    while  len(arr) > 0: #Looking at all values in the list
        if inte not in arr: #if the integer/string is not there return -1
            return -1
        elif arr[loc] == inte: #otherwise, if arr[loc] is equal to the integer/string, return loc
            return loc
        else:
            return searc_ndex(arr, inte, loc+1) #if its not equal iterate through the other locs

#_____Add up the digits of an integer_____
def sum_digits(inte, sum_=0):
    if inte == 0: #if zero, return zero
        return sum_
    else: 
        digit = inte % 10 #get value of digit in the tens position
        sum_ += digit #add to sum
        inte //= 10 #
        return sum_digits(inte, sum_) #find the sum of the remaining digits and add to sum

#_____Print values in an array, one per line_____     
def print_array(arr):
    if len(arr)==0:
        return 0 #if its empty, return zero
    else:
        print(arr[0]) #otherwise, print the first term
        print_array(arr[1:]) #Recursively loop through the remaining values in the array

#_____Minimum value in an array_____
def min_value(arr):
    if len(arr)==0: #if empty return zero
        return 0
    if len(arr) == 1:#If theres only on element, return it
        return arr[0]
    else:
        if arr[1] < arr[0]: #otherwise if the second term is less than the first
            return (min_value(arr[1:])) #Disregard the first term and loop through the remainder
        else:
            arr[1]=arr[0] #if the first term is less than the second, set it to be the second term
            return (min_value(arr[1:])) #Disregard the first term and loop through the remainder

            
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