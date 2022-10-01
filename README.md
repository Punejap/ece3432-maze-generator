# ece3432-maze-generator
imports a text file with maze building instructions and outputs a csv

USAGE:
Place MazeGen.py in the same directory as input .txt file

add the following code:
#import package
From MazeGen import MazeGen

#instantiate the class
mazegen = MazeGen()

#add name of txt file as argument to method 'createCSV' 
mazegen.createCSV('inputfile.txt')

INPUT
a .txt file should contain lines for a maze for use in amaze.py package

The text file should be formatted with the cell numbers separated in parentheses, followed by values of distance from the wall in order West, East, North, South.
ex:"(3, 2)",0.22,1.2,0.14,1.8
"(4, 2)",1.1,1.2,1.3,0.12
"(1, 3)",0.7,0.8,0.21,1.1
"(2, 3)",1.2,0.15,1.3,0.16

the output will automatically sort the cells in order:
  cell  	E	W	N	S
(1, 1)	0	0	0	1
(2, 1)	1	0	1	1
(3, 1)	1	0	1	0

NOTES
If the value of distance from the wall is <0.25, then the program assumes it is not a path. If that distance is >=0.25, the program assumes it is a path and places a 1.
