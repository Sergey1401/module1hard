# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Исходные данные:
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
# Формулы для подсчета средних оценок:
g1 = sum(grades[0])/len(grades[0])
g2 = sum(grades[1])/len(grades[1])
g3 = sum(grades[2])/len(grades[2])
g4 = sum(grades[3])/len(grades[3])
g5 = sum(grades[4])/len(grades[4])
# Новый список со средними оценками:
average_grade = [g1,g2,g3,g4,g5]
# Имена из множества в список в алфавитном порядке:
student_list_alph = list(sorted(students))
# Два списка в словарь:
average_grade = dict(zip(student_list_alph,average_grade))
print(average_grade)