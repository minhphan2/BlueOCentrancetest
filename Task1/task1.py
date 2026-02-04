def dodaixuathiennhieunhat(str):
    dem_do_dai = {}

    for i in str:
        dodai =len(i)

        if dodai not in dem_do_dai:
            dem_do_dai[dodai] = 1
        else:
            dem_do_dai[dodai] += 1

    xh_nhieu_nhat = 0
    do_dai_nhieu_nhat = 0

    for dodai, soluong in dem_do_dai.items():
        if soluong > xh_nhieu_nhat:
            xh_nhieu_nhat = soluong
            do_dai_nhieu_nhat = dodai


    result = []

    for i in str:
        if len(i) == do_dai_nhieu_nhat:
            result.append(i)

    return result

## cach nhanh hon
#def dodaixuathiennhieunhat_v2(str):
#    from collections import Counter

#    dem_do_dai = Counter(len(i) for i in str)
#    do_dai_nhieu_nhat = max(dem_do_dai, key=dem_do_dai.get)

#    return [i for i in str if len(i) == do_dai_nhieu_nhat]



# Test
strings = ["a", "ab", "abc","cd", "def", "gh"]
print(dodaixuathiennhieunhat(strings))