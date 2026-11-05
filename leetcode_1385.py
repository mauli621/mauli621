class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for i in range(len(arr1)):  # 0 1 2
            flag = True
            for j in range(len(arr2)):  # 0 1 2 3
                if abs(arr1[i] - arr2[j]) <= d: # 4 - 10 <= 2
                    flag = False
                    break
            if flag == True:
                count += 1
        return count