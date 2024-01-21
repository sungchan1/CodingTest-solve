

# def get_lean(point_1, point_2):
#     if point_1[0] == point_2[0]:
#         if point_1[1] < point_2[1]:
#             return float("inf")
#         else :
#             return -float("inf")
#     else :
#         return (point_2[1]-point_1[1]) / (point_2[0]-point_1[0])


points = list()
for i in range(3):
    points.append(list(map(int, input().split())))


point_a = points[0]
point_b = points[1]
point_c = points[2]
#
# lean_a_to_b = get_lean(point_a, point_b)
# lean_b_to_c =  get_lean(point_b, point_c)

vector_a_to_b =  [point_b[0] - point_a[0], point_b[1] - point_a[1]]
vector_a_to_c = [point_c[0] - point_a[0], point_c[1] - point_a[1]]
cross_product = vector_a_to_b[0]*vector_a_to_c[1] - vector_a_to_b[1]*vector_a_to_c[0]

# # 일직선인 경우
# if lean_a_to_b == lean_b_to_c or point_a[0] == point_b[0] == point_c[0]:
#     print("0")
# # 시계 방향
# elif lean_a_to_b > lean_b_to_c:
#     print("-1")
# # 반시계 방향
# else:
#     print("1")

# 평행
if cross_product == 0:
    print("0")
# 반시계
elif cross_product > 1:
    print("1")
else:
    print("-1")