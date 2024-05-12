# Created by Li Zhao at 5/5/2024
# @Author   : 初见
# @File     : WaterTankControl.py
# @Software : PyCharm

from PIDControl import PIDControl
from PIDPlot import drawPlot

class WaterTank:
    def __init__(self, volumn , current, leak=0):
        self.volumn = volumn    # Maximun water volumn
        self.leak = leak        # water tank leak water ,default =0
        self.current = current  # current water volumn

    def print_info(self):
        print(f'Target Volumn: {self.volumn}, Current Volumn: {self.current}, leak: {self.leak}')

    # n: number of add water
    # dt: every dt msec
    def addWater(self, n, dt, pid):
        x =[0]
        y = [0]
    
        targetValue =self.volumn
        measureValue = self.current
        for i in range(1, n):

            waterTankPid = pid
            output = waterTankPid.calculate(targetValue, measureValue)

        
            measureValue =  measureValue + output - self.leak
            
            y.append(measureValue)
            print(f'i= {i},measure value= {measureValue:.2f}')
            x.append(dt * i)


        print(x)
        print(y)
        drawPlot(x,y)


def test1():
    wt = WaterTank(10,2)
    dt =10
    pid =PIDControl(0.7, 0, 0, dt, 10, 0)
    wt.addWater(10, dt, pid)
    

def test2():
    wt = WaterTank(10,2,1)
    dt =10
    pid =PIDControl(0.7, 0.01, 0, dt, 10, 0)
    wt.addWater(20, dt, pid)

def test3():
    wt = WaterTank(10,2,1)
    dt =10
    pid =PIDControl(0.7, 0.01, 0.02, dt, 10,-10)
    wt.addWater(20, dt, pid)

test3()