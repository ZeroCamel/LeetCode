#!/usr/bin/python3

# 递归 阶乘
def F(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*F(n-1))

# a=F(1)
# print(a)

# 从排序数组中删除重复项
# 不需要分配额外的空间
# 1、后面数字往前面冒泡
def RemoveDuplicateArray(list):
    length=1
    for index in range(0,len(list)-1):
        if(list[index]!=list[index+1]):
            length+=1
            list[length]=list[index+1]

    for index in range(length):
        print(list[index])
    return

# array=[0,0,1,1,1,2,2,3,3,4]
# RemoveDuplicateArray(array)

# 买卖股票的最佳时机
# 先假设买点后假设卖点 有漏洞 C数组不满足 6 1 3 2 4 7
def MaxStcockProfit(prices):
    profit=0
    start_i=0
    length=len(prices)-1

    # 判断卖点并计算
    # 与买点正好相反 排列组合
    while start_i < length:

        # 判断第一次买点
        # 1、下三角
        # 2、递增是第一个
        # 3、递减是最后一个
        for k in range(start_i,length):
            if k<length-1:
                if prices[k+1]<=prices[k]:
                    start_i=k+1
                else:
                    break
            else:
                continue

        max=min=prices[start_i]
        out_length=0
        for j in range(start_i+1,len(prices)):
            blFlag=False
            if(j<=length-1):
                blFlag=True if min<prices[j] and prices[j+1]<prices[j] else False
            else:
                blFlag=True if min<prices[j] else False

            if blFlag:
                max=prices[j]
                out_length=j+1
                break
            else:
                out_length=j
                continue       
        profit+=max-min
        if(j!=out_length):
            start_i=j
        start_i+=1
    return profit

a=[7,1,5,3,6,4]
b=[1,2,3,4,5,6]
d=[7,6,4,3,1]
c=[6,1,3,2,4,7]
e=[2,1,4]
f=[3,2,6,5,0,3]
# 相等 重复 判断买入卖点边界
g=[2,1,2,1,0,0,1]
h=[3,3,5,0,0,3,1,4,0,0,3,4,5,7,1,23,50,4]
k=[1,2,4,2,5,7,2,4,9,0]
kk=[1,7,4,2]

# print(MaxStcockProfit(a))

# 旋转数组
#方案一 超时
def rotate(nums,k):
    i=0
    temp=0
    length=len(nums)

    while i < k:
        temp=nums[length-1]
        for j in range(length-1,0,-1):
            nums[j]=nums[j-1]
        nums[0]=temp
        i+=1
    return nums

#方案二 优化
def rotate2(nums,k):
    length=len(nums)
    trueK=k%length
    if trueK==0:
        return nums
    else:
        k=trueK
    
    b=[nums[i] for i in range(length-k,length)]
    for g in range(length-1-k,-1,-1):
        nums[g+k]=nums[g]  
    for h in range(k):
        nums[h]=b[h]
    return nums

nums=[1,2]
newnums=rotate2(nums,3)
for i in newnums:
    print(i)



