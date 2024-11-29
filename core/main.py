from config import RUN_TYPE
from cli_interfacer import CliInterface

if __name__ == '__main__':
    if RUN_TYPE == 'cli':
        run = CliInterface()

