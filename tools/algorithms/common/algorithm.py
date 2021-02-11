import sys
import getopt

# common to all qgis modules
import algorithms.common.exceptions as C_Exceptions

# module specific qgis libraries
from qgis.core import QgsVectorLayer

class Algorithm(object):
    """Hold common functionalities between algorithms"""

    _DEFAULT_CRS_NUMBER = 4326
    _PROVIDER_LIBRARY_OGR = 'ogr'
    _PROVIDER_LIBRARY_DELIMITED_TEXT = 'delimitedtext'

# OPTIONS
    @staticmethod
    def _get_long_options():
        """Return an array of all long options"""

        return [ "help" ]
        
    @staticmethod
    def _get_short_options():
        """Return a list of all short options"""
        
        return "h"

    @staticmethod
    def _load_options(argv, short_options, long_options):
        """Load options from arguments"""

        try:
            opts, args = getopt.getopt(argv, short_options, long_options)
        except (getopt.GetoptError, C_Exceptions.MissingArgumentsError, C_Exceptions.DisplayHelpError) as ex:
            raise C_Exceptions.OptionsError(ex)
        except Exception as ex:
            raise C_Exceptions.UnexpectedError(ex)

        return opts

# LAYER
    def _load_vector_layer(self, layer_path, layer_name, provider_library):
        """Create and return a layer loaded in memory"""

        try:
            layer = QgsVectorLayer(layer_path, layer_name, provider_library)
        except Exception as ex:
            raise C_Exceptions.LoadVectorLayerError(ex)

        if not layer.isValid():
            raise C_Exceptions.LoadVectorLayerNotValidError(layer_name)

        return layer
