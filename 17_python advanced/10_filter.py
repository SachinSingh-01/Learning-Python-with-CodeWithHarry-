# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a=[1, 3, 4, 5, 342, 12, 42, 53, 3, 6, 77, 43] 

new=list(filter(lambda x: x>9, a))
print(new)