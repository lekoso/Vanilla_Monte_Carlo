import sys
sys.path.append('A:\Lekan\Miscellaneous\python\modules')
import Vanilla_func as VF

Price = 50
Exercise = 47
Interest = 0.04     #in percentage fraction
Time = 1         #in months
Volatility = 0.8
Iteration = 10000

result = round(VF.Vanilla_func(Price, Exercise, Interest, Time, Volatility, Iteration), 2)
print(result)
