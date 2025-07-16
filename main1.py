# f = open("C:\\Users\\usertolko\\Documents\\work_folder\\learning_python\\txt.txt")

# txt = f.readlines()

# txt.pop(0)

# coord_x = []
# coord_y = []

# for i in txt:
#     elem = i.split()
#     coord_x.append(elem[0])
#     coord_y.append(elem[1][:-2])

# for i in range(len(coord_x)):
#     coord_x[i] = coord_x[i].replace(",", ".")
#     coord_y[i] = coord_y[i].replace(",", ".")

# for i in range(len(coord_x)):
#     coord_x[i] = float(coord_x[i])
#     coord_y[i] = float(coord_y[i])

# coord_xy = dict(zip(coord_x, coord_y))

# line = 10


# cluster_0 = []
# cluster_1 = []

# for i in coord_xy.items():
#     if i[1] >= 10:
#         cluster_0.append(i)
#     else:
#         cluster_1.append(i)


# res_center = []

# # min_max = (
# #     (cluster_0[i + 1][0] - cluster_0[i][0]) ** 2
# #     + (cluster_0[i + 1][1] - cluster_0[i][1]) ** 2
# # ) ** 0.5

# minimum = 10**10
# for i in range(len(cluster_0) - 1):
#     min_sum = []
#     for _ in range(len(cluster_0) - 1):
#         x1 = cluster_0[i][0]
#         y1 = cluster_0[i][1]
#         x2 = cluster_0[i + 1][0]
#         y2 = cluster_0[i + 1][1]
#         d_a_b = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#         min_sum.append(d_a_b)
#     summm = sum(min_sum)
#     minimum = min(minimum, summm)


# print(minimum)
