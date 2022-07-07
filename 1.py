# n=int(input("enter num"))
# div=int(input("enter num"))
  
# def find(n, div):
#     sum=
#     i=0
#     while n<2: 
#         q = n//div
#         print("Quotient: ", q)
    
#         r = n%div
#         print("Remainder", r)
# find(n, div)


# n = int(input("ent"))
# div = int(input("enter"))
# sum1 = 0
# sum2 = 0
# for i in range(2,div+1):
#     if i % n == 0:
#         sum1+=i
#     else:
#         sum2+=i
# print(abs(sum2-sum1))


#  n = int(input())
# div = int(input())

# def FindSumOfRemainders(n, div):
  
#     sum=0
#     a= []
#     for i in range(1,n+1):
       
#         sum=sum+ i%div 
#     return sum

# result = FindSumOfRemainders(n, div)
# print(result)


# k = int(input("enter the number: "))
# n = int(input("enter the number: "))
# l = []

# for i in range(0, n):
#     p = int(input())
#     l.append(p)
# def SumOfNumbers(l,n,k):
#     l.sort()
#     if k>=1 and k<=n:
#         if n>0:
#             if l[k-1]!=l[-k]:
#                 sum=l[k-1]+l[-k]
#                 return sum
#             else:
#                 return(l[k-1],l[-k])
# result = SumOfNumbers(l,n,k)
# print(result)


# n=int(input("enter the number: "))
# div=int(input("enter the number: "))
# def sumof_remainder(n,div):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+i%div
#     return sum
# result=sumof_remainder(n,div)
# print(result)


# k=int(input("enter the number: "))
# n=int(input("enter the number: "))
# l=[]
# for i in range(0,n):
#     p=int(input("enter no: "))
#     l.append(p)

# def sumof_number(l,n,k):
#     l.sort()
#     if k>=1 and k<=n:
#         if n>0:
#             if l(k-1)!=l(-k):
#                 sum=l(k-1)+l(-k)
#                 return sum
#             else:
#                 return l(k-1),l(-k)
# result=sumof_number(l,n,k)
# print(result)




# list1=[1,2,4]
# list2=[1,3,4]
# for i in list2:
#     list1.append(i)
# print(list1)

# list1=[1,2,4]
# list2=[1,3,4]
# i=0
# while i<len(list1):
#     a=list1[i]+list2[i]
#     i=i+1
#     print(a)

# n=input("enter the number: ")
# m="()","{}","[]","()[]{}"
# if (n in m):
#     print("True") 
# else:
#     print("False")


# list1=[1,2,4]
# list2=[1,3,4]
# list3=list1+list2
# list3.sort()
# print(list3)





# list1=[1,2,4]
# list2=[1,3,4]
# a=list1+list2
# n=a
# i=0
# m=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             m=a[j]
#             a[j]=a[i]
#             a[i]=m
#         j=j+1
#     i=i+1
# print(a) 


# n=input("enter the name: ")
# dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# m=0
# for i in range(len(n)):
#     if i+1!=len(n) and dict[n[i]]<dict[n[i+1]]:
#         m=m-dict[n[i]]
#     else:
#         m=m+dict[n[i]]
# print(m)




# list1=[1,2,4]
# list2=[1,3,4]
# list=list1+list2
# i=0
# while i<len(list):
#     list.sort()
#     i=i+1
# print(list)



