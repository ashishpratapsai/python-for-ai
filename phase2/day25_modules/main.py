from institura_pkg.reader import read_students
from institura_pkg.cleaner import load_students
from institura_pkg.analyzer import analyse_batch, filter_by_batch

students = load_students("sample_students.csv")
print(analyse_batch(students))