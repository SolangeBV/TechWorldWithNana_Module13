from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, lectures_to_attend):
        super().__init__(first_name, last_name, age)
        self.lectures_to_attend = lectures_to_attend

    def get_lectures_to_attend(self):
        print(self.lectures_to_attend)

    def add_lecture_to_attend(self, new_lecture):
        self.lectures_to_attend.append(new_lecture)

    def remove_lecture_from_attend(self, lecture_to_remove):
        self.lectures_to_attend.remove(lecture_to_remove)
