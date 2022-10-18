import random


class Employee:

    def attendance(self):
        """
        Function checks employee attendance
        :return: Employee Attendance
        """
        is_present = 1
        emp_check = random.randrange(0, 2)
        if emp_check == is_present:
            print("Employee is present")
        else:
            print("Employee is absent")


if __name__ == "__main__":
    emp = Employee()
    emp.attendance()
