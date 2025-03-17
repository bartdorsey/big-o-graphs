import time
import matplotlib.pyplot as plt


def plot_function_performance(
    func,
    inputs,
    func_args=None,
    func_kwargs=None,
    xlabel="Input",
    ylabel="Time (seconds)",
    title="Function Performance",
):
    """
    Plot the performance of a function over a range of inputs.

    Parameters:
    - func: The function to test. It should accept at least one argument.
    - inputs: An iterable of inputs to pass to the function.
    - func_args: A list of additional positional arguments to pass to the function (after the main input).
    - func_kwargs: A dictionary of keyword arguments to pass to the function.
    - xlabel, ylabel, title: Strings for labeling the plot.
    """
    if func_args is None:
        func_args = []
    if func_kwargs is None:
        func_kwargs = {}

    times = []
    for input_val in inputs:
        start_time = time.time()
        func(input_val, *func_args, **func_kwargs)
        end_time = time.time()
        times.append(end_time - start_time)

    # Plot the execution times
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(inputs)), times, marker="o", linestyle="-", color="b")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
