from turtle import *

data = [tuple(map(float, point.split())) for point in open('27/9/27.txt')]
count_of_clustres = 3
count_of_points = len(data)
min_dist = 1


def visual(clusters): 
    tracer(0)
    up()
    screensize(5000, 5000)
    k = 50
    colors = ['red', 'green']
    for cluster, color in zip(clusters, colors):
        for p in cluster: 
            x, y = *p,
            goto(x * k, y * k)
            dot(4, color)
    done()


def dist(p1, p2): 
    x1, y1, x2, y2 = *p1, *p2
    return max(abs(x1 - x2), abs(y1 - y2))


def get_centroid(cluster): 
    res = []
    for point in cluster: 
        summ = sum([dist(point, point_2) for point_2 in cluster])
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

assert len(clusters) == count_of_clustres
assert sum([len(cluster) for cluster in clusters]) == count_of_points

centroids = [get_centroid(cluster) for cluster in clusters]

px = sum(x for x, y in centroids) / count_of_clustres
py = sum(y for x, y in centroids) / count_of_clustres

print(int(10000 * px), int(10000 * py))
