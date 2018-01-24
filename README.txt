This program simulates the path for a robot from source to goal using Artificial Potential Field Planning algorithm.

Run mover.py(Use python2.7) for demo. The driver program asks for the information about the environment and plots the path of the robot.

Hyperparameters a & b are chosen to scale the values of delta X and delta Y small as compared to their actual values.

b is chosed to be significantly larger than a since we want to avoid the obstacle at all costs and take smaller steps.

Spread of the obstacle is restricted to 10 units, otherwise the robot was entering the obstacle and bouncing back.