#Write a Python program to filter the height and weight of students, which 
#are stored in a dictionary using lambda.
'''Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),
 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height> 6 ft and Weight> 70 kg:
{'Cierra Vega': (6.2, 70)}'''


l={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),
 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
result=dict(filter(lambda x:x[1][0]>6 and x[1][1]>70,l.items()))
print(result)