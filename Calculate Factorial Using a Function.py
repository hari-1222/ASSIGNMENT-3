a=int(input('Enter a number:'))
def factorial(a):
    if a<2:
        return 1
    else:
        return a * (factorial(a-1))
output=factorial(a)
print(f"Factorial of {a} is:",factorial(a))