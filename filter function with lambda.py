#to check condition with lambda function we use filter keyword

lst=[12,14,45,67,11]
result=filter(lambda x:x%2==0,lst) 
print(list(result))


#wap to filter integers from list of values

lst=[1,1.2,15,-9]
result=filter(lambda x:type(x)==int,lst)
print(list(result))