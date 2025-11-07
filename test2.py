import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

# Step 1: Centroid Decomposition Preparation
size = [0] * N
dead = [False] * N

def dfs_size(v, p):
    size[v] = 1
    for u in tree[v]:
        if not dead[u] and u != p:
            dfs_size(u, v)
            size[v] += size[u]

def find_centroid(v, p, total):
    for u in tree[v]:
        if not dead[u] and u != p and size[u] > total // 2:
            return find_centroid(u, v, total)
    return v

# dist_to_centroid[v] = list of (centroid, dist)
dist_to_centroid = [[] for _ in range(N)]

def dfs_dist(v, p, depth, centroid):
    dist_to_centroid[v].append((centroid, depth))
    for u in tree[v]:
        if not dead[u] and u != p:
            dfs_dist(u, v, depth + 1, centroid)

def decompose(v):
    dfs_size(v, -1)
    c = find_centroid(v, -1, size[v])
    dead[c] = True
    dfs_dist(c, -1, 0, c)
    for u in tree[c]:
        if not dead[u]:
            decompose(u)
    return c

decompose(0)

# Step 2: Handle updates and queries
INF = 10**9
best = [INF] * N
is_white = [False] * N

def update(v):
    # Toggle color
    is_white[v] = not is_white[v]
    for c, d in dist_to_centroid[v]:
        if is_white[v]:
            best[c] = min(best[c], d)
        else:
            # Recompute this centroid’s best if it had v as contributor
            best[c] = INF
            for i in range(N):
                if is_white[i]:
                    for cc, dd in dist_to_centroid[i]:
                        if cc == c:
                            best[c] = min(best[c], dd)

def query(v):
    res = INF
    for c, d in dist_to_centroid[v]:
        res = min(res, best[c] + d)
    return -1 if res == INF else res

# Step 3: Process queries
Q = int(input())
for _ in range(Q):
    t, x = map(int, input().split())
    x -= 1
    if t == 0:
        update(x)
    else:
        print(query(x))
