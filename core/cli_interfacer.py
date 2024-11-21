import pandas as pd

class CliInterface:
    def __init__(self, available_data: pd.DataFrame):
        self.available_data = available_data

    def choose_function(self):
        while True:
            choice = input("Choose a function: (1) Object Finder, (2) What's Up There -> ")
            if choice == "1":
                finder = ObjectFinder(self.available_data)
                break
            elif choice == "2":
                finder = RightNow(self.available_data)
                break
            else:
                print('Invalid choice. Please select from the numbers listed.')
        finder.proceed()

class ObjectFinder(CliInterface):
    def __init__(self, available_data: pd.DataFrame):
        super().__init__(available_data)
        self.object_list = self.available_data['name'].to_list()

    def _obtain_target(self):
        objs_str = ', '.join(p for p in self.object_list)
        while True:
            print(f'Enter target object.')
            selection = input(f'Choices are: {objs_str} -> ')
            if selection in self.object_list:
                print('Valid target.')
                return selection
            else:
                print('Invalid target. Please select from the options listed.')


    def proceed(self):
        target = self._obtain_target()

# TODO: Implement RightNow functionality
class RightNow(CliInterface):
    def __init__(self, available_data: pd.DataFrame):
        super().__init__(available_data)

    @staticmethod
    def proceed():
        print('This feature is not yet implemented.')
