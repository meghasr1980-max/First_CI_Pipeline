def rotate_list(items, k):
    if not items:
        return []
    n = len(items)
    k = k % n
    return items[-k:] + items[:-k]