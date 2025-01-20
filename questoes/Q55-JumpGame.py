class Solution:
    def canJump(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                print(f"Parado no índice {i}, valor {nums[i]}")
        return False


