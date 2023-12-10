import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Calcula a área máxima de um contêiner retangular formado pelas alturas fornecidas.

        Parameters:
            height (List[int]): Lista de alturas.

        Returns:
            int: Área máxima do contêiner.
        """
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
        """
        Calcula a capacidade total de armazenamento de água com base nas alturas fornecidas.

        Parameters:
            height (List[int]): Lista de alturas.

        Returns:
            float: Capacidade total de armazenamento de água em metros cúbicos.
        """
        if not height or not isinstance(height, list):
            raise ValueError("A lista de alturas fornecida é inválida.")

        s = Solution()
        max_capacity = s.maxArea(height)
        total_capacity = max_capacity * 100  # Ajuste para metros cúbicos
        return total_capacity

    def plotTerrainHeight(self, height: list[int]) -> None:
        """
        Gera um gráfico de barras para visualizar a altura do terreno.

        Parameters:
            height (List[int]): Lista de alturas.

        Returns:
            None
        """
        if not height or not isinstance(height, list):
            raise ValueError("A lista de alturas fornecida é inválida.")

        plt.bar(np.arange(len(height)), height, color='blue')
        plt.title(f"Altura do Terreno - Capacidade: {self.calculateTotalCapacity(height):.2f} metros cúbicos")
        plt.xlabel("Posição")
        plt.ylabel("Altura (m)")
        plt.show()

user_height = input("Digite a altura do terreno em metros (separe os valores por espaço): ")
height = [int(h) for h in user_height.split()]

s = Solution()

try:
    total_capacity = s.calculateTotalCapacity(height)
    print("A capacidade máxima de armazenamento de água do reservatório é de:", total_capacity, "metros cúbicos")
except ValueError as e:
    print("Erro:", str(e))

try:
    s.plotTerrainHeight(height)
except ValueError as e:
    print("Erro:", str(e))

