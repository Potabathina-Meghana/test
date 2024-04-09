""" In each iteration, we concatenate a string of spaces (" " * (n - i)) followed by a string of stars ("*" * (2 * i - 1)") to the pattern string. The number of stars in each row is 2 * i - 1 (where i is the current row number), and the number of spaces decreases by 1 in each row (n - i)."""

def print_star_triangle(n):
    pattern = ""
    for i in range(1, n + 1):
        pattern += " " * (n - i) + "*" * (2 * i - 1) + "\n"
    return pattern

# Test the function
n = int(input("Enter the number of rows: "))
print(print_star_triangle(n))


n = int(input())
space = n-1
star = 1
for i in range(n):
    a=space
    b=star
    for j in range(a):
        print(" ", end='')
        a-=1
    for k in range(b):
        print("*", end='')
        b-=1
    space-=1
    star+=2
    n-=1
    print()

