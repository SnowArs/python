class People():
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname

	def get_full_name(self):
		return self.name + ' ' + self.surname

class Student(People):
	def __init__(self, name, surname, birth_date, class_room, father_name, mother_name):
		People.__init__(self, name, surname)
		self.birth_date = birth_date
		self.class_room = class_room
		self.father_name = father_name
		self.mother_name = mother_name

	def class_room(self):
		self.class_room = str(int(self.class_room.split()[0])) + ' ' + self.class_room.split()[1]

class Teacher(People):
	def __init__(self, name, surname, lesson, teach_classes):
		People.__init__(self, name, surname)
		self.lesson = lesson
		self.teach_classes = teach_classes

	def teach_classes(self):
		return [str(int(self.teach_classes.split()[0])) + ' ' + self.teach_classes.split()[1] for col in teach_classes]

def print_classes():
	return print("классы в школе", set([cl.class_room for cl in students]))

def full_data():
	for cl in students: print(cl.get_full_name())
	full_name = input("введите имя и фамилию ученика как указанно выше ")
	for cl in students:
		if cl.get_full_name() == full_name:
			f_data = (cl.father_name, cl.mother_name, cl.class_room)
	return f_data


students = [Student("Александр", "Иванов", '10.11.1998', "5 А", "Игорь", "Ирина"),
			Student("Петр", "Сидоров", '10.10.1995', "8 Б", "Иван", "Татьяна"),
			Student("Василий", "Пупкин", '10.01.1996', "7 А", "Николай", "Светлана"),
			Student("Саша", "Синий", '23.01.1995', "8 Б", "Жора", "Татьяна"),
			Student("Миша", "Круг", '30.11.1998', "5 А", "Игорь", "Ирина"),
			Student("Костя", "Эрнст", '01.08.1995', "8 Б", "Дон", "Светлана"),
			Student("Глеб", "Жиглов", '09.03.1996', "7 А", "Сэмэн", "Мира"),
			Student("Саша", "Хряк", '23.01.1995', "8 Б", "Додон", "Ольга")
			]

teachers = (Teacher("Михайло ", "Ломоносов", "Математика", ("5 А", "8 Б")),
			Teacher("Александр ", "Скляр", "Музыка", ("5 А", "7 А")),
			Teacher("Изя ", "Рабинович", "Финансы", ("7 А", "8 Б"))
			)




answer = "y"

while answer != "n":
	print("Получить полный список всех классов школы [1]")
	print("Получить список всех учеников в указанном классе [2]")
	print("Получить список всех предметов указанного ученика [3]")
	print("Узнать ФИО родителей указанного ученика [4]")
	print("Получить список всех Учителей, преподающих в указанном классе [5]")

	do = int(input("введите номер действия "))

	if do == 1:
		print_classes()
	elif do == 2:
		number_class = input("введите номер класса : '8 Б', '7 А', '5 А' - ")
		print([cl.get_full_name() for cl in students if cl.class_room == number_class])

	elif do == 3:
		less = full_data()
		lessons_inclass = [ls.lesson for ls in teachers if less[2] in ls.teach_classes]
		print(lessons_inclass)
	elif do == 4:
		less = full_data()
		print("имя отца - %s, имя матери - %s" % (less[0:2]))
	elif do == 5:
		number_class = input("введите номер класса : '8 Б', '7 А', '5 А' - ")
		print([tch.get_full_name() for tch in teachers if number_class in tch.teach_classes])
	else:
		pass
	answer = input("\nхотите повторить (у/n) -")

