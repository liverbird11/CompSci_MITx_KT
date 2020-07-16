## Cleaning Robot Simulation

This simple Python program is created from a problem set (pset2) in the course [Introduction to Computer Science and Programming using Python](https://www.edx.org/course/introduction-to-computer-science-and-programming-7) by MITx, which I attended from Jan-Mar 2020.

This code simulates the movement of cleaning robots in a rectangular room. You can investigate what movement strategies would work well in rectangular rooms of different sizes and aspect ratios!

#### Running the code

You can run the code from your chosen IDE (e.g. Spyder) by first running _ps2.py_. The visualization of robot movement requires on Python version 3.7 to run.

Visualize movement of a standard robot in a square room with 5-by-5 grid by typing in the console:

```python
testRobotMovement(StandardRobot, RectangularRoom)
```

Simulate the run time for a robot to finish cleaning a room (you have the choices of StandardRobot or RandomWalkRobot for robot_type, and min_coverage refers to the proportion of room cleaned as the trigger to stop the simulation):

```
runSimulation(num_robots = 1, speed = 1.0, width = 10, height = 10, min_coverage = 0.75, num_trials = 30, robot_type = StandardRobot)
```

You can see the plot comparing the time taken for 1-10 robots to finish cleaning a room:

```
showPlot1("Time taken for 1-10 robots", "No. of robots", "Steps")
```

You can see the plot comparing the time taken for 2 robots to clean various aspect ratios:

```
showPlot2("Time taken for 2 robots to clean various aspect ratios", "Aspect ratios", "Steps")
```

