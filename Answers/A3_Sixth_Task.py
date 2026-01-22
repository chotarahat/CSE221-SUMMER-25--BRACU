def tree_build(in_order, pre_order):
    if not in_order:
        return []

    root = pre_order[0]
    root_index = in_order.index(root)

    left_in = in_order[:root_index]
    right_in = in_order[root_index + 1:]

    left_pre = pre_order[1:1 + len(left_in)]
    right_pre = pre_order[1 + len(left_in):]

    left_post = tree_build(left_in, left_pre)
    right_post = tree_build(right_in, right_pre)

    return left_post + right_post + [root]

N = int(input())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))

post_order = tree_build(in_order, pre_order)
print(" ".join(map(str, post_order)))
