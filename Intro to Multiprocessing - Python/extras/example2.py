import multiprocessing
from multiprocessing import Process
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
        print('Chef is finished cooking the chicken.')
print('number of cores: ', multiprocessing.cpu_count())
ts = time.time()
chefs = []
for i in range(48):
    chef = Chef()
    chefs.append(chef)
for chef in chefs:
    chef.start()
for chef in chefs:
    chef.join()

print("All the chefs are done! time taken: ", round(time.time()-ts, 2), "seconds")


