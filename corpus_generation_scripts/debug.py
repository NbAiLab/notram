import time

start_time = time.time()

def exec_time():
    end_time = time.time()
    out = str(round(end_time-start_time,1)) + " seconds"
    return out

for i in range (0,10000000):
    ...

print(f'From start: {exec_time()}')

for i in range (0,10000000):
    ...

print(f'From start: {exec_time()}')
