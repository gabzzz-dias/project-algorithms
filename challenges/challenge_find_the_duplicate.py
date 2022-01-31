def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    for x in nums:
        if type(x) != int or x < 0:
            return False

        result = [x for x in nums if nums.count(x) > 1]

        if len(result) > 0:
            return result[0]
        else:
            return False
