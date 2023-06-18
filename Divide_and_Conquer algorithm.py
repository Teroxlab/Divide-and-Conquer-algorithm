import math


def distance(point1, point2):
    """
    Helper function to calculate the Euclidean distance between two points.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def brute_force(points):
    """
    Brute-force method to find the closest pair of points in a given set.
    """
    min_distance = float('inf')
    closest_points = ()

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_points = (points[i], points[j])

    return min_distance, closest_points


def closest_pair(points):
    """
    Divide & Conquer algorithm to find the closest pair of points in a given set.
    """
    n = len(points)

    # Base case: if there are only two or three points, use brute force
    if n <= 3:
        return brute_force(points)

    # Sort points by x-coordinate
    points_sorted_by_x = sorted(points, key=lambda point: point[0])

    # Divide the points into two halves
    mid = n // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]

    # Recursively find the closest pair in each half
    min_left_dist, closest_left = closest_pair(left_half)
    min_right_dist, closest_right = closest_pair(right_half)

    # Determine the minimum distance and closest pair between the two halves
    if min_left_dist < min_right_dist:
        min_dist = min_left_dist
        closest_pair = closest_left
    else:
        min_dist = min_right_dist
        closest_pair = closest_right

    # Find the points within the strip that are closer than the minimum distance
    strip_points = [point for point in points_sorted_by_x if abs(point[0] - points[mid][0]) < min_dist]
    strip_points_sorted_by_y = sorted(strip_points, key=lambda point: point[1])

    # Check for closer pairs within the strip
    strip_min_dist = min_dist
    strip_closest_pair = closest_pair

    for i in range(len(strip_points_sorted_by_y)):
        j = i + 1
        while j < len(strip_points_sorted_by_y) and strip_points_sorted_by_y[j][1] - strip_points_sorted_by_y[i][
            1] < strip_min_dist:
            dist = distance(strip_points_sorted_by_y[i], strip_points_sorted_by_y[j])
            if dist < strip_min_dist:
                strip_min_dist = dist
                strip_closest_pair = (strip_points_sorted_by_y[i], strip_points_sorted_by_y[j])
            j += 1

    # Return the closest pair and its distance
    if strip_min_dist < min_dist:
        return strip_min_dist, strip_closest_pair
    else:
        return min_dist, closest_pair


# Test the algorithm with a sample set of points
points = [(1, 2), (5, 6), (3, 4), (9, 8), (2, 10)]
min_distance, closest_points = closest_pair(points)

print("Closest pair of points: ", closest_points)
print("Distance: ", min_distance)
