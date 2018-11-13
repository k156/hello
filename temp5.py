class Student:
    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.score = score

    def string(self):
        return "{}/{}/{}/{}".format(self.name, self.gender, self.age, self.score)

    def grading(self):
        if score > 90:
            score == A
        elif score >= 80:
            score == B
        elif score >= 70:
            score == C
        elif score >= 60:
            score == D
        else:
            score == F


students = [Student("김정민",0,28,90),
Student("김준면",1,28,92),
Student("김민석",1,29,89),
Student("김종대",1,27,79),
Student("변백현",1,27,70),
Student("김종인",1,25,82),
Student("오세훈",1,25,90),
Student("도경수",1,26,50),
Student("박찬열",1,27,85),
Student("장이씽",1,28,0),]



name_grade = map(string, students)
print(name_grade)

grd_order = sorted(students, key = lambda stu: stu.score)

def covername(self):