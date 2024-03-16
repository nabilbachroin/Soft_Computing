#Gradient Descent with Rastrigin 1D function (animation)

import matplotlib.animation as animation
import numpy as np
import math
import matplotlib.pyplot as plt

def gradient_descent2(gradient, start, learn_rate, n_iter=50): 
    tolerance=1e-03
    vector = start
    yield vector
    for _ in range(n_iter):
        step = -learn_rate * gradient(vector)
        if np.all(np.abs(step) <= tolerance): #check that the difference is small enough
            break
        vector += step
        print('FUN=',C(vector))    
        yield vector
    #return results

def C(x): #rastrigin 1D 
   return 10.0 + x * x - 10.0 * np.cos(2.0 * math.pi * x)
    

def gradC(x):
    return 2 * x + 62.8319* np.sin(6.28319* x)

def animate(i,gen):
    vec=next(gen)
    print(vec)
    plt.plot(vec[0],C(vec[0]),'ro')

def main():	
    x=np.arange(-2,3,0.1)
    y=C(x)
    plt.plot(x,y)
    r=-2+np.random.random()*5 #random starting point
    start=np.array([r])
    gen=gradient_descent2(gradC,start,0.001)
    ani = animation.FuncAnimation(plt.gcf(), animate,fargs=(gen,), interval=1000) 
    
    
    plt.show()


if __name__ == "__main__":
    main()