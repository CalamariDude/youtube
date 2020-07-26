import multiprocessing
from multiprocessing import Process
import time

class Chef(Process):
    def __init__(self):
        Process.__init__(self)

    def season_chicken(self):
        #Takes 3 seconds to season chicken
        time.sleep(1)

    def cook_chicken(self):
        #Takes 10 seconds to cook the chicken
        time.sleep(1)

    def run(self):
        self.season_chicken()
        self.cook_chicken()
        print(multiprocessing.current_process().name, 'done with chicken')

print('total processors', multiprocessing.cpu_count())

chef1 = Chef()
ts = time.time()
chef1.start()
chef1.join()

print('Time taken for all 4 chefs to finish cooking chicken:', round(time.time()-ts,2), 'seconds.')