from matplotlib import pyplot as plt
import numpy as np

def linearFunctionAlgorithm():
    userSlopePoints = input('In order to create a linear equation, first, we need to find the slope. Provide the first set of points spaced by a comma. Ex: 2,3. ')
    user2ndPoints = input("Provide the second set of points: ")
    x_str, y_str = userSlopePoints.split(',')
    x_value = float(x_str)
    y_value = float(y_str)
    x_str2, y_str2 = user2ndPoints.split(',')
    x_value2 = float(x_str2)
    y_value2 = float(y_str2)
    
    slopeFormula = (y_value2 - y_value) / (x_value2 - x_value)
    b = y_value - slopeFormula * x_value
    
    if b >= 0:
        equation = f'y = {slopeFormula:.3f}x + {b:.3f}'
    else:
        equation = f'y = {slopeFormula:.3f}x - {abs(b):.3f}'
    
    print(equation)
    
    inputGraph = input("Would you like to see the equation on a graph? Type Yes or No: ").lower()
    if inputGraph == "yes":

        x_values = np.linspace(-50, 50, 1000)
        y_values = slopeFormula * x_values + b
        
 
        plt.plot(x_values, y_values, label=equation, color = 'g', )
        
 
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the Linear Equation')
        plt.grid(True)
    
        plt.legend()   
        plt.show()

linearFunctionAlgorithm()
