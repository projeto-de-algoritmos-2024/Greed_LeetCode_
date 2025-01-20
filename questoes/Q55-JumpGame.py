class Solution:
    def canJump(self, nums):
        # Posição inicial
        current_position = 0
        
        # Enquanto houverem saltos possíveis
        while current_position < len(nums) - 1:
            max_jump = nums[current_position]
            # Se o salto atual for 0, ficamos presos
            if max_jump == 0:
                return False
            # Move para o próximo índice
            current_position += 1
        
        return True  # Supondo que sempre conseguimos chegar ao final

