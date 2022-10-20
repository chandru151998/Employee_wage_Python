import pytest

from employee_wage_pytest import Employee, Company, Companies


@pytest.fixture
def employee():
    return Employee({"employee_name": "Chandru", "employee_wage": 20,
                     "maximum_working_hrs": 100, "maximum_working_days": 20})


@pytest.fixture
def company():
    return Company("Intellicar")


@pytest.fixture
def multiple_companies():
    return Companies()


def test_full_time(employee):
    attendence = employee.check_attendance(1)
    assert attendence == 8


def test_part_time(employee):
    attendence = employee.check_attendance(2)
    assert attendence == 4


def test_absent(employee):
    attendence = employee.check_attendance(0)
    assert attendence == 0


def test_int_attributes(employee):
    employee.calc_wage()
    assert isinstance(employee.total_wage, int)
    assert isinstance(employee.total_emp_hrs, int)
    assert isinstance(employee.total_emp_days, int)


def test_add_employee(employee, company):
    assert len(company.employee_dict) == 0
    company.add_emp(employee)
    assert len(company.employee_dict) == 1


def test_delete_emp(employee, company):
    company.add_emp(employee)
    company.delete_emp("Chandru")
    assert not company.get_emp("Chandru")


def test_multi_company_dict_length(company):
    companies = Companies()
    assert len(companies.company_dict) == 0
    companies.add_company(company)
    assert len(companies.company_dict) == 1


def test_company(company, multiple_companies):
    multiple_companies.add_company(company)
    assert company == multiple_companies.get_company_object("Intellicar")


def test_remove_company_method(company, multiple_companies):
    multiple_companies.add_company(company)
    multiple_companies.remove_company("Intellicar")
    assert not multiple_companies.get_company_object("Intellicar")
