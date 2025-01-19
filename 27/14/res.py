from math import dist
from turtle import *

data = [tuple(map(float, point.split())) for point in open('27/14/27.txt')]

count_points = len(data)
max_dist = 0.8
count_clusters = 3
count_not_clusters = 3

clusters = []


def visual(clusters): 
    up()
    tracer(0)
    k = 50
    screensize(5000, 5000)

    colors = ['green', 'red', 'blue'] + ['black'] * 10
    for cluster, color in zip(clusters, colors): 
        for point in cluster: 
            x, y = *point,
            goto(x * k, y * k)
            if color == 'black': 
                dot(7, color)
            else: 
                dot(4, color)
    done()


def get_centroid(cluster): 
    res  = []

    for p1 in cluster: 
        sum_dist = sum([dist(p1, p2) for p2 in cluster])
        res.append([sum_dist, p1])
    return min(res)[1]


while data: 
    clusters.append([data.pop()])

    for point in clusters[-1]: 
        n = [p for p in data if dist(p, point) < max_dist]
        clusters[-1] += n
        for p in n: 
            data.remove(p)

assert sum([len(cl) for cl in clusters]) == count_points

visual(clusters)

not_clusters = [cl for cl in clusters if len(cl) < 10]
for cl in not_clusters: 
    clusters.remove(cl)

print([len(cl) for cl in clusters])
print([len(cl) for cl in not_clusters])

assert len(not_clusters) == count_not_clusters
assert len(clusters) == count_clusters

centroids = [get_centroid(cluster) for cluster in clusters]
print(centroids)

px = sum([x for x, y in centroids]) / count_clusters
py = sum([y for x, y in centroids]) / count_clusters

print(int(px * 100_000), int(py * 100_000))
