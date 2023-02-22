class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxi = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = h * w
            maxi = max(maxi, area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return maxi

# Altura do terreno em metros
height = np.array([10, 15, 20, 25, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10, 5])

# Estimativa da capacidade de armazenamento de água
s = Solution()
max_capacity = s.maxArea(height)

# Capacidade total em metros cúbicos
total_capacity = max_capacity * 100
print("A capacidade máxima de armazenamento de água do reservatório é de:", total_capacity, "metros cúbicos")
