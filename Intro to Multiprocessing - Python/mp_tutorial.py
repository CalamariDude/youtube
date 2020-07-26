import multiprocessing
from multiprocessing import Process
import time

class Chef(Process):
    def __init__(self):
        Process.__init__(self)
    
    def cook_chicken(self):
        chicken = [0] * 10000000
        for cell in chicken:
            cell = 1
        return chicken

    def run(self):
        #do stuff
        cooked_chicken = self.cook_chicken()
        print("Chef has finished cooking the chicken!")
ts = time.time() # time since jan 1, 1970
chefs = []
print('cores: ', multiprocessing.cpu_count())

for i in range(48):
    chefs.append(Chef())
for chef in chefs:
    chef.start()
for chef in chefs:
    chef.join()

print('All the chefs are done. Time taken: ', round(time.time()-ts,2), 'seconds')



    