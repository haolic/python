def fact(n):
    return fact_iter(n, 1)
def fact_iter(n, product):
    if n == 1:
        return product
    return fact_iter(n - 1, n * product)
print(fact(1))
print(fact(5))
print(fact(100))
print(fact(1000))
# python 没有对尾递归做优化，所以即便用上述尾递归方式写函数，依然会导致栈溢出。