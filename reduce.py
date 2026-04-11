from functools import reduce 
result = reduce (lambda x,y:x+y,range(1,101))
print("sum =",result)
