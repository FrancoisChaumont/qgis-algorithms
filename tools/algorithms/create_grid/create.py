# common to all qgis modules
from algorithms.common.algorithm import Algorithm
import algorithms.common.exceptions as C_Exceptions

# module specific qgis libraries
from qgis.core import QgsProcessingException

class Create(Algorithm):
    """Handle grid creation"""

    # default values
    _DEFAULT_CRS = f'EPSG:{Algorithm._DEFAULT_CRS_NUMBER}'
    _DEFAULT_TYPE = 1
    _DEFAULT_HSPACING = 1
    _DEFAULT_VSPACING = 1

    def __init__(self, argv):
        self._grid_extent_path = None
        self._output_file = None

        self._grid_crs = self._DEFAULT_CRS
        self._grid_type = self._DEFAULT_TYPE
        self._horizontal_spacing = self._DEFAULT_HSPACING
        self._vertical_spacing = self._DEFAULT_VSPACING
        
        self._init_options(argv)
    
    def _init_options(self, argv):
        """Verify and set up values from options/arguments"""

        opts = Create._load_options(argv)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise C_Exceptions.DisplayHelpError
            # MANDATORY ARGUMENTS
            elif opt == "--gridextentpath":
                self._grid_extent_path = arg
            elif opt == "--outfile":
                self._output_file = arg
            # OPTIONAL ARGUMENTS
            elif opt == "--gridcrs":
                self._grid_crs = arg
            elif opt == "--gridtype":
                self._grid_type = arg
            elif opt == "--horizontalspacing":
                self._horizontal_spacing = arg
            elif opt == "--verticalspacing":
                self._vertical_spacing = arg

        if self._grid_extent_path == None or self._output_file == None:
            raise C_Exceptions.MissingArgumentsError

    @staticmethod
    def _get_long_options():
        """Return an array of all long options"""

        return super(Create, Create)._get_long_options() + [
            "gridtype=",
            "gridextentpath=",
            "horizontalspacing=",
            "verticalspacing=",
            "gridcrs=",
            "outfile="
        ]
    
    @staticmethod
    def _get_short_options():
        """Return a list of all short options"""
        
        return super(Create, Create)._get_short_options()

    @staticmethod
    def _load_options(argv):
        """Load options from arguments"""

        return super(Create, Create)._load_options(argv, Create._get_short_options(), Create._get_long_options())

    def get_grid_extent_path(self):
        """Return grid extent path"""

        return self._grid_extent_path

    def create_vector_layer(self, layer_path, layer_name):
        """Create and return a layer loaded in memory"""

        return super()._load_vector_layer(layer_path, layer_name, self._PROVIDER_LIBRARY_OGR)

    def create_grid(self, processing, grid_extent):
        """Create a grid and save it to an output file"""

        try:
            processing.run("native:creategrid", {
                'TYPE': self._grid_type,
                'EXTENT': grid_extent,
                'HSPACING': self._horizontal_spacing,
                'VSPACING': self._vertical_spacing,
                'HOVERLAY': 0,
                'VOVERLAY': 0,
                'CRS': self._grid_crs,
                'OUTPUT': self._output_file
            })
        except QgsProcessingException as ex:
            raise C_Exceptions.ProcessingError(ex)
        except Exception as ex:
            raise C_Exceptions.UnexpectedError(ex)
