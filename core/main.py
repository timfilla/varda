from core.cli_interfacer import CliInterface
from data_readers import JsonReader
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
    interface.choose_function()
