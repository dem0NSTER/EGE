from turtle import *
from math import dist
data = [tuple(map(float, point.split())) for point in open('27/16/27.txt')]

count_of_points = len(data)
count_clusters = 3
count_not_clusters = 3
max_dist = 1


def visual(clusters): 
    up()
    tracer(0)
    screensize(5000, 5000)
    k = 50
    colors = ['red', 'green'] + ['black'] * 100

    for color, cluster in zip(colors, clusters): 
        for point in cluster: 
            x, y = *point, 
            goto(x * k, y * k)
            if color == 'black': 
                dot(10, color)
            else: 
                dot(4, color)
    done()


def get_centroid(cluster): 
    res = []

    for point in cluster: 
        sum_dist = sum(dist(point, p) for p in cluster)
        res.append([sum_dist, point])
    return min(res)[1]


clusters = []
while data: 
    clusters.append([data.pop()])
    for point in clusters[-1]: 
        n = [p for p in data if dist(p, point) < max_dist]
        clusters[-1] += n
        for p in n: 
            data.remove(p)


print(count_of_points)

assert sum([len(cl) for cl in clusters]) == count_of_points
assert len(clusters) == (count_clusters + count_not_clusters)

clusters = [cl for cl in clusters if len(cl) > 10]

assert len(clusters) == count_clusters

centroids = [get_centroid(cl) for cl in clusters]

px = sum([x for x, y in centroids]) / count_clusters
py = sum([y for x, y in centroids]) / count_clusters

print(int(px * 100_000), int(py * 100_000))
