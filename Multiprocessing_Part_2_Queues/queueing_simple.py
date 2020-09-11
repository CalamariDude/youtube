import multiprocessing
from multiprocessing import Process, Queue
import time

class Chef(Process):
    def __init__(self, queue, chicken):
        Process.__init__(self)
        self.queue = queue
        self.chicken = chicken
    
    def cook_chicken(self, chicken):
        for i in range(len(chicken)):
            chicken[i] = 1
        return chicken

    def run(self):
        #do stuff
        cooked_chicken = self.cook_chicken(self.chicken)
        print("Chef has finished cooking the chicken!")
        self.queue.put(cooked_chicken)

ts = time.time() # time since jan 1, 1970
chefs = [] 
queue = Queue()
chickens_to_cook = 4
for i in range(chickens_to_cook):
    raw_chicken = [0] * 10000000 #some raw chicken
    chefs.append(Chef(queue, raw_chicken))
for chef in chefs:
    chef.start()
while chickens_to_cook  > 0:
    cooked_chicken = queue.get() #default blocks
    print('cooked chicken received! ', cooked_chicken[0])
    chickens_to_cook -=1

print('All the chefs are done. Time taken: ', round(time.time()-ts,2), 'seconds')



    