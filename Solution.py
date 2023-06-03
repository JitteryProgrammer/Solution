import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def maxArea(self, height: list[int]) -> int:
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

    def calculateTotalCapacity(self, height: list[int]) -> float:
        if not height or not isinstance(height, list):
            raise ValueError("A lista de alturas fornecida é inválida.")

        s = Solution()
        max_capacity = s.maxArea(height)
        total_capacity = max_capacity * 100
        return total_capacity

    def plotTerrainHeight(self, height: list[int]) -> None:
        if not height or not isinstance(height, list):
            raise ValueError("A lista de alturas fornecida é inválida.")

        plt.bar(np.arange(len(height)), height, color='blue')
        plt.title("Altura do terreno")
        plt.xlabel("Posição")
        plt.ylabel("Altura (m)")
        plt.show()


# Altura do terreno em metros
height = np.array([10, 15, 20, 25, 30, 25, 20, 15, 10, 5, 10, 15, 20, 25, 30, 25, 20, 15, 10, 5])

# Criando uma instância da classe Solution
s = Solution()

# Calculando a capacidade total de armazenamento de água
try:
    total_capacity = s.calculateTotalCapacity(height)
    print("A capacidade máxima de armazenamento de água do reservatório é de:", total_capacity, "metros cúbicos")
except ValueError as e:
    print("Erro:", str(e))

# Criando o gráfico de barras para visualizar a altura do terreno
try:
    s.plotTerrainHeight(height)
except ValueError as e:
    print("Erro:", str(e))

