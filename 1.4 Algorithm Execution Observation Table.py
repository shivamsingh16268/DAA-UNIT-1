def generate_execution_observation_table(input_sizes):

    def recursive_fib_calls(n):
        if n <= 1:
            return 1

        return 1 + recursive_fib_calls(n - 1) + recursive_fib_calls(n - 2)

    result = []

    result.append("Algorithm Execution Observation Table")

    result.append(
        "InputSize RecursiveFactorial IterativeFactorial "
        "RecursiveFibonacci IterativeFibonacci LinearSearch "
        "BinarySearch BubbleSort InsertionSort"
    )

    for n in input_sizes:

        recursive_factorial = n + 1
        iterative_factorial = n

        recursive_fibonacci = recursive_fib_calls(n)
        iterative_fibonacci = n

        linear_search = n
        binary_search = n.bit_length()

        bubble_sort = n * (n - 1) // 2
        insertion_sort = n * (n - 1) // 2

        result.append(
            f"{n} {recursive_factorial} {iterative_factorial} "
            f"{recursive_fibonacci} {iterative_fibonacci} "
            f"{linear_search} {binary_search} "
            f"{bubble_sort} {insertion_sort}"
        )

    return result