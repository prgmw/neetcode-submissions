# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        aux = []

        if len(pairs) == 0:
            return aux

        aux.append(pairs.copy())
        
        for item in range(1, len(pairs)):
            itr = item - 1

            while itr >=0 and pairs[itr + 1].key < pairs[itr].key:
                tmp = pairs[itr + 1]
                pairs[itr + 1] = pairs[itr]
                pairs[itr] = tmp

                itr -= 1
            
            aux.append(pairs.copy())

        return aux
        