# common to all qgis modules
from algorithms.common.algorithm import Algorithm
import algorithms.common.exceptions as C_Exceptions

# module specific qgis libraries
from qgis.core import QgsProcessingException

class Add(Algorithm):
    """Handle adding an autoincremental field to a vector layer"""

    _DEFAULT_START = 1

    def __init__(self, argv):
        self._start = self._DEFAULT_START

        self._input_layer_path = None
        self._field_name = None
        self._output_file = None

        self._init_options(argv)
    
    def _init_options(self, argv):
        """Verify and set up values from options/arguments"""

        opts = Add._load_options(argv)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise C_Exceptions.DisplayHelpError
            # MANDATORY ARGUMENTS
            elif opt == "--inputlayer":
                self._input_layer_path = arg
            elif opt == "--fieldname":
                self._field_name = arg
            elif opt == "--outfile":
                self._output_file = arg
            # OPTIONAL ARGUMENTS
            elif opt == "--start":
                self._start = arg

        if self._input_layer_path == None or \
            self._field_name == None or \
            self._output_file == None:
            raise C_Exceptions.MissingArgumentsError

    @staticmethod
    def _get_long_options():
        """Return an array of all long options"""

        return super(Add, Add)._get_long_options() + [
            "inputlayer=",
            "fieldname=",
            "start=",
            "outfile="
        ]
    
    @staticmethod
    def _get_short_options():
        """Return a list of all short options"""
        
        return super(Add, Add)._get_short_options()

    @staticmethod
    def _load_options(argv):
        """Load options from arguments"""

        return super(Add, Add)._load_options(argv, Add._get_short_options(), Add._get_long_options())

    def get_input_layer_path(self):
        """Return input layer path"""

        return self._input_layer_path
    
    def get_field_name(self):
        """Return field name"""

        return self._field_name

    def get_start(self):
        """Return start"""

        return self._start

    def get_output_file_path(self):
        """Return output file path"""

        return self._output_file

    def create_vector_layer(self, layer_path, layer_name):
        """Create and return a layer loaded in memory"""

        return super()._load_vector_layer(layer_path, layer_name, self._PROVIDER_LIBRARY_OGR)

    def add_autoincremental_field(self, processing, input_layer, field_name, start, output_file):
        """Add autoincremenetal field to vector layer features"""

        try:
            processing.run("native:addautoincrementalfield", {
                'INPUT': self._input_layer_path,
                'FIELD_NAME': self._field_name,
                'START': self._start,
                'OUTPUT': self._output_file
            })
        except QgsProcessingException as ex:
            raise C_Exceptions.ProcessingError(ex)
        except Exception as ex:
            raise C_Exceptions.UnexpectedError(ex)
