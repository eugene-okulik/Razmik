import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


class DataProcessor:
    def __init__(self, file):
        self.file_path = file
        self.python_date = None

    def data_file(self):
        with open(self.file_path, encoding='utf-8') as homework:
            data_string = homework.readlines()
            for line in data_string:
                line = line.strip()
                date_start_index = line.find(' ') + 1
                date_end_index = line.find(' - ')
                date_substr = line[date_start_index:date_end_index]
                self.python_date = datetime.datetime.strptime(date_substr, "%Y-%m-%d %H:%M:%S.%f")
                return self.python_date

    def method_increase_one_week(self):
        if self.python_date is not None:
            return self.python_date + datetime.timedelta(days=7)
        else:
            return None

    def method_print_day(self):
        return self.python_date.strftime("%A")

    def print_difference_current_day(self):
        now = datetime.datetime.now()
        difference = now - self.python_date
        return difference.days


one = DataProcessor(file_path)
one.data_file()
print(one.method_increase_one_week())
second = DataProcessor(file_path)
second.data_file()
print(second.method_print_day())
third = DataProcessor(file_path)
third.data_file()
print(third.print_difference_current_day())
