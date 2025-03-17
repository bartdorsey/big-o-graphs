import time
import matplotlib.pyplot as plt
import statistics


def moving_average(data, window_size):
    """Simple moving average filter"""
    return [
        sum(data[i : i + window_size]) / window_size
        for i in range(len(data) - window_size + 1)
    ]


def remove_outliers(data, threshold=2):
    """Remove outliers using z-score"""
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    z_scores = [(x - mean) / std_dev for x in data]
    return [x for x, z in zip(data, z_scores) if abs(z) < threshold]


def plot_function_performance(
    func,
    inputs,
    func_args=None,
    func_kwargs=None,
    xlabel="Input",
    ylabel="Time (seconds)",
    title="Function Performance",
    smoothing_window=5,
    outlier_threshold=2,
):
    """
    Plot the performance of a function over a range of inputs with smoothing and outlier removal.

    Parameters:
    - func: The function to test. It should accept at least one argument.
    - inputs: An iterable of inputs to pass to the function.
    - func_args: A list of additional positional arguments to pass to the function (after the main input).
    - func_kwargs: A dictionary of keyword arguments to pass to the function.
    - xlabel, ylabel, title: Strings for labeling the plot.
    - smoothing_window: The window size for the moving average smoothing.
    - outlier_threshold: The z-score threshold for outlier removal.
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

    # Remove outliers
    times = remove_outliers(times, threshold=outlier_threshold)

    # Smooth the data using moving average
    if len(times) >= smoothing_window:
        times_smoothed = moving_average(times, smoothing_window)
    else:
        times_smoothed = times

    # Plot the execution times
    plt.figure(figsize=(10, 6))
    plt.plot(
        range(len(times_smoothed)), times_smoothed, marker="o", linestyle="-", color="b"
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
