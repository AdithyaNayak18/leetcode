class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Reverse strings for easier index handling
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Initialize an array to hold the results of multiplication
        product = [0] * (len(num1) + len(num2))

        # Multiply each digit and accumulate the results
        for i in range(len(num1)):
            for j in range(len(num2)):
                product[i + j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # Handle carry
                product[i + j + 1] += product[i + j] // 10
                product[i + j] %= 10

        # Remove leading zeros from the result
        while len(product) > 1 and product[-1] == 0:
            product.pop()

        # Convert the product array back to a string
        return ''.join(map(str, product[::-1]))
