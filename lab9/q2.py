def minimax_tree(depth, node_index, is_max, values):

    # If leaf node
    if depth == 3:
        return values[node_index]

    if is_max:
        return max(
            minimax_tree(depth + 1, node_index * 2, False, values),
            minimax_tree(depth + 1, node_index * 2 + 1, False, values)
        )
    else:
        return min(
            minimax_tree(depth + 1, node_index * 2, True, values),
            minimax_tree(depth + 1, node_index * 2 + 1, True, values)
        )


values = [3, 5, 2, 9, 12, 5, 23, 23]
print("Optimal Value:", minimax_tree(0, 0, True, values))
