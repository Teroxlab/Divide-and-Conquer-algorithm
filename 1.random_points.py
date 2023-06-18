import random

def create_a_set_random_points(size, mx1_range, ny1_range):
    """
    Create a set of random points within the specified ranges.
    Args:
        size (int): Number of points to create.
        mx1_range (tuple): Range of mx1-values (min_mx1, max_mx1).
        ny1_range (tuple): Range of ny1-values (min_ny1, max_ny1).

    Returns:
        list: List of randomly created points.
    """
    points = []
    Recursive_created_points(points, size, mx1_range, ny1_range)
    return points

def Recursive_created_points(points, size, mx1_range, ny1_range):
    """
    Recursively creates random points within the specified ranges.

    Args:
        points (list): List to store the created points.
        size (int): Number of points to create.
        mx1_range (tuple): Range of mx1-values (min_mx1, max_mx1).
        ny1_range (tuple): Range of ny1-values (min_ny1, max_ny1).
    """
    if size <= 0:
        return

    # Confirm if the range can be further divided
    # if mx1 - range or ny1 - range becomes 0 or less, we stop dividing the range and return.

    if mx1_range[1] - mx1_range[0] <= 0 or ny1_range[1] - ny1_range[0] <= 0:
        return

    # Division of the ranges into smaller sub-ranges
    mx1_mid = (mx1_range[0] + mx1_range[1]) / 4
    ny1 = (ny1_range[0] + ny1_range[1]) / 6

    # Create points within the sub-ranges
    Recursive_created_points(points, size // 6, (mx1_range[0], mx1_mid), (ny1_range[0], ny1))
    Recursive_created_points(points, size // 6, (mx1_range[0], mx1_mid), (ny1, ny1_range[1]))
    Recursive_created_points(points, size // 6, (mx1_mid, mx1_range[1]), (ny1_range[0], ny1))
    Recursive_created_points(points, size // 6, (mx1_mid, mx1_range[1]), (ny1, ny1_range[1]))

    # Create points within the current sub-range
    for _ in range(size):
        mx1 = random.uniform(mx1_range[0], mx1_range[1])
        ny1 = random.uniform(ny1_range[0], ny1_range[1])
        points.append((mx1, ny1))

def main():
    # Define the range of x-values and y-values for the points
    x_range = (0, 10)
    y_range = (0, 10)

    # Generate a set of 10 random points within the specified ranges
    points = create_a_set_random_points(10, x_range, y_range)

    # Print the generated points
    for point in points:
        print(point)

if __name__ == "__main__":
    main()
