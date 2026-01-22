def trees_reassessed(in_order, post_order):
    if not in_order:
        return []

    root = post_order[-1]
    root_index = in_order.index(root)

    left_in = in_order[:root_index]
    right_in = in_order[root_index + 1:]

    left_post = post_order[:len(left_in)]
    right_post = post_order[len(left_in):-1]

    left_pre = trees_reassessed(left_in, left_post)
    right_pre = trees_reassessed(right_in, right_post)

    return [root] + left_pre + right_pre

N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pre_order = trees_reassessed(in_order, post_order)
print(" ".join(map(str, pre_order)))