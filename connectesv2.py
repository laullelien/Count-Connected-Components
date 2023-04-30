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
    evry point have coordinates between 0 and 1
    the distance is divided by sqrt(2) so that every point in a cell are connected
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        cell_size = 0.7071067811865475*distance
        grid = dict()
        for l in lines:
            p = tuple(map(float, l.split(", ")))
            grid.setdefault(
                (int(p[0]/cell_size), int(p[1]/cell_size)), list()).append(p)
    return distance, grid


def visit(distance_s, distance, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[coord] by checking each cell that is possibly connected using recursion
    there are different ways to check connection in function of the relative position of the cells
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected_1(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected_3(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected_4(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected_2(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected_1(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected_1(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected_2(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected_2(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected_1(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected_3(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected_4(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected_2(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected_1(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected_1(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected_3(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected_4(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected_3(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected_4(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected_2(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected_2(points, neighbour_coord, grid, distance_s, distance):
        size += visit(distance_s, distance, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def is_connected_1(points, neighbour_coord, grid, distance_s, distance):
    """
    the neighbour is higher than the current cell
    """
    points.sort()
    grid[neighbour_coord].sort(reverse=True)
    for p in points:
        for i, q in enumerate(grid[neighbour_coord]):
            x_dist = p[0]-q[0]
            if x_dist > distance:
                if i == 0:
                    return False
                else:
                    break
            if x_dist**2+(p[1]-q[1])**2 <= distance_s:
                return True
    return False


def is_connected_2(points, neighbour_coord, grid, distance_s, distance):
    """
    the neighbour is lower than the current cell
    """
    points.sort(reverse=True)
    grid[neighbour_coord].sort()
    for p in points:
        for i, q in enumerate(grid[neighbour_coord]):
            x_dist = q[0]-p[0]
            if x_dist > distance:
                if i == 0:
                    return False
                else:
                    break
            if x_dist**2+(p[1]-q[1])**2 <= distance_s:
                return True
    return False


def is_connected_3(points, neighbour_coord, grid, distance_s, distance):
    """
    the neighbour is to the left of the current cell
    """
    points.sort(key=lambda x: x[1])
    grid[neighbour_coord].sort(key=lambda x: x[1], reverse=True)
    for p in points:
        for i, q in enumerate(grid[neighbour_coord]):
            y_dist = p[1]-q[1]
            if y_dist > distance:
                if i == 0:
                    return False
                else:
                    break
            if (p[0]-q[0])**2+y_dist**2 <= distance_s:
                return True
    return False


def is_connected_4(points, neighbour_coord, grid, distance_s, distance):
    """
    the neighbour is to the right of the current cell
    """
    points.sort(key=lambda x: x[1], reverse=True)
    grid[neighbour_coord].sort(key=lambda x: x[1])
    for p in points:
        for i, q in enumerate(grid[neighbour_coord]):
            y_dist = q[1]-p[1]
            if y_dist > distance:
                if i == 0:
                    return False
                else:
                    break
            if (p[0]-q[0])**2+y_dist**2 <= distance_s:
                return True
    return False


def print_components_sizes(distance_s, distance, grid):
    """
    prints the sizes of the connected components in decreasing order
    """
    components_sizes = list()
    while grid:
        coord, points = grid.popitem()
        components_sizes.append(
            visit(distance_s, distance, grid, coord, points))
    components_sizes.sort(reverse=True)
    print(components_sizes)
    components_sizes


def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        distance, grid = load_instance(instance)
        print_components_sizes(distance**2, distance, grid)


main()
