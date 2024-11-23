from datetime import datetime, UTC
import pytz

class TimeFinder:
    def __init__(self):
        self.time = ''

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def cli_finder(self):
        while True:
            choice = input('Choose a time: (1) use system time, (2) enter a date and time. -> ')
            if choice == '1':
                finder = SystemTime()
                break
            elif choice == '2':
                finder = ManualTime()
                break
            else:
                print('Invalid choice. Enter a number from the listed options.')
        self.set_time(finder.get_time())
        print(f'Time (in UTC) is set to {self.time}.')

class SystemTime:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
         return datetime.now(UTC)

class ManualTime:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        print('All dates and time should be entered in UTC.')
        while True:
            selected_date_str = input('Enter date in format "YYYY-MM-DD". -> ')
            try:
                selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d')
                break
            except ValueError:
                print('Invalid date. Enter a date in the specified format.')

        while True:
            selected_time_str = input('Enter time in format "HH:MM". Use 24 hour time. -> ')
            try:
                selected_time = datetime.strptime(selected_time_str, '%H:%M')
                break
            except ValueError:
                print('Invalid time. Enter a number in the specified format.')

        dt = datetime.combine(selected_date, selected_time.time())
        return pytz.utc.localize(dt)
