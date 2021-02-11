import os
import sys
import getopt

# qgis import and initialization
from algorithms.common.initialization import *

# common to all qgis modules
import algorithms.common.exceptions as C_Exceptions
from algorithms.common.help import Help as C_Help

# module specific libraries
from algorithms.create_grid.create import Create

def main(argv):
    script_name = os.path.basename(__file__)
    
    try:
        # options/arguments + initialization
        print("Initialization...")
        cgrid = Create(argv)

        # load grid extent layer
        print("Loading grid extent layer...")
        grid_extent = cgrid.create_vector_layer(cgrid.get_grid_extent_path(), script_name)

        # create grid from extent layer
        print("Creating grid from extent layer...")
        cgrid.create_grid(processing, grid_extent)
    except ( \
        C_Exceptions.DisplayHelpError, \
        C_Exceptions.MissingArgumentsError, \
        C_Exceptions.OptionsError):
        C_Help.display(script_name)
    except ( \
        C_Exceptions.LoadVectorLayerError, \
        C_Exceptions.LoadVectorLayerNotValidError, \
        C_Exceptions.ProcessingError, \
        C_Exceptions.UnexpectedError):
        pass
    except Exception as ex:
        C_Exceptions.UnexpectedError(ex)

if __name__ == "__main__":
    main(sys.argv[1:])
    app_clean_exit()
