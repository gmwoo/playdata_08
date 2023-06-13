class Car:
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
    
    def upSpeed(self, value):    # self, speed 는 3행의 speed 의미
        self.speed += value      # 즉, 자신의 클래스에 있는 speed 변수
        if self.speed >= 150:
            self.speed = 150
    
    def downSpeed(self, value):
        self.speed -= value
        
# main code part
myCar1 = Car("빨강", 30)
myCar2 = Car("파랑", 60)

# ouput
print("Car1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))
print("Car2의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))