# se target for maior que solução, andar para direita, se for menor, andar para esquerda fim, very easy indeed.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left + 1, right + 1]
            elif result < target:
                left += 1
            else:
                right -= 1
