import  pytest
from students import StudentManagementSystem

@pytest.fixture
def system():
    return StudentManagementSystem(students = {
        "001": {"name": "Alice", "age": 20, "grades": {"Math": "A", "English": "B"}},
        "002": {"name": "Bob", "age": 22, "grades": {"Programming": "B", "English": "A"}}
    })

def test_add_student(system):
    print("Add function works")
    system.add_student("003", {"name": "Charlie", "age": 21, "grades": {"Math": "C", "English": "A"}})
    assert len(system.students) == 3