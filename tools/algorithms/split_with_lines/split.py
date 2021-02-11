# common to all qgis modules
from algorithms.common.algorithm import Algorithm
import algorithms.common.exceptions as C_Exceptions

# module specific qgis libraries
from qgis.core import QgsProcessingException

class Split(Algorithm):
    """Handle splitting layer with grid lines"""

    def __init__(self, argv):
        self._input_layer_path = None
        self._split_layer_path = None
        self._output_file = None

        self._init_options(argv)
    
    def _init_options(self, argv):
        """Verify and set up values from options/arguments"""

        opts = Split._load_options(argv)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise C_Exceptions.DisplayHelpError
            # MANDATORY ARGUMENTS
            elif opt == "--inputlayer":
                self._input_layer_path = arg
            elif opt == "--splitlayer":
                self._split_layer_path = arg
            elif opt == "--outfile":
                self._output_file = arg

        if self._input_layer_path == None or \
            self._split_layer_path == None or \
            self._output_file == None:
            raise C_Exceptions.MissingArgumentsError

    @staticmethod
    def _get_long_options():
        """Return an array of all long options"""

        return super(Split, Split)._get_long_options() + [
            "inputlayer=",
            "splitlayer=",
            "outfile="
        ]
    
    @staticmethod
    def _get_short_options():
        """Return a list of all short options"""
        
        return super(Split, Split)._get_short_options()

    @staticmethod
    def _load_options(argv):
        """Load options from arguments"""

        return super(Split, Split)._load_options(argv, Split._get_short_options(), Split._get_long_options())

    def get_input_layer_path(self):
        """Return input layer path"""

        return self._input_layer_path
    
    def get_split_layer_path(self):
        """Return split layer path"""

        return self._split_layer_path

    def get_output_file_path(self):
        """Return output file path"""

        return self._output_file

    def create_vector_layer(self, layer_path, layer_name):
        """Create and return a layer loaded in memory"""

        return super()._load_vector_layer(layer_path, layer_name, self._PROVIDER_LIBRARY_OGR)

    def split_with_lines(self, processing, input_layer, split_layer, output_file):
        """Split the input layer along the lines of the split layer"""

        try:
            processing.run("native:splitwithlines", {
                'INPUT': self._input_layer_path,
                'LINES': self._split_layer_path,
                'OUTPUT': self._output_file
            })
        except QgsProcessingException as ex:
            raise C_Exceptions.ProcessingError(ex)
        except Exception as ex:
            raise C_Exceptions.UnexpectedError(ex)
