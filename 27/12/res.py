from math import dist
from turtle import *
data = [tuple(map(float, point.split())) for point in open('27/12/27.txt')]

count_of_points = len(data)
count_of_clusters = 3
max_dist = 1

clusters = []


def get_centroid(cluster): 
    res = []

    for point in cluster: 
        sum_dist = sum([dist(p, point) for p in cluster])
        res.append([sum_dist, point])
    return min(res)[1]


def visual(clusters): 
    tracer(0)
    screensize(5000, 5000)
    up()
    k = 50
    colors = ['red', 'green', 'blue']

    for cluster, color in zip(clusters, colors): 
        for point in cluster:
            x, y = *point,
            goto(x * k, y * k)
            dot(4, color)
    done()


while data: 
    clusters.append([data.pop()])
    for point in clusters[-1]: 
        n = [p for p in data if dist(p, point) < max_dist]
        clusters[-1] += n
        for p in n: 
            data.remove(p)


assert sum([len(cl) for cl in clusters]) == count_of_points
assert len(clusters) == count_of_clusters

visual(clusters)

centroids = [get_centroid(cluster) for cluster in clusters]

px = sum([x for x, y in centroids]) / count_of_clusters
py = sum([y for x, y in centroids]) / count_of_clusters

print(int(px * 100_000), int(py * 100_000))
