from institura_pkg.reader import read_students
from institura_pkg.cleaner import load_students
from institura_pkg.analyzer import analyse_batch, filter_by_batch, get_batch_names


students = load_students("sample_students.csv")
print(analyse_batch(students))

print(get_batch_names(students))