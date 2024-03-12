def triplet(n: int, nums: [int]) -> [[int]]:
    res = set()

    for i in range(len(nums)):
        hmap = set()
        for j in range(i+1, len(nums)):
            k = -(nums[i] + nums[j])
            if k in hmap:
                temp = tuple(sorted([nums[i], nums[j], k]))
                res.add(temp)

            hmap.add(nums[j])
    res = list(res)
    result = []

    for i in res:
        result.append(list(i))
    return result
    

