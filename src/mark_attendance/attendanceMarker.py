
class AttendanceMarker:
    def __init__(self):
        pass

    def mark_present(self, students,subcode):
        for student in students:
            print(student.getName())
        return 1
