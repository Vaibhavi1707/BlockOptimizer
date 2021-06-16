def follows_topo_order(order, adj_list):
    for u in adj_list:
        for v in u.parents:
            if v in order and order.index(v) < order.index(u):
                return False
    return True