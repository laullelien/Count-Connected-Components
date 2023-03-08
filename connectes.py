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
        points = [[[] for _ in range(int(1/distance)+1)]
                  for _ in range(int(1/distance)+1)]
        for l in lines:
            point = Point([float(f) for f in l.split(",")])
            points[int(point.coordinates[0]/distance)
                   ][int(point.coordinates[1]/distance)].append(point)
            to_visit.add(
                (int(point.coordinates[0]/distance), int(point.coordinates[1]/distance)))
    return distance, points, to_visit


def explore(points, i, j, visited, distance):
    """
    Retourne le nombre d'éléments de la composante connexe des points de points[i][j]
    """
    if not points[i][j] or visited[i][j]:
        return 0
    visited[i][j] = True
    group_elements = len(points[i][j])
    max_idx = len(points) - 1
    if i != 0:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i-1][j]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i-1, j, visited, distance)
                break
    if i != max_idx:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i+1][j]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i+1, j, visited, distance)
                break
    if j != 0:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i][j-1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i, j-1, visited, distance)
                break
    if j != max_idx:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i][j+1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i, j+1, visited, distance)
                break
    if i != max_idx and j != 0:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i+1][j-1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i+1, j-1, visited, distance)
                break
    if i != max_idx and j != max_idx:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i+1][j+1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i+1, j+1, visited, distance)
                break
    if i != 0 and j != 0:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i-1][j-1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i-1, j-1, visited, distance)
                break
    if i != 0 and j != max_idx:
        found = False
        for p1 in points[i][j]:
            for p2 in points[i-1][j+1]:
                if p1.distance_to(p2) <= distance:
                    found = True
                    break
            if found:
                group_elements += explore(points, i-1, j+1, visited, distance)
                break

    return group_elements


def print_components_sizes(distance, points, to_visit):
    """
    affichage des tailles triees de chaque composante
    """
    visited = [[False for _ in range(int(1/distance)+1)]
               for _ in range(int(1/distance)+1)]
    group_nb = []
    for i, j in to_visit:
        if not visited[i][j] and points[i][j]:
            group_nb.append(explore(points, i, j, visited, distance))
    group_nb.sort(reverse=True)
    print(group_nb)


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points, to_visit = load_instance(instance)
        print_components_sizes(distance, points, to_visit)


main()
