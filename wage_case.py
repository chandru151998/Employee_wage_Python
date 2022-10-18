import random


class Employee:
    def __init__(self, emp_rate_per_hr):
        self.emp_rate_per_hr = emp_rate_per_hr

    def calculate_wage(self):
        """
        Function to calculate wage
        """
        r = random.randint(0, 2)

        emp_hrs = self.get_emp_hrs(r)
        emp_wage = emp_hrs * self.emp_rate_per_hr
        print(f'Employee wage is {emp_wage}')

    def get_emp_hrs(self, r):
        """
        Function to check employee working hours
        """
        switcher = {
            0: 0,
            1: 8,
            2: 4,
        }
        return switcher.get(r)


if __name__ == '__main__':
    employee = Employee(20)
    employee.calculate_wage()
