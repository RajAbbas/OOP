from Triangle import Triangle

t1 = Triangle()          
t2 = Triangle(5)         
t3 = Triangle(4, 6)      
t4 = Triangle(3, 4, 5)   
t5 = Triangle(t4)        

print(t1)
print(t2.perimeter())  
print(t4.isRightAngled())
print(Triangle.objectCount())
