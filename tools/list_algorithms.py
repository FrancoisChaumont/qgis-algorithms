import os
import getopt

# qgis import and initialization
from algorithms.common.initialization import *

# common to all qgis modules
import algorithms.common.exceptions as C_Exceptions
from algorithms.common.help import Help as C_Help

# module specific libraries
from algorithms.help_tools.tools import AlgorithmTools as AlgorithmTools

def main(app, argv):
    script_name = os.path.basename(__file__)

    # options/arguments
    try:
        opts, args = getopt.getopt(
            argv, 
            "h", 
            [ "help" ]
        )

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise C_Exceptions.DisplayHelpError

    except getopt.GetoptError:
        C_Exceptions.OptionsError()
        C_Help.display(script_name)
        return
    except (C_Exceptions.DisplayHelpError):
        C_Help.display(script_name)
        return

    # list algorithms
    AlgorithmTools.list_all(app)

if __name__ == "__main__":
    main(app, sys.argv[1:])
    app_clean_exit()
