import os
import sys
import getopt

# qgis import and initialization
from algorithms.common.initialization import *

# common to all qgis modules
import algorithms.common.exceptions as C_Exceptions
from algorithms.common.help import Help as C_Help

# module specific libraries
from algorithms.join_attributes_by_location.join import Join

def main(argv):
    script_name = os.path.basename(__file__)
    
    # options/arguments + initialization
    print("Initialization...")
    try:
        jabl = Join(argv)
    except (C_Exceptions.DisplayHelpError, C_Exceptions.MissingArgumentsError, C_Exceptions.OptionsError):
        C_Help.display(script_name)
        return
    
    # create join layer
    print("Creating join layer {}...".format(jabl.get_join_layer_name()))
    try:
        join_layer = jabl.create_join_layer()
    except (C_Exceptions.LoadVectorLayerError, C_Exceptions.LoadVectorLayerNotValidError, C_Exceptions.UnexpectedError):
        return
    except Exception as ex:
        C_Exceptions.UnknownError(ex)
        return

    # parse all input files
    print("Parsing input files...")
    path_list = jabl.get_input_path_list()
    for path in path_list:
        path_in_str = str(path)

        # create input file layer
        input_file = os.path.basename(path_in_str)
        print("Creating input layer for {}...".format(input_file))
        try:
            input_layer = jabl.create_input_layer(input_file, path_in_str, input_file)
        except (C_Exceptions.LoadVectorLayerError, C_Exceptions.LoadVectorLayerNotValidError, C_Exceptions.UnexpectedError):
            continue
        except Exception as ex:
            C_Exceptions.UnknownError(ex)
            continue
        
        # join join-layer and input-layer
        output_file_name = os.path.splitext(input_file)[0]
        print("Joining with layer {}...".format(jabl.get_join_layer_name()))
        
        try:
            joined = jabl.join(
                processing,
                output_file_name,
                input_layer,
                join_layer    
            )
        except Exception as ex:
            C_Exceptions.UnknownError(ex)

        if joined is not None:
            print(f"{joined} joined")
        else:
            print("Failed to join!")

if __name__ == "__main__":
    main(sys.argv[1:])
    app_clean_exit()
