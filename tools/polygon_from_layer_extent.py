import os
import sys

# qgis import and initialization
from algorithms.common.initialization import *

# common to all qgis modules
import algorithms.common.exceptions as C_Exceptions
from algorithms.common.help import Help as C_Help

# module specific libraries
from algorithms.polygon_from_layer_extent.extract import Extract

def main(argv):
    script_name = os.path.basename(__file__)
    
    try:
        # options/arguments + initialization
        print("Initialization...")
        pfle = Extract(argv)

        # load input layer
        print("Loading input layer...")
        input_layer = pfle.create_vector_layer(pfle.get_input_layer_path(), script_name)

        # split input layer
        print("Adding autoincremental field...")
        pfle.extract_polygon_from_layer_extent(processing, input_layer, pfle.get_output_file_path())
        
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
