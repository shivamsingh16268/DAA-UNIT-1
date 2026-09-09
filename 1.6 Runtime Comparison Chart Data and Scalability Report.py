def generate_runtime_chart_report(sizes):

    result = []

    # Header for chart data
    result.append("Runtime Comparison Chart Data")
    result.append(
        "InputSize LinearSearch BinarySearch BubbleSort InsertionSort"
    )

    # Data rows for each size
    for n in sizes:

        linear = n

        # floor(log2(n)) + 1 without import
        binary = 1
        temp = n

        while temp > 1:
            temp //= 2
            binary += 1

        bubble = n * (n - 1) // 2
        insertion = bubble

        result.append(
            f"{n} {linear} {binary} {bubble} {insertion}"
        )

    # Scalability Summary
    result.append("Scalability Summary")
    result.append("Algorithm Complexity Scalability")

    result.append("Linear Search O(n) Moderate")
    result.append("Binary Search O(log n) Excellent")
    result.append("Bubble Sort O(n^2) Poor")
    result.append("Insertion Sort O(n^2) Poor")

    # Key Observations
    result.append("Key Observations")
    result.append("Best Algorithm: Binary Search")
    result.append("Most Expensive Algorithm: Bubble Sort")
    result.append(
        "Conclusion: Logarithmic algorithms scale better for large inputs"
    )

    return result