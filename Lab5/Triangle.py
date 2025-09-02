class Triangle : 
    __count = 0
    def __init__(self,*args):
        
        if len(args) == 0:
            self.sideA=self.sideB=self.sideC = 1.0
        elif len(args)== 1:
            if isinstance(args[0],Triangle):
                other = args[0]
                self.sideA,self.sideB,self.sideC = other.sideA,other.sideB,other.sideC
            else:   
                self.sideA=self.sideB=self.sideC = float(args[0])
            
        elif len(args) == 2 :
            x,y = args
            self.sideA=self.sideB = float(x)
            self.sideC = float(y)
        
        elif len(args) == 3 :
            self.sideA,self.sideB,self.sideC = map(float,args)
            
        else:
            raise ValueError("Invalid number of arguments")
        
        Triangle.__count += 1
          
    @property
    def sideA(self):
        return self.__sideA

    @sideA.setter
    def sideA(self, value):
        if value <= 0:
            raise ValueError("Side length must be positive")
        self.__sideA = value

    @property
    def sideB(self):
        return self.__sideB

    @sideB.setter
    def sideB(self, value):
        if value <= 0:
            raise ValueError("Side length must be positive")
        self.__sideB = value

    @property
    def sideC(self):
        return self.__sideC

    @sideC.setter
    def sideC(self, value):
        if value <= 0:
            raise ValueError("Side length must be positive")
        self.__sideC = value        

    def perimeter(self):
        return self.sideA + self.sideB + self.sideC
    
    def isRightAngled(self):
        
        sides = sorted([self.sideA, self.sideB, self.sideC])
        a,b,c = sides[0],sides[1],sides[2]
        return (a*a) + (b*b) == c*c
     
    def clone(self):
        return Triangle(self)

    @classmethod
    def objectCount(cls):
        return cls.__count
    
    def __str__(self):
        return f"Triangle(sides: {self.sideA}, {self.sideB}, {self.sideC})"
