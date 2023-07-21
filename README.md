# Maze-Solver

Maze Solver is a Python program that generates a maze, allows you to visualize the maze creation process, and then solves the maze using a depth-first search algorithm.

## Table of Contents

 -[Installation](#installation)
 -[Usage](#usage)
 
 ## Installation:
 1. Clone the repository: https://github.com/ejosborn/Maze-Solver

 2. Navigate to the project directory:
    cd maze-solver
 3. Install the require dependencies (if not already installed):
    pip install tkinter

## Usage
To generate and visualize a maze, run the 'main.py' script:
A window will open, showing the maze generation process. The program will use a recursive depth-first search algorithm to create the maze, breaking walls to create passages. The start and end cells will always be the top-left cell with the top wall broken for entry and bottom-right cell with the bottom wall broken for exit, respectively.

To solve the maze, press any key in the console while the maze window is open. The program will use the same depth-first search algorithm to find the path from the start cell to the end cell, drawing the solution in red. Any path that you see with a gray line leads to a 'loser cell' that isn't the end cell.

You can modify the maze size and other settings by changing the parameters in the `main.py` file.