class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d, v = {}, []

        for i in arr1:
            d[i] = d.get(i, 0) + 1
        

        for i in arr2:
            for j in range(d[i]):
                v.append(i)
                d[i] -= 1

        for i in sorted(set(arr1) - set(arr2)):
                for j in range(d[i]):
                    v.append(i)
        return v