import math


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def brute_force_closest_pair(x, y):
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            distance = euclidean_distance((x[i], y[i]), (x[j], y[j]))
            if distance < min_distance:
                min_distance = distance
                closest_pair = ((x[i], y[i]), (x[j], y[j]))

    return closest_pair


def closest_pair(x, y):
    if len(x) <= 3:
        return brute_force_closest_pair(x, y)

    mid = len(x) // 2
    mid_point = (x[mid], y[mid])

    left_x = x[:mid]
    left_y = y[:mid]
    right_x = x[mid:]
    right_y = y[mid:]

    left_closest_pair = closest_pair(left_x, left_y)
    right_closest_pair = closest_pair(right_x, right_y)

    delta = min(euclidean_distance(left_closest_pair[0], left_closest_pair[1]),
                euclidean_distance(right_closest_pair[0], right_closest_pair[1]))

    strip = [(x[i], y[i]) for i in range(len(x)) if abs(x[i] - mid_point[0]) < delta]
    strip.sort(key=lambda point: point[1])

    closest_in_strip = None
    min_strip_distance = delta

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            distance = euclidean_distance(strip[i], strip[j])
            if distance < min_strip_distance:
                min_strip_distance = distance
                closest_in_strip = (strip[i], strip[j])

    if closest_in_strip is not None:
        return closest_in_strip
    elif euclidean_distance(left_closest_pair[0], left_closest_pair[1]) < euclidean_distance(right_closest_pair[0],
                                                                                             right_closest_pair[1]):
        return left_closest_pair
    else:
        return right_closest_pair


def input_points():
    n = int(input("Enter the number of points: "))
    print(f"Enter the {n} x-coordinates:")
    x = [float(input()) for _ in range(n)]
    print(f"Enter the {n} y-coordinates:")
    y = [float(input()) for _ in range(n)]
    return x, y


if __name__ == '__main__':
    x, y = input_points()

    closest = closest_pair(x, y)
    print(
        f"The closest pair of points is {closest} with a distance of {euclidean_distance(closest[0], closest[1]):.2f}")
