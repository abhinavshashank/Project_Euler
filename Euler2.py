'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Sum=4613732'''

def fibonacci(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=1
sum=0
while (fibonacci(n)<4000000):
    if(fibonacci(n)%2==0):
        sum+=fibonacci(n)
    n+=1
print(sum)
