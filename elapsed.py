import time
start=time.time()
print(23*2.3)
end=time.time()
print(end-start)

#using timeit
from timeit import default_timer as timer
satrt=timer()
print(23*2.3)
end = timer()
print(end-start)