# Created by Li Zhao at 5/5/2024
# @Author   : 初见
# @File     : PIDControl.py
# @Software : PyCharm

class PIDControl:
    def __init__(self, kp, ki, kd, dt , max, min ):
        self.kp = kp        # Proportional gain
        self.ki = ki        # Integral gain
        self.kd = kd        # derivative gain
        self.dt = dt        # loop interval time
        self.max = max      # Max value of manipulated variable
        self.min = min      # Min value of manipulated variable
        self.integral = 0   # integral error
        self.previousError = 0  # previous  error
        self.error = 0      # targetValue - measureValue
        self.derivative = 0   # error - previousError
        self.output = 0       # output



    def calculate(self, targetValue, measureValue):
        self.error = targetValue - measureValue
        self.integral = self.integral + self.error * self.dt
        self.derivative = self.error - self.previousError
        self.previousError = self.error
        self.output = self.kp*self.error + self.ki*self.integral + self.kd*self.derivative
        if(self.output > self.max):
            self.output = self.max
        elif(self.output < self.min):
            self.output = self.min
        self.print_info(
            
        )
        self.print_info()
        return self.output

    def print_info(self):
        print(f'Kp: {self.kp}, Ki: {self.ki}, Kd: {self.kd} ,error: {self.error:.2f}, integral:{self.integral:.2f}, derivative:{self.derivative:.2f} , output:{self.output:.2f}')




