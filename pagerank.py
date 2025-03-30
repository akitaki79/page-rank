import numpy as np

L = np.array([
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0]
])

n = L.shape[0]

M = np.zeros((n, n))
for i in range(n):
    column_sum = np.sum(L[:, i])
    if column_sum != 0:
        M[:, i] = L[:, i] / column_sum
    else:
        M[:, i] = np.ones(n) / n  # Handle dead-end pages

d = 0.85

teleportation = np.ones((n, n)) / n

A = d * M + (1 - d) * teleportation

page_rank = np.ones(n) / n

# Calculate the PageRank by iteratively applying the PageRank formula
for _ in range(200):
    page_rank = np.dot(A, page_rank)

print("PageRank:", page_rank)




