def compare_search_algorithms(arr, target):

    # Linear Search
    li_in = -1
    li_comp = 0

    for i in range(len(arr)):
        li_comp += 1

        if arr[i] == target:
            li_in = i
            break

    # Binary Search
    bi_in = -1
    bi_comp = 0

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        bi_comp += 1

        if arr[mid] == target:
            bi_in = mid
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # Compare Algorithms
    if li_comp < bi_comp:
        better = "Linear Search"

    elif bi_comp < li_comp:
        better = "Binary Search"

    else:
        better = "Both Equal"

    # Result
    result = [
        "Search Comparison Report",
        "",
        "Linear Search",
        f"Index: {li_in}",
        f"Comparisons: {li_comp}",
        "",
        "Binary Search",
        f"Index: {bi_in}",
        f"Comparisons: {bi_comp}",
        "",
        f"Better Algorithm: {better}"
    ]

    return result