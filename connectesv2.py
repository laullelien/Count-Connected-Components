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
        cells_x= int(1/distance)+1
        cells_y= int(1/distance)+1
        grid=[[ [] for _ in range(cells_y) ] for _ in range(cells_x)]
        points=[tuple(map(float, line.split(", "))) for line in lines]     
        to_visit=set(points)
        for p in points:
            grid[int(p[0]/distance)][int(p[1]/distance)].append(p)
    return distance, grid, to_visit, cells_x, cells_y


def visit(distance,distance_s, grid, to_visit, cells_x, cells_y, stack):
    """
    returns the size of the connecting components containing the point in stack
    """
    size=0
    stacks=dict()
    grid_x=int((stack[0][0])/distance)
    grid_y=int((stack[0][1])/distance)
    stacks[(grid_x, grid_y)]=stack
    while stack:
        p=stack.pop()
        size+=1
        for i in range(max(grid_x-1, 0), min(grid_x +2, cells_x)):
            for j in range(max(grid_y-1, 0), min( grid_y +2, cells_y)):
                for q in grid[i][j]:
                    if q in to_visit and (p[0]-q[0])**2+(p[1]-q[1])**2 <= distance_s:
                        stacks.setdefault((i, j), list()).append(q)
                        to_visit.remove(q)
                        grid[i][j].remove(q)
    stacks.pop((grid_x, grid_y))
    for s in stacks.values():
        if s:
            size+=visit(distance,distance_s, grid, to_visit, cells_x, cells_y, s)
    return size


def print_components_sizes(distance,distance_s, grid, to_visit, cells_x, cells_y):
    """
    prints the sizes of the connected components in decreasing order
    """
    components_sizes=list()
    n=0
    while to_visit:
        n+=1
        components_sizes.append(visit(distance,distance_s, grid, to_visit, cells_x, cells_y, [to_visit.pop()]))
    components_sizes.sort(reverse=True)
    print(components_sizes, len(components_sizes))

def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        distance, grid, to_visit, cells_x, cells_y=load_instance(instance)
        print_components_sizes(distance, distance**2, grid, to_visit, cells_x, cells_y)


main()
