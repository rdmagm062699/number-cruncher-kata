import random
from src.reporter import crunch_report

numbers = [random.randint(1, 100) for _ in range(5)]

print(f"Input:  {numbers}")
print(f"Result: {crunch_report(numbers)}")
print()
print("🎉 Congratulations! You've successfully reported on the Number Cruncher!")
