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

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_1(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_2(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_3(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_4(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_5(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_6(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_7(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_8(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_9(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_10(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_11(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_12(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_13(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_14(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_15(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_16(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_17(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_18(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_19(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_1(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    return size


def visit_20(distance_s, grid, coord, points):
    """
    returns the size of the connecting components containing the points of grid[i][j]
    """
    i, j = coord
    size = len(points)

    neighbour_coord = (i-2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_2(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_3(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_4(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_5(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_6(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_7(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i-1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_8(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_9(distance_s, grid, neighbour_coord,
                        grid.pop(neighbour_coord))

    neighbour_coord = (i, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_10(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_11(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_12(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_13(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_14(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_15(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_16(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+1, j+2)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_17(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j-1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_18(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_19(distance_s, grid, neighbour_coord,
                         grid.pop(neighbour_coord))

    neighbour_coord = (i+2, j+1)
    if neighbour_coord in grid and is_connected(points, neighbour_coord, grid, distance_s):
        size += visit_20(distance_s, grid, neighbour_coord,
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
    return components_sizes


def main():
    """
    loads an instance and prints the sizes
    """
    for instance in argv[1:]:
        distance, grid = load_instance(instance)
        print_components_sizes(distance**2, grid)


main()
