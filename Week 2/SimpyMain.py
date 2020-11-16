import car_mod
car_mod.Car

import simpy

def driver(env, car):
     yield env.timeout(3)
     car.action.interrupt()

env = simpy.Environment()
car = car_mod.Car(env)
env.run(until=15)



