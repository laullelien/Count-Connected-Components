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
        cell_size = 0.7071067811865475*distance
        cells = int(1/cell_size)+1
        grid = dict()
        for l in lines:
            p = tuple(map(float, l.split(", ")))
            grid.setdefault(
                (int(p[0]/cell_size), int(p[1]/cell_size)), list()).append(p)
    return distance, grid


def visit(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)
    for y in range(j-1, j+2):
        neighbour_coord = (i-2, y)
        if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
            size += visit(distance_s, grid, neighbour_coord,
                          grid.pop(neighbour_coord))
        neighbour_coord = (i+2, y)
        if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
            size += visit(distance_s, grid, neighbour_coord,
                          grid.pop(neighbour_coord))
    for y in range(j-2, j+3):
        neighbour_coord = (i-1, y)
        if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
            size += visit(distance_s, grid, neighbour_coord,
                          grid.pop(neighbour_coord))
        neighbour_coord = (i+1, y)
        if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
            size += visit(distance_s, grid, neighbour_coord,
                          grid.pop(neighbour_coord))
    for y in range(j-2, j):
        neighbour_coord = (i, y)
        if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
            size += visit(distance_s, grid, neighbour_coord,
                          grid.pop(neighbour_coord))
    for y in range(j+1, j+3):
        neighbour_coord = (i, y)
        if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
            size += visit(distance_s, grid, neighbour_coord,
                          grid.pop(neighbour_coord))
    return size


def is_connected(points, neighbour_coord, grid, distance_s):
    for p in points:
        for q in grid[neighbour_coord]:
            if (p[0]-q[0])**2+(p[1]-q[1])**2 <= distance_s:
                return True
    return False


def print_components_sizes(distance_s, grid):
    """
    prints the sizes of the connected components in decreasing order
    """
    components_sizes = list()
    while grid:
        coord, points = grid.popitem()
        components_sizes.append(visit(distance_s, grid, coord, points))
    components_sizes.sort(reverse=True)
    print(components_sizes)


def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        distance, grid = load_instance(instance)
        print_components_sizes(distance**2, grid)


main()
