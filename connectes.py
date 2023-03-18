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
        points = [] 
        points=[tuple(map(float, line.split(", "))) for line in lines]
        min_x = min(p[0] for p in points) 
        max_x = max(p[0] for p in points) 
        min_y = min(p[1] for p in points) 
        max_y = max(p[1] for p in points)
        x_cells= int((max_x-min_x)/distance)+1
        y_cells= int((max_y-min_y)/distance)+1
        grid=[[ [] for _ in range(y_cells) ] for _ in range(x_cells)]
        to_visit=set(points)
        for p in points:
            idx_x=int((p[0]-min_x)/distance)
            idx_y=int((p[1]-min_y)/distance)
            grid[idx_x][idx_y].append((p[0], p[1]))
    return distance, grid, to_visit, x_cells, y_cells, min_x, min_y


def visit(distance,distance_s, grid, to_visit, x_cells, y_cells, min_x, min_y, stack):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    size=0
    stacks=dict()
    idx_x=int((stack[0][0]-min_x)/distance)
    idx_y=int((stack[0][1]-min_y)/distance)
    stacks[(idx_x, idx_y)]=stack
    while stack:
        p=stack.pop()
        size+=1
        for i in range(max(idx_x-1, 0), min(idx_x +2, x_cells)):
            for j in range(max(idx_y-1, 0), min( idx_y +2, y_cells)):
                for q in grid[i][j]:
                    if q in to_visit and is_connected(p, q, distance_s,):
                        stacks.setdefault((i, j), list()).append(q)
                        to_visit.remove(q)
    stacks.pop((idx_x, idx_y))
    for s in stacks.values():
        if s:
            size+=visit(distance,distance_s, grid, to_visit, x_cells, y_cells, min_x, min_y, s)
    return size

                
def is_connected(p, q, distance):
    return (p[0]-q[0])**2+(p[1]-q[1])**2 <= distance



def print_components_sizes(distance,distance_s, grid, to_visit, x_cells, y_cells, min_x, min_y):
    """
    prints the sizes of the connected components in decreasing order
    """
    components_sizes=list()
    while to_visit:
        components_sizes.append(visit(distance,distance_s, grid, to_visit, x_cells, y_cells, min_x, min_y, [to_visit.pop()]))
    components_sizes.sort(reverse=True)
    print(components_sizes)

def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        distance, grid, to_visit, x_cells, y_cells, min_x, min_y=load_instance(instance)
        print_components_sizes(distance, distance**2, grid, to_visit, x_cells, y_cells, min_x, min_y)


main()
