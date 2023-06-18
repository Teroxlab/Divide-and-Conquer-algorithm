import math

def distance(P1, P2):

    """
    Calculate the distance between two points P1 and P2.
    """
    return math.sqrt((P1[0] - P2[0]) ** 2 + (P1[1] - P2[1]) ** 2)

def brute_force(P):
    """
    Brute-force method to find the closest pair of P in a given set.
    """
    min_DIST = float('inf')
    closest_points = ()

    n = len(P)
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(P[i], P[j])
            if dist < min_DIST:
                min_DIST = dist
                closest_points = (P[i], P[j])

    return min_DIST, closest_points

def strip_closest(strip_points, min_distance, closest_pair):
    """
    Helper function to find the closest pair of P within the strip.
    """
    n = len(strip_points)
    for i in range(n):
        j = i + 1
        while j < n and strip_points[j][1] - strip_points[i][1] < min_distance:
            dist = distance(strip_points[i], strip_points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (strip_points[i], strip_points[j])
            j += 1

    return min_distance, closest_pair


# noinspection PyGlobalUndefined
def closest_pair(points):
    """
    Divide & Conquer algorithm to find the closest pair of P in a given set.
    """
    global closest_pair
    n = len(points)

    # Base case: if there are only two or three P, use brute force
    if n <= 3:
        return brute_force(points)

    # Sort P by x-coordinate
    points_sorted_by_x = sorted(points, key=lambda point: point[0])

    # Divide the bruteForce(P) into two halves
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

    # Find the P within the strip that are closer than the minimum distance
    strip_points = [point for point in points_sorted_by_x if abs(point[0] - points[mid][0]) < min_dist]
    strip_points_sorted_by_y = sorted(strip_points, key=lambda point: point[1])

    # Check for closer pairs within the strip
    min_dist, closest_pair = strip_closest(strip_points_sorted_by_y, min_dist, closest_pair)

    # Return the closest pair and its distance
    return min_dist, closest_pair

# Test the algorithm with a sample set of P
points = [(1, 2), (5, 6), (3, 4), (9, 8), (2, 10)]
min_distance, closest_points = closest_pair(points)

print("Closest pair of P: ", closest_points)
print("Distance: ", min_distance)
