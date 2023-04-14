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
            new_point = [float(f) for f in l.split(",")]
            x_coord.append(new_point[0])
            y_coord.append(new_point[1])
        min_x = min(x_coord)
        max_x = max(x_coord)
        min_y = min(y_coord)
        max_y = max(y_coord)
        cell_size = (0.51*distance)
        grid = [[[] for _ in range(int((max_y-min_y)/cell_size)+1)]
                for _ in range(int((max_x-min_x)/cell_size)+1)]
        visited = [[False for _ in range(int((max_y-min_y)/cell_size)+1)]
                   for _ in range(int((max_x-min_x)/cell_size)+1)]
        to_visit = set()
        for i in range(len(x_coord)):
            idx_x = int((x_coord[i]-min_x)/cell_size)
            idx_y = int((y_coord[i]-min_y)/cell_size)
            grid[idx_x][idx_y].append((x_coord[i], y_coord[i]))
            to_visit.add((idx_x, idx_y))
    return distance**2, grid, to_visit, visited


def visit(grid, i, j, visited, distance):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    if visited[i][j]:
        return 0
    if not grid[i][j]:
        visited[i][j] = True
        return 0
    visited[i][j] = True
    max_x_idx = len(grid)
    max_y_idx = len(grid[0])
    size = len(grid[i][j])
    for x in range(i-2, i+3):
        for y in range(j-2, j+3):
            if x >= 0 and y >= 0 and x < max_x_idx and y < max_y_idx and connection(grid, i, j, x, y, distance):
                size += visit(grid, x, y, visited, distance)
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
    components_sizes = list()
    for i, j in to_visit:
        if not visited[i][j]:
            components_sizes.append(visit(grid, i, j, visited, distance))
    components_sizes.sort(reverse=True)
    print(components_sizes)
    return components_sizes


def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        distance, grid, to_visit, visited = load_instance(instance)
        return print_components_sizes(distance, grid, to_visit, visited)


main()
