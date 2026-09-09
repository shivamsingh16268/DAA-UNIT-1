def compare_bubble_insertion(random_data, sorted_data, reverse_data):

    # Bubble Sort
    def bubble_sort(arr):
        a = arr[:]
        n = len(a)
        comparisons = 0
        swaps = 0

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                comparisons += 1

                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swaps += 1
                    swapped = True

            if not swapped:
                break

        return a, comparisons, swaps

    # Insertion Sort
    def insertion_sort(arr):
        a = arr[:]
        n = len(a)
        comparisons = 0
        shifts = 0

        for i in range(1, n):
            key = a[i]
            j = i - 1

            while j >= 0:
                comparisons += 1

                if a[j] > key:
                    a[j + 1] = a[j]
                    shifts += 1
                    j -= 1
                else:
                    break

            a[j + 1] = key

        return a, comparisons, shifts

    # Datasets
    datasets = [
        ("Random Dataset", random_data),
        ("Sorted Dataset", sorted_data),
        ("Reverse Dataset", reverse_data)
    ]

    # Result
    result = ["Sorting Performance Report"]

    for name, data in datasets:
        result.append(name)

        # Bubble Sort
        b_sorted, b_comp, b_swaps = bubble_sort(data)

        result.append(
            "Bubble Sorted: " + " ".join(map(str, b_sorted))
        )
        result.append(
            "Bubble Comparisons: " + str(b_comp)
        )
        result.append(
            "Bubble Swaps: " + str(b_swaps)
        )

        # Insertion Sort
        i_sorted, i_comp, i_shifts = insertion_sort(data)

        result.append(
            "Insertion Sorted: " + " ".join(map(str, i_sorted))
        )
        result.append(
            "Insertion Comparisons: " + str(i_comp)
        )
        result.append(
            "Insertion Shifts: " + str(i_shifts)
        )

        # Compare Algorithms
        if b_comp < i_comp:
            result.append("Better Algorithm: Bubble Sort")

        elif i_comp < b_comp:
            result.append("Better Algorithm: Insertion Sort")

        else:
            result.append("Better Algorithm: Both Equal")

    return result