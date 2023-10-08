class Human():
    def __init__(self, name, last_name, gender):
        self.name = name
        self.last_name = last_name
        self.gender = gender

    def changesome(self, what, value):
        if what == "name":
            self.name = value
        elif what == "last_name":
            self.last_name = value
        elif what == "gender":
            self.gender = value

    def printall(self):
        print(self.name + ' ' + self.last_name + ' ' + self.gender)


class Study():
    def __init__(self, bal, faculty, age, faculty2='None'):
        self.bal = bal
        self.faculty = faculty
        self.age = age
        self.faculty2 = faculty2

    def ch_addfaculty(self, whatfac, whatwrfac):
        if whatfac == "faculty" or whatfac == "faculty1" or whatfac == "faculty 1":
            self.faculty = whatwrfac
        if whatfac == "faculty2":
            self.faculty2 = whatwrfac

    def printstudy(self):
        if self.faculty2 == 'None':
            print(self.bal + ' ' + self.faculty + ' ' + self.age)
        else:
            print(self.bal + ' ' + self.faculty + ' ' + self.age + ' ' + self.faculty2)


class Profession():
    def __init__(self, prof, wanna_prof, experience):
        self.prof = prof
        self.wanna_prof = wanna_prof
        self.experience = experience

    def changeprof(self, new_prof):
        self.prof = new_prof


class Adult(Human, Study, Profession):
    def __init__(self, name, last_name, gender, bal, faculty, age, faculty2, prof, wanna_prof, experience):
        super().__init__(name, last_name, gender)
        Study.__init__(self, bal, faculty, age, faculty2)
        Profession.__init__(self, prof, wanna_prof, experience)

    def printadult(self):
        print(f"{self.name}, {self.last_name}, {self.gender}, {self.bal}, {self.faculty}, {self.age}, {self.faculty2}, {self.prof}, {self.wanna_prof}, {self.experience}")


Adult1 = Adult("Mykhailo", "Knysh", "male", 100, "Finance", 20, "Yurystyka", "Bukhalter", "Yuryst", 2)
Adult1.printadult()
