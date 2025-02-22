import pandas as pd

class ModeSelector:
    def __init__(self, available_data: pd.DataFrame):
        self.available_data = available_data
        self.mode = ''
        self.target = ''

    def get_mode(self):
        return self.mode

    def get_target(self):
        return self.target

    def set_mode(self, mode):
        self.mode = mode

    def set_target(self, target):
        self.target = target

    def choose_mode(self):
        while True:
            choice = input("Choose a function: (1) Object Finder, (2) What's Up There -> ")
            if choice == "1":
                finder = ObjectFinderMode(self.available_data)
                break
            elif choice == "2":
                finder = RightNowMode(self.available_data)
                break
            else:
                print('Invalid choice. Please select from the numbers listed.')
        finder.proceed()
        self.set_mode(finder.mode)
        self.set_target(finder.target)

class ObjectFinderMode(ModeSelector):
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
        self.set_mode('objectfinder')
        self.set_target(self._obtain_target())

class RightNowMode(ModeSelector):
    def __init__(self, available_data: pd.DataFrame):
        super().__init__(available_data)

    def proceed(self):
        self.set_mode('rightnow')
        print('This feature is not yet implemented.')
