def pagerank(graph):
    #initialises values to be used in the pagerank algorithm
    n = len(graph.nodes)
    init = 1.0/n
    ranks = dict(zip(graph.get_nodes(), [init] * n))

    new_ranks = ranks
    #calculates new rank
    for node, prev in ranks.items():
        rank_sum = 0.0
        #iterates through incoming nodes
        for incoming in node.inbound:
            numerator = ranks[incoming]
            denominator = len(incoming.outbound) # denominator is the number of nodes leaving incoming nodes
            ta = numerator / denominator

            #score transfer
            new_ranks[incoming] = new_ranks[incoming] - ta
            rank_sum = rank_sum + ta

        new_ranks[node] = ranks[node] + rank_sum

    ranks = new_ranks

    return ranks
    