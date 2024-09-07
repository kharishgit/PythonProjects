# Gradient descent is an optimization algorithm used to minimize a function by iteratively moving towards the
# direction of the steepest descent, i.e., where the function decreases most rapidly. It('s widely used in '
# machine learning, particularly for training models by minimizing a cost function (also called a loss function), which measures how well the model is performing.)
# Key Concepts of Gradient Descent:
#
#     Objective: The goal of gradient descent is to find the minimum value of a function
#     (like a cost or loss function). In machine learning, this often involves finding the best parameters
#     (e.g., weights and biases) that minimize the error between predicted and actual values.
#
#     Gradient: The gradient is a vector of partial derivatives of the function with respect to its parameters.
#     It indicates the direction and rate of the steepest increase of the function. In gradient descent,
#     we move in the opposite direction of the gradient to minimize the function.
#
#     Learning Rate (Step Size): The learning rate is a hyperparameter that determines the size of the steps
#     taken towards the minimum. If the learning rate is too small, convergence will be slow; if it('s too large, '
#     'the algorithm may overshoot the minimum and fail to converge.)
#
#     Iterations: Gradient descent runs for a certain number of iterations (or until it converges). In each
#     iteration, the algorithm updates the model parameters by taking a small step in the opposite direction of
#     the gradient.

import numpy as np

def gradientdescent(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08
    for i in range(iterations):

        y_predicted = m_curr * x + b_curr
        mse = 1 / n * sum([val ** 2 for val in (y - y_predicted)])
        md = - (2/n) * sum(x*(y-y_predicted))
        bd = - (2/n) * sum (y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print(f"iterations {i}, m ={m_curr}, b ={b_curr},mse = {mse}")


x=np.array([1,2,3,4,5])
y =np.array([5,7,9,11,13])

gradientdescent(x,y)