#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv 


def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and grid.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        x_coord = list()
        y_coord = list()
        for l in lines:
            new_point=[float(f) for f in l.split(",")]
            x_coord.append(new_point[0])
            y_coord.append(new_point[1])
        min_x=min(x_coord)
        max_x=max(x_coord)
        min_y=min(y_coord) 
        max_y=max(y_coord)
        cell_size=0.7071067811865475*distance
        grid=[[ [] for _ in range(int((max_y-min_y)/cell_size)+1) ] for _ in range(int((max_x-min_x)/cell_size)+1)]
        visited=[[ False for _ in range(int((max_y-min_y)/cell_size)+1) ] for _ in range(int((max_x-min_x)/cell_size)+1)]
        to_visit=set()
        for i in range(len(x_coord)):
            idx_x=int((x_coord[i]-min_x)/cell_size)
            idx_y=int((y_coord[i]-min_y)/cell_size)
            grid[idx_x][idx_y].append((x_coord[i], y_coord[i]))
            to_visit.add((idx_x, idx_y))
    return distance**2, grid, to_visit, visited


def visit(grid, i, j, visited, distance, max_x_idx, max_y_idx):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    if not grid[i][j] or visited[i][j]:
        return 0
    visited[i][j]=True
    size=len(grid[i][j])
    left_bound_y=max(0, j-1)
    right_bound_y=min(max_y_idx, j+2)
    x=max(0, i-2)
    for y in range(left_bound_y, right_bound_y):
        if connection(grid, i, j, x, y, distance):
            size+=visit(grid, x, y, visited, distance, max_x_idx, max_y_idx)
    for x in range(max(0, i-1), min(max_x_idx, i+2)):
        for y in range(max(0, j-2), min(max_y_idx, j+3)):
            if connection(grid, i, j, x, y, distance):
                size+=visit(grid, x, y, visited, distance, max_x_idx, max_y_idx)
    x=min(max_x_idx-1, i+2)
    for y in range(left_bound_y, right_bound_y):
            if connection(grid, i, j, x, y, distance):
                size+=visit(grid, x, y, visited, distance, max_x_idx, max_y_idx)
    return size

                
def connection(grid, i, j, x, y, distance):
    """
    returns whether some points of grid[i][j] and grid[x][y] are connected
    """
    for p in grid[i][j]:
        for q in grid[x][y]:
            if (p[0]-q[0])**2+(p[1]-q[1])**2 <= distance:
                return True
    return False



def print_components_sizes(distance, grid, to_visit, visited):
    """
    prints the sizes of the connected components in decreasing order
    """
    components_sizes=list()
    max_x_idx=len(grid)
    max_y_idx=len(grid[0])
    for i, j in to_visit:
        if not visited[i][j]:
            components_sizes.append(visit(grid, i, j, visited, distance, max_x_idx, max_y_idx))
    components_sizes.sort(reverse=True)
    print(components_sizes)

def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        distance, grid, to_visit, visited = load_instance(instance)
        print_components_sizes(distance, grid, to_visit, visited)


main()
