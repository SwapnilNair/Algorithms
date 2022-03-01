def Bin(L,start,end,x,k):
    if end >start:
        mid = (start+end)//2
        if (x==L[mid]):
            j = mid
            i = mid
            while(i>-1 and L[i]==x):
                i-=1
            while(j<k and L[j]==x):
                j+=1
            return(i,j)

        elif x<L[mid]:
            return Bin(L,start,mid-1,x,k)
        else:
            return Bin(L,mid+1,end,x,k)
    else:
        return (-100,-100)

def findOccOf(L,x):
    (start,end) = Bin(L,0,len(L),x,len(L))
    if start == -100:
        return(None,None)
    else:
        return(start+1,end-1)
- - - 
def quicksort(L,l,r):
	if(r-l <=1):
		return L
	(pivot,lower,upper) = (L[l][0],l+1,l+1)
	for i in range(l+1,r):
		if L[i][0] > pivot:
			upper+=1
		else:
			(L[lower],L[i]) = (L[i],L[lower])
			(lower,upper) = (lower+1,upper+1)
	(L[l],L[lower-1]) = (L[lower-1],L[l])
	lower -=1
	quicksort(L,l,lower)
	quicksort(L,l+1,upper)
	return L


def mergeAndCount(A,B):
    (m,n) = (len(A),len(B))
    (C,i,j,k,count) = ([],0,0,0,0)
    while k < m+n :
        if i==m :
            C.extend(B[j:])
            (j,k) = (j+1,k+1)
        elif j==n :
            C.extend(A[i:])
            (i,k) = (i+1,k+1)
        elif A[i]< B[j] :
            C.append(A[i])
            (i,k) = (i+1,k+1)
        else:
            C.append(B[j])
            (j,k,count) = (j+1,k+1,count + m-i)
    return (C,count)
    
def sortAndcount(A):
    n = len(A)
    if n<=1:
        return(A,0)
    (L,countL) = sortAndcount(A[:n//2])
    (R,countR) = sortAndcount(A[n//2:])
    (B,countB) = mergeAndCount(L,R)
    return (B,countL+countR+countB)


def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


def countIntersection(A,B):
    return sortAndcount(sort_list(A,B))[1]
    
- - -
def euclidean_distance_sqr(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def column_based_sort(array, column=0):
    return sorted(array, key=lambda x: x[column])


def dis_between_closest_pair(points, points_counts, min_dis=float("inf")):
    for i in range(points_counts - 1):
        for j in range(i + 1, points_counts):
            current_dis = euclidean_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def dis_between_closest_in_strip(points, points_counts, min_dis=float("inf")):
    for i in range(min(6, points_counts - 1), points_counts):
        for j in range(max(0, i - 6), i):
            current_dis = euclidean_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, points_counts):
    # base case
    if points_counts <= 3:
        return dis_between_closest_pair(points_sorted_on_x, points_counts)

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
    points_sorted_on_x = column_based_sort(points, column=0)
    points_sorted_on_y = column_based_sort(points, column=1)
    return (closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, points_counts)) ** 0.5
    
def minDistance(points):
    return round(closest_pair_of_points(points, len(points)),2)
pts = eval(input())
timeout = 3.0  # Timeout in sec
