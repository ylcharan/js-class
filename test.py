import sys
sys.setrecursionlimit(1000005)

# --- Persistent Segment Tree Implementation ---

MAX_W = 100005

class Node:
    __slots__ = ['left', 'right', 'count']

    def __init__(self, count=0):
        self.left = None
        self.right = None
        self.count = count

def insert(node, l, r, val):
    new_node = Node(node.count + 1)
    if l == r:
        return new_node
    mid = (l + r) // 2
    if val <= mid:
        new_node.left = insert(node.left if node.left else Node(), l, mid, val)
        new_node.right = node.right
    else:
        new_node.left = node.left
        new_node.right = insert(node.right if node.right else Node(), mid + 1, r, val)
    return new_node

def query(node_u, node_v, node_lca, node_parent_lca, l, r, k):
    if l == r:
        return l
    mid = (l + r) // 2
    # Count the elements in the left half of the range
    count_left = (node_u.left.count if node_u.left else 0) + \
                 (node_v.left.count if node_v.left else 0) - \
                 (node_lca.left.count if node_lca.left else 0) - \
                 (node_parent_lca.left.count if node_parent_lca.left else 0)
    
    if k <= count_left:
        # k-th element is in the left half
        return query(node_u.left if node_u.left else Node(), 
                     node_v.left if node_v.left else Node(), 
                     node_lca.left if node_lca.left else Node(), 
                     node_parent_lca.left if node_parent_lca.left else Node(), 
                     l, mid, k)
    else:
        # k-th element is in the right half, adjust k
        return query(node_u.right if node_u.right else Node(), 
                     node_v.right if node_v.right else Node(), 
                     node_lca.right if node_lca.right else Node(), 
                     node_parent_lca.right if node_parent_lca.right else Node(), 
                     mid + 1, r, k - count_left)

# --- LCA Precomputation (Binary Lifting) ---

MAX_LOG = 18 # Sufficient for N <= 100000 (2^17 ~ 131072)
parent = [[0] * MAX_LOG for _ in range(100001)]
depth = [0] * 100001

def dfs_lca(u, p, d, adj):
    depth[u] = d
    parent[u][0] = p
    for i in range(1, MAX_LOG):
        if parent[u][i-1] != 0:
            parent[u][i] = parent[parent[u][i-1]][i-1]
        else:
            parent[u][i] = 0
    for v in adj[u]:
        if v != p:
            dfs_lca(v, u, d + 1, adj)

def get_lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for i in range(MAX_LOG - 1, -1, -1):
        if (diff >> i) & 1:
            u = parent[u][i]
    if u == v:
        return u
    for i in range(MAX_LOG - 1, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]
    return parent[u][0]

# --- Main Logic ---

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        
        parts = list(map(int, line.split()))
        if not parts:
            return
        
        N, M = parts
        if N == 0:
            return

        weights = [0] + list(map(int, sys.stdin.readline().split()))
        
        # Coordinate Compression
        sorted_weights = sorted(list(set(weights[1:])))
        weight_map = {val: i + 1 for i, val in enumerate(sorted_weights)}
        compressed_weights = [0] * (N + 1)
        for i in range(1, N + 1):
            compressed_weights[i] = weight_map[weights[i]]
        W = len(sorted_weights)

        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)
        
        # Build Persistent Segment Tree with DFS
        # roots[i] stores the root of PST for path root to node i
        roots = [None] * (N + 1)
        roots[0] = Node() # Dummy root for parent of actual root
        
        def dfs_pst(u, p, root_p):
            # Create a new version of PST for node u by inserting its compressed weight
            roots[u] = insert(root_p, 1, W, compressed_weights[u])
            for v in adj[u]:
                if v != p:
                    dfs_pst(v, u, roots[u])
        
        # Build LCA table and PST
        dfs_lca(1, 0, 0, adj)
        dfs_pst(1, 0, roots[0])

        # Process queries
        results = []
        for _ in range(M):
            u, v, k = map(int, sys.stdin.readline().split())
            LCA_node = get_lca(u, v)
            Parent_LCA = parent[LCA_node][0]
            
            # Find the kth smallest compressed weight
            compressed_result_idx = query(roots[u], roots[v], roots[LCA_node], roots[Parent_LCA] if Parent_LCA != 0 else roots[0], 1, W, k)
            
            # Map back to original weight
            original_result = sorted_weights[compressed_result_idx - 1]
            results.append(original_result)
        
        for res in results:
            print(res)

    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    solve()
