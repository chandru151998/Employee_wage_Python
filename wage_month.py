# Program to calculate Employee Wage
import random


class Employee:

    def __init__(self, name):
        self.name = name

    def wage_for_month(self):
        """
        Function calculates wage of month
        :return: Employee Wage for the month
        """
        is_full_time = 1
        is_part_time = 2
        emp_rate_per_hour = 20
        num_of_working_days = 20
        total_emp_wage = 0
        for days in range(num_of_working_days):
            emp_check = random.randrange(0, 3)
            if emp_check == is_full_time:
                emp_hrs = 8
            elif emp_check == is_part_time:
                emp_hrs = 4
            else:
                emp_hrs = 0

            emp_wage = emp_hrs * emp_rate_per_hour
            total_emp_wage += emp_wage

        print("Daily wage of {} is : {}".format(self.name, total_emp_wage))


if __name__ == "__main__":
    emp1 = Employee("Anu")
    emp2 = Employee("Ajay")
    emp1.wage_for_month()
    emp2.wage_for_month()

