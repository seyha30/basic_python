
def sum_num(a,b):
    return a + b
def sayhi(str):
    print(str)
# unknown number of arguments
def my_function(*params):
    print(params)


print (sum_num(1, 2))
sayhi('str')
my_function('param1','param2','param3')