import multiprocessing
from multiprocessing import Process
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import time

class Chef(Process):
    def __init__(self):
        Process.__init__(self)

    def cook_chicken(self):
        seasonings = [0] * 1000000
        for seasoning in seasonings:
            seasoning = 1
        return seasonings
                
    def run(self):
        chicken = self.cook_chicken()
        # print('Chef is finished cooking the chicken.')

print(multiprocessing.cpu_count())
times_taken = []
for processes in range(1,128):
    chefs = []
    print(processes)
    for i in range(processes):
        chefs.append(Chef())

    ts = time.time()
    for chef in chefs:
        chef.start()

    for chef in chefs:
        chef.join()
    times_taken.append(time.time() - ts)

plt.plot(range(1,128), times_taken, color='red')
plt.title('Time taken vs Number of Chickens Cooked with 12 Chefs')
plt.xlabel('Chickens cooked')
plt.ylabel('Time Taken (seconds)')
plt.show()