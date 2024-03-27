'''
You are given a positive integer N which represents the number of steps in a staircase. 
You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
Can you find a solution in O(n) time?
'''


# Time complexit 2^n
def staircase_recursive(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    return staircase_recursive(n - 1) + staircase_recursive(n - 2)


print(staircase_recursive(4))  # 5
print(staircase_recursive(5))  # 8

# Time complexity O(n)
def staircase_memo(n, memo={}):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = staircase_memo(n - 1, memo) + staircase_memo(n - 2, memo)
    return memo[n]


print(staircase_memo(4))  # 5
print(staircase_memo(5))  # 8
