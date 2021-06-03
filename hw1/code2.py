import numpy as np


#because in this problem, we use 'Taxation' way to figure the problem
#before do it , we have to add a G-G relations to make a trap
if __name__ == '__main__':

    # Read in a directed graph, store edges
    f = open('input.txt', 'r')
    edges = [line.strip('\n').split(' ') for line in f]
    print(edges)

    # Get set of nodes based on edges
    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
    print(nodes)

    N = len(nodes)

    # Map letters node  to Arabic numerals letters
    i = 0
    node_to_num = {}
    for node in nodes:
        node_to_num[node] = i
        i += 1
    for edge in edges:
        edge[0] = node_to_num[edge[0]]
        edge[1] = node_to_num[edge[1]]
    print(edges)

    # Generate a matrix of node relationships
    S = np.zeros([N, N])
    for edge in edges:
        S[edge[1], edge[0]] = 1
    print(S)

    # Transform the matrix into a matrix that reflects pagerank,
    # that is, the probability distribution of the random surfer position is represented by an n-dimensional column vector

    for j in range(N):
        sum_of_col = sum(S[:, j])
        for i in range(N):
            S[i, j] /= sum_of_col
    print(S)


    # Start iteration and calculate the final pagerank value
    beta = 0.8    #its beta ,we will use it later
    P_n = np.ones(N) / N   #its Vo
    e_1 = np.ones(N) / N
    P_n1 = np.zeros(N)


    e = 100000  # Set the initial error to 10000
    k = 0  # times of iteration
    print('loop...')
    while e > 0.00000001:  # it comes to an end when e  is very small

        P_n1 = (beta*np.dot(S, P_n)) + (1-beta)*e_1
        # v' = betaMv + (1 - beta)e/n   beta:beta, M:S , v:P_n ,  e/n:e_1

        e = P_n1 - P_n
        e = max(map(abs, e))  # caculate e(error)
        P_n = P_n1
        k += 1
        print('iteration %s:' % str(k), P_n1)
    print('-------------final result-------------')
    j = 0
    for i in P_n1:
        print('PageRank(%s)：' %nodes[j],i)
        j+=1