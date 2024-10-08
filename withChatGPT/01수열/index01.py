total = 0
number = 1
limitNum = 1000

while number <= limitNum:
    total += number
    number += 1

print(f"1부터 {limitNum}까지의 합은:", total)