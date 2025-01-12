from turtle import * 

data = [tuple(map(float, point.split())) for point in open('27/10/27.txt')]

count_of_points = len(data)
count_of_clusters = 3
min_dist = 2


def visual(clusters): 
    up()
    tracer(0)
    screensize(5000, 5000)
    k = 15
    colors = ['red', 'green', 'blue']
    for cluster, color in zip(clusters, colors):
        for point in cluster: 
            x, y = *point,
            goto(x * k, y * k)
            dot(4, color)
    done()


def dist(p1, p2): 
    x1, y1, x2, y2 = *p1, *p2
    return abs(x2 - x1) + abs(y2 - y1)


def get_centroid(cluster): 
    res = []
    for p in cluster: 
        summ = sum([dist(p, p2) for p2 in cluster])
        res.append([summ, p])
    return min(res)[1]


clusters = []
while data: 
    clusters.append([data.pop()]) 
    for point in clusters[-1]: 
        n = [p for p in data if dist(p, point) < min_dist]   
        clusters[-1] += n
        for p in n: 
            data.remove(p)


assert len(clusters) == count_of_clusters
assert sum([len(cluster) for cluster in clusters]) == count_of_points


centroids = [get_centroid(cluster) for cluster in clusters]
print(centroids)

px = sum([x for x, y in centroids]) / count_of_clusters
py = sum(y for x, y in centroids) / count_of_clusters

print(int(px * 1_000), int(py * 1_000))

visual(clusters)
