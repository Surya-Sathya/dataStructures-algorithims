def iterative_sum_upto(n):
    i = 1
    whileloop_res = 0
    while i <= n:
        whileloop_res += i
        i += 1
    
    print(f"While loop iterative result: {whileloop_res}")

    forloop_res = 0
    for j in range(1, n+1):
        forloop_res += j

    print(f"For loop iterative result: {forloop_res}")

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

n = 5
iterative_sum_upto(n)
print(f"Recursive sum up to: {sum(n)}")


"""
#RANGE:
In Python-3, range creates the much more efficient range-object instead, 
which provides the numbers as needed rather than all at once in a list
"""

"""
#my_iterator describes the iterator, and the iterables are the elements within this iterator
#Also I guess x^x means XOR gate between two binary representations of x? so 5 ^ 2 -> 0101 ^ 0010 -> 0111 = 7
my_iterator = iter([1, 5, 10])
print([i**2 for i in my_iterator])
print([i**2 for i in my_iterator]) #Stateful: Once you've looped over, this will return [] 
#https://treyhunner.com/2018/02/python-range-is-not-an-iterator/
"""

