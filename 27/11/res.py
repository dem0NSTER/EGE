from turtle import *
from math import dist

data = [tuple(map(float, point.split())) for point in open('27/11/27.txt')]

count_of_clusters = 3
max_dist = 1
count_of_points = len(data)


def visual(clusters):
    tracer(0)
    up()
    k = 20 
    colors = ['red', 'green', 'blue']
    for cluster, color in zip(clusters, colors): 
        for point in cluster: 
            x, y = *point, 
            goto(x * k, y * k)
            dot(4, color)
    done()


def get_centroid(cluster): 
    res = []
    for point in cluster: 
        summ = sum([dist(point, p) for p in cluster])
        res.append([summ, point])
    return min(res)[1]


clusters = []
while data: 
    clusters.append([data.pop()])
    for point in clusters[-1]: 
        n = [p for p in data if dist(p, point) < max_dist]
        clusters[-1] += n
        for p in n: 
            data.remove(p)


assert len(clusters) == count_of_clusters
assert sum([len(cluster) for cluster in clusters]) == count_of_points

centroids = [get_centroid(cluster) for cluster in clusters]
print(centroids)

px = sum([x for x, y in centroids]) / count_of_clusters
py = sum([y for x, y in centroids]) / count_of_clusters
print(int(px * 100_000), int(py * 100_000))

visual(clusters)
