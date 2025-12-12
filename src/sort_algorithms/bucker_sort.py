from quick_sort import quick_sort

def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if buckets is None:
        buckets = int(len(a) ** 0.5)
    bucket_list = [[] for i in range(buckets)]
    mn, mx = min(a), max(a)
    for i in a:
        ind = int((i - mn) / (mx - mn) * (buckets - 1))
        bucket_list[ind].append(i)
    sorted_a = []
    for bt in bucket_list:
        sorted_a.extend(quick_sort(bt, 0, len(bt) - 1))
    return sorted_a