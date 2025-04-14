# given array conditions
# array of 7 values [0,1,2,3,4,5,6]
# combinations -> [0,1,2],[1,2,3],[2,3,4],[3,4,5],[4,5,6]
class Solution:
    def conditions(self, arr, a, b, c):
        count = 0
        l = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if (abs(arr[i] - arr[j]) <= a and
                        abs(arr[j] - arr[k]) <= b and
                        abs(arr[i] - arr[k]) <= c):
                        l.append([arr[i], arr[j], arr[k]])
                        count += 1
        return count, l

# Create an instance of Solution
s = Solution()

# Call the method
result = s.conditions([1, 2, 3, 4, 5], 2, 3, 4)
print(result)  # Output: (number of valid triplets, list of triplets)


# ---------------------------------------------------------------------------------------

