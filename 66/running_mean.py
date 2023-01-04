import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    acc = list(itertools.accumulate(sequence))
    return [round(num / i, 2) for i, num in enumerate(acc, start=1)]


running_mean([1, 2, 3])  # [1, 1.5, 2]
