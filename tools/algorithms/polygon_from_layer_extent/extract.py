# common to all qgis modules
from algorithms.common.algorithm import Algorithm
import algorithms.common.exceptions as C_Exceptions

# module specific qgis libraries
from qgis.core import QgsProcessingException

class Extract(Algorithm):
    """Handle creating a polygon from an input layer extent"""

    _DEFAULT_START = 1

    def __init__(self, argv):
        self._input_layer_path = None
        self._output_file = None

        self._init_options(argv)
    
    def _init_options(self, argv):
        """Verify and set up values from options/arguments"""

        opts = Extract._load_options(argv)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise C_Exceptions.DisplayHelpError
            # MANDATORY ARGUMENTS
            elif opt == "--inputlayer":
                self._input_layer_path = arg
            elif opt == "--outfile":
                self._output_file = arg

        if self._input_layer_path == None or \
            self._output_file == None:
            raise C_Exceptions.MissingArgumentsError

    @staticmethod
    def _get_long_options():
        """Return an array of all long options"""

        return super(Extract, Extract)._get_long_options() + [
            "inputlayer=",
            "outfile="
        ]
    
    @staticmethod
    def _get_short_options():
        """Return a list of all short options"""
        
        return super(Extract, Extract)._get_short_options()

    @staticmethod
    def _load_options(argv):
        """Load options from arguments"""

        return super(Extract, Extract)._load_options(argv, Extract._get_short_options(), Extract._get_long_options())

    def get_input_layer_path(self):
        """Return input layer path"""

        return self._input_layer_path

    def get_output_file_path(self):
        """Return output file path"""

        return self._output_file

    def create_vector_layer(self, layer_path, layer_name):
        """Create and return a layer loaded in memory"""

        return super()._load_vector_layer(layer_path, layer_name, self._PROVIDER_LIBRARY_OGR)

    def extract_polygon_from_layer_extent(self, processing, input_layer, output_file):
        """Create a polygon from the input layer extent"""

        try:
            processing.run("native:polygonfromlayerextent", {
                'INPUT': self._input_layer_path,
                'ROUND_TO': 0,
                'OUTPUT': self._output_file
            })
        except QgsProcessingException as ex:
            raise C_Exceptions.ProcessingError(ex)
        except Exception as ex:
            raise C_Exceptions.UnexpectedError(ex)
