# Feito utilizando set pois a operação "in" dentro de um set é em tempo constante. Por isso usar set em vez de lista.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
