"""
List  comprehension  is  a  concise  and  expressive  way  to  create 
lists  in  Python.  It  provides  a  more  compact  syntax  for  generating 
lists  compared  to  using  traditional  loops. 
"""
# [expression for item in iterable if condition]


# l1 = [even*2 for even in range(1,10)]
# print(l1)

list1 = [10,25,63,18,92,64,615,268,61,46,26,41,2,3,6,7]
list2  =  [even  for  even  in  list1  if  even%2==0] 
print(list2) 