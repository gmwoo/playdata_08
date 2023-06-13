class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second 
        
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
        
    def sub(self):
        result = self.first - self.second
        return result
        
    def mul(self):
        result = self.first * self.second
        return result
        
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4, 2)   # a는 setdata, add를 가지고 있음
print(a.add())
print(a.first)
print(a.second)

print(a.sub())
print(a.mul())
print(a.div())

###### 상속 #####
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())

###### 상속, 제곱 #####
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4, 2)
print(a.pow())


###### 메서드 오버라이딩 #####
# 상위 클래스의 메서드를 서브 클래스에서 재정의
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
a = SafeFourCal(4, 0)
print(a.div())