# # # # # var = 10
# # # # # def foo():
# # # # #   var = 15
# # # # # foo()
# # # # # print(var)
# # # # def foo():
# # # #   x = 'Python'
# # # #   def bar():
# # # #     nonlocal x
# # # #     x = 'Java'
# # # #   bar() 
# # # #   return x

# # # # print(foo())

# # # def foo():
# # #   x = 'Python'
# # #   def bar():
# # #     x = 'Java'
# # #   bar() 
# # #   return x

# # # print(foo())
# # def my_func(l1, l2):
# #   r = []
# #   for i in range(len(l1)):
# #     r.insert(l2[i], l1[i])
# #   return r


# # l1 = [0, 1, 2, 3, 4]
# # l2 = [0, 1, 2, 2, 1]

# # if __name__ == "__main__":  
# #   r = my_func(l1, l2)
# #   print(r)
# num = 4

# def foo(num):
#   return num**3

# foo(3)**2

import threading
print("Current:",threading.current_thread().getName())


