'''#converting string to list
string="hello"
print(list(string))'''

'''#updating elements of a list
lst=[1,2,3,2.3,True]
lst[1]="hello"      #in index 1 we get hello by changing
print(lst)'''

'''#functions used in list

lst=[1,2,"hello"]
lst.append(23)
print(lst)      # append inserts a single element at the end of list
lst.extend([34,56,78,True])  #inserts multiple elements at end of list
print(lst)
del lst[3]  #delets the element at particular index(delete is a keyword)
print(lst)
print(lst.pop(-2))    #returns the deleted element'''

lst=[1,2,2,2,3,"hello"]
print(lst.count(2))  #returns frequency of occurence of an element
print(lst.index("hello"))  #returns the index of element
lst.insert(3,40)  #inserts 40 at index 3
print(lst)
lst.sort()    #used to sort the list
lst.sort(reverse=True)   #sorts the list in descending order
lst.reverse()       #reverse the list
print(lst)
