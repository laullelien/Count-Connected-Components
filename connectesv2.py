#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv
from time import time
import itertools
from functools import cache


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
        cell_size=distance
        grid=[[ [] for _ in range(int((max_y-min_y)/cell_size)+1) ] for _ in range(int((max_x-min_x)/cell_size)+1)]
        visited=[[ False for _ in range(int((max_y-min_y)/cell_size)+1) ] for _ in range(int((max_x-min_x)/cell_size)+1)]
        to_visit=set()
        for i in range(len(x_coord)):
            idx_x=int((x_coord[i]-min_x)/cell_size)
            idx_y=int((y_coord[i]-min_y)/cell_size)
            grid[idx_x][idx_y].append((x_coord[i], y_coord[i]))
            to_visit.add((idx_x, idx_y))
    return distance**2, grid, to_visit, visited


# def visit(grid, i, j, component, visited, distance, max_x_idx, max_y_idx):
#     """
#     returns the size of the connecting components containing the points of grid[i][j]
#     """
#     if visited[i][j]:
#         return 0
#     stack=[component]
#     visited[i][j]=True
#     size=len(grid[i][j])
#     for x in range(max(0, i-1), min(max_x_idx, i+2)):
#         for y in range(max(0, j-1), min(max_y_idx, j+2)):
#             if connection(grid, i, j, x, y, distance):
#                 size+=visit(grid, x, y, visited, distance, max_x_idx, max_y_idx)
#     return [len(compo) for compo in stack]

def visit(grid, i, j, stack, visited, distance, max_x_idx, max_y_idx):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    if visited[i][j]:
        return [0 for _ in range(len(stack))]
    visited[i][j]=True
    to_explore={i for i in range(len(grid[i][j]))}
    new_stack=[[] for _ in range(len(stack))]
    for idx_1, component in enumerate(stack):
        if not to_explore:
            break
        for p in component:
            if not to_explore:
                break
            for idx_2, q in enumerate(grid[i][j]):
                if idx_2 in to_explore and connected(p, q, distance):
                    new_stack[idx_1].append(p)
                    to_explore.remove(idx_2)
    for idx_1, component in enumerate(new_stack):
        if not to_explore:
            break
        for p in component:
            if not to_explore:
                break
            for idx_2, q in enumerate(grid[i][j]):
                if idx_2 in to_explore and connected(p, q, distance):
                    new_stack[idx_1].append(p)
                    to_explore.remove(idx_2)
    while to_explore:
        new_stack.append([grid[i][j][to_explore.pop()]])
        for p in new_stack[-1]:
            for idx_2, q in enumerate(grid[i][j]):
                if idx_2 in to_explore and connected(p, q, distance):
                    new_stack[-1].append(q)
                    to_explore.remove(idx_2)
    sizes=[len(stack[i]) for i in range(len(stack))]
    for x in range(max(0, i-1), min(max_x_idx, i+2)):
        for y in range(max(0, j-1), min(max_y_idx, j+2)):
            add(visit(grid, x, y, new_stack, visited, distance, max_x_idx, max_y_idx), sizes)
    return sizes


def add(sizes_1, sizes_2):
    addition= [sizes_1[i]+sizes_2[i] for i in range(len(sizes_2))]
    addition.extend(sizes_2[len(sizes_1):])
                
def connected(p, q, distance):
    """
    returns whether some points of grid[i][j] and grid[x][y] are connected
    """
    return (p[0]-q[0])**2+(p[1]-q[1])**2 <= distance



def print_components_sizes(distance, grid, to_visit, visited):
    """
    prints the sizes of the connected components in decreasing order
    """
    components_sizes=list()
    max_x_idx=len(grid)
    max_y_idx=len(grid[0])
    for i, j in to_visit:
        print(visited)
        if not visited[i][j]:
            print("c", components_sizes)
            components_sizes.extend(visit(grid, i, j, [], visited, distance, max_x_idx, max_y_idx))
    components_sizes.sort(reverse=True)
    print("over")
    print(components_sizes, len(components_sizes))

def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        t0=time()
        distance, grid, to_visit, visited = load_instance(instance)
        print(time()-t0)
        print_components_sizes(distance, grid, to_visit, visited)


main()
