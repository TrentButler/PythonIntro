How to use AStar Unit Test Script:

Requirements:
astar algorithm function must take in three arguments
start, goal, and graph
any additional functionality needed like getting neighbors, calcgscore, calchscore, and calcfscore, must be
handled inside of the algorithm are through other functions that are not 
on the node it self.
You will be given he node and graph class that will be used to test
your algorithm. You are not to modify any of the contents of these classes

When you are ready to test. You need to import the UnitTest module
from the file AStarTest,py. Then you will need to create an instance of 
the UnitTest class and give it the argument of the name of the file you will
be testing against(This file will be provided). Once you have an instace of this class
created invoke the function testastar and pass your algorithm function into it
ex. 
	test = UnitTest("test.txt")
	test.gentestcases()
	a = test.testastar(algorithm)
	
The testastar function will return a list of boolean values stating if you passed a test
or not. If you whish to see the test results there will be a new file created in your local
directory that has all the test cases with the your results and the expected results.

Important Information:
All tests will be performed on a graph size 10 x 10.