from math import dist

data = [tuple(map(float, point.split())) for point in open('27/7/27.txt')]
count_points = len(data)
count_clusters = 5


def get_centroinds(cluster: list[tuple[float, float]]) -> tuple: 
    res: list[tuple[int, tuple[float, float]]] = []
    for point_1 in cluster: 
        dist_to_other_points = 0
        for point_2 in cluster: 
            dist_to_other_points += dist(point_1, point_2)
        res.append(tuple([dist_to_other_points, point_1]))
    return min(res)[1]
        


min_dist = 2
clusters = []
while data: 
    clusters += [[data.pop()]]
    for point in clusters[-1]: 
        n = [p for p in data if dist(p, point) < min_dist]
        clusters[-1] += n
        for p in n: 
            data.remove(p)
    
assert len(clusters) == count_clusters
assert sum([len(cluster) for cluster in clusters]) == count_points

centroids = [get_centroinds(cluster=cluster) for cluster in clusters]




print(int(10_000 * (sum(p[0] for p in centroids) / len(centroids))), int(10_000 * (sum(p[1] for p in centroids) / len(centroids))))