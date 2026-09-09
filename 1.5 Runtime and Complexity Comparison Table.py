def generate_runtime_complexity_table(n):

    result = []

    result.append("Runtime Complexity Comparison")

    result.append(
        "Method ObservedCount ExpectedComplexity Observation"
    )

    # Linear Search
    result.append(
        f"Linear Search {n} O(n) Grows linearly"
    )

    # Binary Search
    # floor(log2(n)) + 1 without importing math
    binary_count = 1
    temp = n

    while temp > 1:
        temp //= 2
        binary_count += 1

    result.append(
        f"Binary Search {binary_count} O(log n) Grows logarithmically"
    )

    # Bubble Sort
    bubble_count = n * (n - 1) // 2

    result.append(
        f"Bubble Sort {bubble_count} O(n^2) Grows quadratically"
    )

    # Insertion Sort
    insertion_count = n * (n - 1) // 2

    result.append(
        f"Insertion Sort {insertion_count} O(n^2) Grows quadratically"
    )

    return result