def dist(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def colsort(array, column=0):
    return sorted(array, key=lambda x: x[column])


def bruteforce(points, points_counts, min_dis=float("inf")):
    for i in range(points_counts - 1):
        for j in range(i + 1, points_counts):
            current_dis = dist(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def dis_between_closest_in_strip(points, points_counts, min_dis=float("inf")):
    for i in range(min(6, points_counts - 1), points_counts):
        for j in range(max(0, i - 6), i):
            current_dis = dist(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, points_counts):
    # base case
    if points_counts <= 3:
        return bruteforce(points_sorted_on_x, points_counts)

    # recursion
    mid = points_counts // 2
    closest_in_left = closest_pair_of_points_sqr(
        points_sorted_on_x, points_sorted_on_y[:mid], mid
    )
    closest_in_right = closest_pair_of_points_sqr(
        points_sorted_on_y, points_sorted_on_y[mid:], points_counts - mid
    )
    closest_pair_dis = min(closest_in_left, closest_in_right)
    cross_strip = []
    for point in points_sorted_on_x:
        if abs(point[0] - points_sorted_on_x[mid][0]) < closest_pair_dis:
            cross_strip.append(point)

    closest_in_strip = dis_between_closest_in_strip(
        cross_strip, len(cross_strip), closest_pair_dis
    )
    return min(closest_pair_dis, closest_in_strip)


def closest_pair_of_points(points, points_counts):
    points_sorted_on_x = colsort(points, column=0)
    points_sorted_on_y = colsort(points, column=1)
    return (closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, points_counts)) ** 0.5
    
def minDistance(points):
    return round(closest_pair_of_points(points, len(points)),2)
pts = eval(input())
timeout = 3.0  # Timeout in sec
