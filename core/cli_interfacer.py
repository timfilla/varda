from core.mode_selector import ModeSelector
from data_readers import JsonReader
from location_finder import *
from time_finder import *
from config import *
import sys


class CliInterface:
    def __init__(self):
        self.data = ''
        self.mode = ''
        self.locator = ''
        self.location = ''
        self.time_finder = ''
        self.obs_time = ''

        # 1. Get data from source specified in config.py.
        if SOURCE_TYPE == 'json':
            self.data = JsonReader(path=SOURCE_LOCATION)
        else:
            sys.exit('Source type not supported.')

        df = self.data.produce_df()

        # 2. Obtain user inputs
        self.mode = ModeSelector(df)
        self.mode.choose_mode()

        # 3. Obtain user location
        self.locator = LocationFinder()
        self.location = self.locator.cli_locator()

        # 4. Obtain user time
        self.time_finder = TimeFinder()
        self.obs_time = self.time_finder.cli_finder()

        # 5. Run selected mode.
        if self.mode.get_mode() == 'objectfinder':
            pass
        elif self.mode.get_mode() == 'rightnow':
            pass