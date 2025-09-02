class Rational:
    def _reduce(self,num,den,sign):
        a = abs(num)
        b = abs(den)
        
        while a % b != 0:
            tempA = a 
            tempB = b
            a = tempB
            b = tempA % tempB 
            
        red_n = abs(num) // b * sign       
        red_d = abs(den) // b  
             
        return [red_n,red_d]     
    def __init__(self,num,den):
        if (not isinstance(num,int)) or (not isinstance(den,int)):
            raise TypeError("The numerator and denominator must be an integer")
        
        if den == 0:
            raise ValueError("The denominator must not be equal to 0")
        
        if num == 0:
            self.numerator = 0
            self.denominator = 1

        sign = 0
        if ((num<0) and (den>0)) or ((num>0 and den<0)):
            sign  = -1
        else :
            sign = 1

        self.numerator,self.denominator = self._reduce(num,den,sign)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self,other):
        if isinstance(other,int):
            n = self.numerator + self.denominator*other
            d = self.denominator
            return Rational(n,d)
        
        if not isinstance(other,Rational):
            raise TypeError("The addition is only possible between int or Rational")
    
        n = self.numerator*other.denominator + other.numerator*self.denominator
        d = self.denominator * other.denominator
        return Rational(n,d)
    
    def __sub__(self,other):
        if isinstance(other,int):
            n = self.numerator - self.denominator*other
            d = self.denominator
            return Rational(n,d)
        
        if not isinstance(other,Rational):
            raise TypeError("The subtraction is only possible between int or Rational")
    
        n = self.numerator*other.denominator - other.numerator*self.denominator
        d = self.denominator * other.denominator
        return Rational(n,d)
    
    def __mul__(self,other):
        if isinstance(other,int):
            n = self.numerator*other
            d = self.denominator
            return Rational(n,d)
        
        if not isinstance(other,Rational):
            raise TypeError("The multiplication is only possible between int or Rational")
    
        n = self.numerator*other.numerator
        d = self.denominator * other.denominator
        return Rational(n,d)
    
    def __mul__(self,other):
        if isinstance(other,int):
            n = self.numerator*other
            d = self.denominator
            return Rational(n,d)
        
        if not isinstance(other,Rational):
            raise TypeError("The multiplication is only possible between int or Rational")
    
        n = self.numerator*other.numerator
        d = self.denominator * other.denominator
        return Rational(n,d)
     
    def __truediv__(self,other):
        
        if isinstance(other,int):
            n = self.numerator
            d = self.denominator * other
            return Rational(n,d)
        
        if not isinstance(other,Rational):
            raise TypeError("The multiplication is only possible between int or Rational")
    
        n = self.numerator*other.denominator
        d = self.denominator * other.numerator
        return Rational(n,d)
    
    def __eq__(self, other):
        if not isinstance(other,Rational):
            raise TypeError("The Argument must be a Rational Number")
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)
    
    def __ne__(self, other):
        return not self == other
    def __lt__(self,other):
        return (self.numerator*other.denominator < self.denominator*other.numerator)
    def __gt__(self,other):
        return not (self == other or self < other)

    def __le__(self,other):
        return self == other or self < other

    def __ge__(self,other):
        return self == other or self > other