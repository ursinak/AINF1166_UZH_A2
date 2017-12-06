from moduleElement import *

class Module(object):

    ######## CODE MISSING HERE

    def __init__(self,ects,title,semester,grade=None):
        "constructor for class module"

        self.ects = ects
        self.grade = grade
        self.title = title
        self.semester = semester

        self.dates = []

        self.elements = []

        ######## CODE MISSING HERE


    def get_important_dates_overview(self):
        "prints all the important dates for a module"

        print("Important dates for {0:s}:".format(self.title))

        for kind,date in self.dates:
            print("\t{0:s} on {1:s}".format(kind,date))


    def set_grade(self,grade):
        "set the grade to a given value"

        self.grade = grade


    def add_module_element(self,other_class,date):
        "add a new module element to the elements list"

        obj = other_class(self)
        obj.add_important_date(date)
        self.elements.append((obj))

    def get_title(self):
        pass
        ######## CODE MISSING HERE

    def get_grade(self):
        pass
        ######## CODE MISSING HERE

#########################################################################

class Course(Module):

    def __str__(self):
        pass
        ######## CODE MISSING HERE

#########################################################################

class Seminar(Module):

    def __init__(self,ects,title,semester,topic, grade=None):
        pass
        ######## CODE MISSING HERE
    
    def __str__(self):
        pass
        ######## CODE MISSING HERE

    def get_topic(self):
        pass
        ######## CODE MISSING HERE

#########################################################################

class Thesis(Module):

    def __init__(self,ects,title,semester,topic,research_group, grade=None):
        pass
        ######## CODE MISSING HERE
    
    def __str__(self):
        pass
        ######## CODE MISSING HERE

    def get_topic(self):
        pass
        ######## CODE MISSING HERE

    def get_research_group(self):
        pass
        ######## CODE MISSING HERE

#########################################################################

### test cases ###

info1 = Course(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
info1.get_important_dates_overview()
# expected output:
# Important dates for Info 1:
#	Midterm on 31.10.2017
#	Final Exam on 20.12.2017
print(info1)
# expected output:
# Course: Info 1

math1 = Course(6, "Mathematik I", 1)
math1.add_module_element(Midterm,"18.12.2017")
math1.get_important_dates_overview()
# Important dates for Mathematik I:
#	Midterm on 18.12.2017


# print(Module.module_count)
# expected output: 2

thesis = Thesis(18,"Bachelor Thesis",6,"A promising research topic on Software Engineering","SEAL")
# print(thesis)
# expected output:
# Bachelor Thesison the topic: A promising research topic on Software Engineering in the Research Group SEAL


sem = Seminar(3,"Seminar in Software Engineering",4,"A Seminar topic")
# print(sem)
# print(thesis)
# expected output:
# Seminar in Software Engineering under the topic: A Seminar topic

info1.set_grade(6)
