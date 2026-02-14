from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
import threading

employee_name = "Alice"
salary = 25000

DEDUCTIONS = {
    "SSS": 0.045,
    "PhilHealth": 0.025,
    "Pag-IBIG": 0.02,
    "Withholding Tax": 0.10
}

def compute_deduction(label, rate, salary):
    thread = threading.current_thread().name
    amount = salary * rate
    print(f"[{thread}] Processing {label} at {rate*100:.1f}%")
    return label, amount


print(f"\nPayroll Breakdown for {employee_name}")
print(f"Gross Salary: {salary:,.2f}\n")

results = {}

with ThreadPoolExecutor(max_workers=len(DEDUCTIONS)) as executor:
    
    futures = [
        executor.submit(compute_deduction, label, rate, salary)
        for label, rate in DEDUCTIONS.items()
    ]

    for future in as_completed(futures):
        label, amount = future.result()
        results[label] = amount

total_deduction = sum(results.values())

print("\n--- Deduction Summary ---")
for label, amount in results.items():
    print(f"{label:<18}: {amount:,.2f}")

print("-" * 30)
print(f"{'Total Deduction':<18}: {total_deduction:,.2f}")
print(f"{'Net Salary':<18}: {salary - total_deduction:,.2f}")
