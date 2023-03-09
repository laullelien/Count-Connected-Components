#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv

from geo.point import Point


def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    to_visit = set()
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in next(lines).split(",")])]
        min_x = points[0].coordinates[0]
        max_x = min_x
        min_y = points[0].coordinates[1]
        max_y = min_y
        for l in lines:
            new_point = Point([float(f) for f in l.split(",")])
            points.append(new_point)
            if new_point.coordinates[0] < min_x:
                min_x = new_point.coordinates[0]
            elif new_point.coordinates[0] > max_x:
                max_x = new_point.coordinates[0]
            if new_point.coordinates[1] < min_y:
                min_y = new_point.coordinates[1]
            elif new_point.coordinates[1] > max_y:
                max_y = new_point.coordinates[1]
        grid = [[[] for _ in range(int((max_y-min_y)/distance)+1)]
                for _ in range(int((max_x-min_x)/distance)+1)]
        for point in points:
            idx_x = int((point.coordinates[0]-min_x)/distance)
            idx_y = int((point.coordinates[1]-min_y)/distance)
            grid[idx_x][idx_y].append(point)
            to_visit.add((idx_x, idx_y))
    return distance, grid, to_visit, ((min_x, max_x), (min_y, max_y))


def explore(grid, i, j, visited, distance):
    """
    Retourne le nombre d'éléments de la composante connexe des points de grid[i][j]
    """
    if not grid[i][j] or visited[i][j]:
        return 0
    visited[i][j] = True
    group_elements = len(grid[i][j])
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    if i != 0:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i-1][j]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i-1, j, visited, distance)
                break
    if i != max_x:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i+1][j]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i+1, j, visited, distance)
                break
    if j != 0:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i][j-1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i, j-1, visited, distance)
                break
    if j != max_y:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i][j+1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i, j+1, visited, distance)
                break
    if i != max_x and j != 0:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i+1][j-1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i+1, j-1, visited, distance)
                break
    if i != max_x and j != max_y:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i+1][j+1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i+1, j+1, visited, distance)
                break
    if i != 0 and j != 0:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i-1][j-1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i-1, j-1, visited, distance)
                break
    if i != 0 and j != max_y:
        found = False
        for p1 in grid[i][j]:
            for p2 in grid[i-1][j+1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(grid, i-1, j+1, visited, distance)
                break

    return group_elements


def print_components_sizes(distance, grid, to_visit, limits):
    """
    affichage des tailles triees de chaque composante
    """
    visited = [[False for _ in range(int((limits[1][1]-limits[1][0])/distance)+1)]
               for _ in range(int((limits[0][1]-limits[0][0])/distance)+1)]
    group_nb = []
    for i, j in to_visit:
        if not visited[i][j] and grid[i][j]:
            group_nb.append(explore(grid, i, j, visited, distance))
    group_nb.sort(reverse=True)
    print(group_nb, len(group_nb), sum(group_nb))


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, grid, to_visit, limits = load_instance(instance)
        print_components_sizes(distance, grid, to_visit, limits)


main()
