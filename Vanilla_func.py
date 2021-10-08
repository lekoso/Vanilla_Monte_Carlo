
from math import exp,sqrt
import numpy as np

def Vanilla_func(StockPrice, Exercise, Interest, time, Volatility, Iteration):
     tim = time / 12
     Simulated = []
     StockSimulate = []
     StockSimulate.append(StockPrice)
     count = 0

     for i in range(1, Iteration):
          z = np.random.standard_normal(Iteration)
          StockSimulate.append(StockSimulate[0] * exp((Interest - 0.5 * Volatility**2 * tim) + (Volatility *sqrt(tim) * z[count])))
          
          payof = exp(-Interest * tim) * max(StockSimulate[i] - Exercise, 0)
          count = count + 1

          Simulated.append(payof)
     callMonte = sum(Simulated)/len(Simulated)
     return callMonte