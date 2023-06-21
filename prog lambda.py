#wap to add two list using lambda function
lst1=[1,2,6,8,9]
lst2=[4,8,9,0,8]
result=map(lambda x1,x2:x1+x2,lst1,lst2)
print(list(result))