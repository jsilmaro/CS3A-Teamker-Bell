from concurrent.futures import ProcessPoolExecutor


def compute_payroll(employee):
    name, salary = employee

 
    sss = salary * 0.045
    philhealth = salary * 0.03
    pagibig = salary * 0.02
    withholding_tax = salary * 0.10

  
    total_deduction = sss + philhealth + pagibig + withholding_tax

    
    net_salary = salary - total_deduction

    return {
        "name": name,
        "gross_salary": salary,
        "total_deduction": total_deduction,
        "net_salary": net_salary
    }


if __name__ == "__main__":
    
    employees = [
        ("John", 30000),
        ("Shane", 35000),
        ("Mars", 40000),
        ("Bane", 45000),
        ("Romeo dilikado makatigbas", 50000),
    ]

    
    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

    
    for result in results:
        print("====================================")
        print(f"Employee: {result['name']}")
        print(f"Gross Salary: {result['gross_salary']:.2f}")
        print(f"Total Deduction: {result['total_deduction']:.2f}")
        print(f"Net Salary: {result['net_salary']:.2f}")
        print("====================================")
