import os
import getopt

# qgis import and initialization
from algorithms.common.initialization import *

# common to all qgis modules
import algorithms.common.exceptions as C_Exceptions
from algorithms.common.help import Help as C_Help

# module specific libraries
from algorithms.help_tools.tools import AlgorithmTools as Tools

def main(processing, argv):
    script_name = os.path.basename(__file__)

    provider = None
    algorithm = None

    # options/arguments
    try:
        opts, args = getopt.getopt(
            argv, 
            "hp:a:", 
            [ "help", "provider=", "algorithm=" ]
        )

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise C_Exceptions.DisplayHelpError
            elif opt in ("-p", "--provider"):
                provider = arg
            elif opt in ("-a", "--algorithm"):
                algorithm = arg
        
        if provider is None or algorithm is None:
            raise C_Exceptions.MissingArgumentsError

    except getopt.GetoptError:
        C_Exceptions.OptionsError()
        C_Help.display(script_name)
        return
    except (C_Exceptions.DisplayHelpError, C_Exceptions.MissingArgumentsError):
        C_Help.display(script_name)
        return

    # display algorithm usage help
    Tools.display_usage(processing, provider, algorithm)

if __name__ == "__main__":
    main(processing, sys.argv[1:])
    app_clean_exit()
