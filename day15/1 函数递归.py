'''
1 什么是函数递归
    函数递归调用（是一种特殊的嵌套调用）：在调用一个函数的过程中，又直接或间接地调用了该函数本身

    递归必须要有两个明确的阶段：
        递推：一层一层递归调用下去,强调每进入下一层递归问题的规模都必须有所减少
        回溯：递归必须要有一个明确的结束条件，在满足该条件时结束递推
            开始一层一层回溯

    递归的精髓在于通过不断地重复逼近一个最终的结果

2、为什么要用函数递归


3、如何用
'''


# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(3000)
# def foo(n):
#     print('from foo',n)
#     foo(n+1)
# foo(0)

# def bar():
#     print('from bar')
#     foo()
#
# def foo():
#     print('from foo')
#     bar()

# foo()

# age(5) = age(4) + 2
# age(4) = age(3) + 2
# age(3) = age(2) + 2
# age(2) = age(1) + 2
# age(1) = 26

# age(n) = age(n-1) + 2 #n > 1
# age(1) = 26           #n = 1


# def age(n):
#     if n == 1:
#         return 26
#     return age(n-1) + 2
#
# print(age(5))


# l=[1,[2,[3,[4,[5,[6,[7,[8,[9,]]]]]]]]]
#
# def tell(l):
#     for item in l:
#         if type(item) is list:
#             #继续进入下一层递归
#             tell(item)
#         else:
#             print(item)
#
# tell(l)

# 有一个从小到大排列的整型数字列表
# nums=[1,3,7,11,22,34,55,78,111,115,137,149,246,371]
# 10 in nums
# for item in nums:
#     if item == 10:
#         print('find it')
#         break
# else:
#     print('not exists')
###############################
nums=[1,3,7,11,22,34,55,78,111,115,137,149,246]
def search(search_num,nums):
    # print(nums)
    if len(nums) == 0:
        #print('not exists')
        return
    mid_index=len(nums) // 2
    if search_num > nums[mid_index]:
        # in the right
        nums=nums[mid_index+1:]
        search(search_num,nums)
    elif search_num < nums[mid_index]:
        # in the left
        nums=nums[:mid_index]
        search(search_num,nums)
    else:
        print('find it')

search(111,nums)

# nums=[1,3,7,11,22,34,55,78,111,115,137,149,246,371]
# def search(search_num,nums): # def search(search_num,nums):
#     if len(nums)==0:#if len(nums) == 0:
#         print('not exits')
#         return
#     mid_index=len(nums) // 2 #     mid_index=len(nums) // 2
#     if search_num > nums[mid_index]: #     if search_num > nums[mid_index]:
#         nums=nums[mid_index+1:]  #nums=nums[mid_index+1:]
#         search(search_num,nums)  #         search(search_num,nums)
#     elif search_num < nums[mid_index]:  #     elif search_num < nums[mid_index]:
#         nums=nums[:mid_index]  #         nums=nums[:mid_index]
#         search(search_num,nums)  #         search(search_num,nums)
#     else:
#         print('find it')
#
#
#  search(111,nums)