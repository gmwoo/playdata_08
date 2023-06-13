class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
        
cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()  # 계속해서 계산기를 만들 수 있음(클래스 장점)

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal3.sub(4))

#### pass
class Cookie:
    pass

a = Cookie()
b = Cookie()

##### 생성자
class class_name:
    def __init__(self):
        # 이 부분에 초기화할 코드 입력
        pass