""" x = int(input('give me a number'))
if(x%2) == 0:
    print('even')
else:
    print('odd') """
#---------------------------------------------------------

""" x = int(input('subtotal'))
service = input('How was the service')
if service == ("bad"):
    print(int(x))
elif service == ("okay"):
    print(int(x*1.15))
elif service == ("good"):
    print(int(x*1.2))
elif service == ('great'):
    print(int(x*1.25)) """

#------------------------------------------------------------------

""" def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors 
1
number = int(input("Please enter a number: "))
list_of_factors = get_all_factors(number)
print("factors of {} are: {}".format(number,list_of_factors)) """

#--------------------------------------------------------------------------------------

def gcf(numX, numY):
    if numX > numY:
        x = numY
    else:
        x = numX
    cf = []
    for i in range(1,x+1):
        if(numX,numY)%i == 0:
            cf.append(i)
    return cf
    
numX = int(input('please enter the first number:'))
numY = int(input('please enter the second number:'))
print(max(gcf))
