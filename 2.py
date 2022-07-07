# number=int(input("enter the number: "))
# for i in range (number):
#     a,b=map(int,input().split())
#     aeven=a//2
#     aodd=a-aeven
#     beven=b//2
#     bodd=b*beven
#     ans=(aeven*beven)+(aodd*bodd)
#     print(ans)





# num=int(input("entr the number: "))
# i=1
# sum=0
# while i<=num:
#     num1=int(input("enter the number: "))
#     if num1%2==0:
#         sum=sum+num1
#     i=i+1
# print(sum)






# t=int(input())
# for i in range(t):
#      c,d,l=map(int,input().split())
#      total=(c+d)*4
#      if(c>(d*2)):
#         min_legs=(c-(d*2)+d)*4
#      else:
#         min_legs=(d*4)
#      if l%4==0 and l>=min_legs and l<=total:
#          print("yes")
#      else:
#           print("no")


# t=int(input())
# for i in range(t):
#      c,d,l=map(int,input().split())
#      total=(c+d)*4
#      if(c>(d*2)):
#         min_legs=(c-(d*2)+d)*4
#      else:
#         min_legs=(d*4)
#      if l%4==0 and l>=min_legs and l<=total:
#          print("yes")
#      else:
#           print("no")

# i=7
# j=1
# while i>=1:
#     print(" "*j,i*"*",j*" ")
#     j=j+1
#     i=i-2


# num=int(input("enter the number: "))
# sum=0
# i=0
# while num!=0:
#     rem=num%10
#     sum=sum+rem*pow(2,i)
#     num=int(num/10)
#     i=i+1
# print("decimal number:",sum)

# num=30
# n=[10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# n1=[]
# while i<len(n):
#     j=0
#     n2=[]
#     while j<len(n):
#         if n[i]+n[j]==num:
#             n2.append(n[i])
#             n2.append(n[j])
#             n1.append(n2)
#         j=j+1
#     i=i+1
# print(n1)


# elements= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# while i<len(elements):
#     if elements[i]%2==0:
#         sum=sum+elements[i]
#         print(elements[i],"even")
#     else:
#         sum=sum+elements[i]
#         print(elements[i],"odd")
#     i=i+1
# print(sum)


# i=int(input('enter a number: '))
# number1=int(input('enter the number: '))
# x=[]
# while i<=(number1):
# 	j=1
# 	y=[]
# 	x.append(i)
# 	while j<=10:
# 		z=j*i
# 		y.append(z)
# 		j+=1
# 	i=i+1
# 	x.append(y)
# print(x)


# list=[1,2,3,4,5,6]
# i=0
# j=-1
# l=[]
# while i<len(list)/2:
#     l.append(list[j])
#     l.append(list[i])
#     i=i+1
#     j=j-1
# print(l)
    

# list=[[1,2],[3,4],[5,6]]
# i=0
# sum=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         sum=sum+list[i][j]
#         j=j+1
#     i=i+1
# print(sum)


# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = ['10','20','56','45','36','20']
# i=0
# list=[]
# while i<len(students):
#     z=str(students[i]+marks[i])
#     list.append(z)
#     i=i+1
# print(list)



# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# i=0
# while i<len(list):
#     j=1
#     c=0
#     while j<=(list[i]):
#         if list[i]%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         print(list[i],"prime number")
#     else:
#         print(list[i],"not prime number")
    # i=i+1


# def num(number):
#     i=1
#     sum=0
#     while i<=25:
#         if i%number==0:
#             print(i)
#             sum=sum+i
#         i=i+1
#     print("sum",sum)
# num(int(input("enter the number: ")))











 

    
    


        
       
















