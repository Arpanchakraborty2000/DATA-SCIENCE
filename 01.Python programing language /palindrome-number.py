def is_palindrome(n):
    return str(n) == str(n)[::-1]

number = list(map(int, input("Enter the numbers separated by space: ").split()))

palindrome = sorted([n for n in number if is_palindrome(n)])

print("This is your list:", palindrome)
