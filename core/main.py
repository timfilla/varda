from core.cli_interfacer import CliInterface
from data_readers import JsonReader
from location_finder import *
from config import *
import sys

if __name__ == '__main__':

    # 1. Get data from source specified in config.py.
    if SOURCE_TYPE == 'json':
        data = JsonReader(path=SOURCE_LOCATION)
    else:
        sys.exit('Source type not supported.')

    df = data.produce_df()

    # 2. Obtain user inputs
    interface = CliInterface(df)
    interface.choose_mode()

    # 3. Obtain user location
    location = LocationFinder()

    print('Lat: ' + str(location.get_lat()))
    print('Lon: ' + str(location.get_lon()))
    print('Mode: ' + interface.get_mode())
    print('Target: ' + interface.get_target())

    # 4. Run selected mode.
    if interface.get_mode() == 'objectfinder':
        pass
    elif interface.get_mode() == 'rightnow':
        pass
