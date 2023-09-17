distance_height_list = []
height = 100.0
for i in range(10):
    if(i == 0):
        distance_height_list.append(height)
    else:
        distance_height_list.append(height * 2)
    height = height / 2
print("總共經歷 {} 公分".format(sum(distance_height_list)))
print("第 10 次反彈後有 {} 公分".format(height))
