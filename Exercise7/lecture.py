class Lecture:
    def __init__(self, name, max_number_of_students, duration, professors):
        self.name = name
        self.max_number_of_students = max_number_of_students
        self.duration = duration
        self.professors = professors

    def get_lecture_infos(self):
        print(f"Lesson Name: {self.name}\nDuration: {self.duration}")

    def add_professors(self, new_professor):
        self.professors.append(new_professor)
