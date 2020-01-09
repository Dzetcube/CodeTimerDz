"""
Usage Example of dzcodetimer.py

"""
from dzcodetimer import CodeTimer

timer = CodeTimer()

# step 1
x = 1
for i in range(1000):
    x += i
print(x)
timer.check("step 1")

# step 2
timer.start_step()
x = 1
for i in range(10000):
    x += i
print(x)
timer.check("step 2 from start")
timer.end_step("only step 2")

# step 3
timer.start_step()
x = 1
for i in range(1000000):
    x += i
print(x)
timer.check("step 3 from start")
timer.end_step("only step 3")