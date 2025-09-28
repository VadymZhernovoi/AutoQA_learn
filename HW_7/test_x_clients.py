
from HW_7.employee_api import EmployeeApi

base_url = "http://5.101.50.27:8000"


def test_change_company_name():
    employee = EmployeeApi(base_url)

    employee_json = {
        "first_name": "First",
        "last_name": "Last",
        "middle_name": "Middle",
        "company_id": 3,
        "email": "user@example.com",
        "phone": "123 456 78",
        "birthdate": "2000-04-29",
        "is_active": "true"
    }
    resp_create = employee.create_employee(employee_json)
    # assert "id" in resp_create, "Нет ключа 'id'"
    # assert "employee_id" in resp_create, "Нет ключа 'employee_id'"
    employee_id = resp_create.get('id')
    if employee_id is None: # т.к. запрос на создание employee (/employee/create) не возвращает id
        employee_id = 3     # берём id от фонаря
    old_employee = employee.get_employee(employee_id)

    print(old_employee)

    changed_employee = {
        "last_name": "Updated 111",
        "email": "updated_user@example.com",
        "phone": "876 543 21",
        "is_active": False
    }
    resp_update = employee.update_employee(employee_id, changed_employee)

    assert resp_update.get('last_name') == changed_employee['last_name']
    assert resp_update.get('email') == changed_employee['email']
    assert resp_update.get('phone') == changed_employee['phone']
    assert resp_update.get('is_active') == changed_employee['is_active']




