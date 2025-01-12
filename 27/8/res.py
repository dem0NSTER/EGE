from math import dist
from turtle import *

data = [tuple(map(float, points.split())) for points in open('27/8/27.txt')]
count_points = len(data)
min_dist = 0.2
count_clusters = 3


def visual(clusters): 
    k = 40
    colors = ['red', 'green']
    tracer(0); up(); i = 0; screensize(5000, 5000)
    for cluster in clusters: 
        color = colors[i]
        i += 1
        for point in cluster: 
            x, y = point
            goto(x * k, y * k)
            dot(4, color)
    done()


def get_centroid(cluster):
    res = []
    for point in cluster: 
        summ = sum([dist(p, point) for p in cluster])
        res.append([summ, point])
    return min(res)[1]


clusters = []
while data: 
    clusters.append([data.pop()])
    
    for point in clusters[-1]: 
        n = [p for p in data if dist(point, p) < min_dist]
        clusters[-1] += n
        for p in n: 
            data.remove(p)

print(len(clusters))
assert len(clusters) == count_clusters
assert sum([len(cluster) for cluster in clusters])

centroids = [get_centroid(cluster=cluster) for cluster in clusters]
print(int(10_000 * (sum([centroid[0] for centroid in centroids]) / len(clusters))), int(10_000 * (sum([centroid[1] for centroid in centroids]) / len(clusters))))

