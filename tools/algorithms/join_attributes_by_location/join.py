import sys
from pathlib import Path

# common to all qgis modules
from algorithms.common.algorithm import Algorithm
import algorithms.common.exceptions as C_Exceptions

# module specific qgis libraries
from qgis.core import QgsVectorLayer

class Join(Algorithm):
    """Handle join attributes by location processing"""

    # default values
    _DEFAULT_CRS = Algorithm._DEFAULT_CRS_NUMBER
    _DEFAULT_JOIN_TYPE = 1
    _DEFAULT_DISCARD_NONMATCHING_FROM_MATCH_RESULTS = True
    _DEFAULT_KEEP_NON_MATCHING_ONLY = False
    _DEFAULT_GEO_PREDICATE_CRITERIA = 5
    _DEFAULT_INPUT_DELIMITER = ","

    # fixed values
    _OUTPUT_EXTENSION = "csv"

    # use csv headers or not
    _USE_HEADERS_YES = "yes"
    _USE_HEADERS_NO = "no"

    def __init__(self, argv):
        self._input_crs = self._DEFAULT_CRS
        self._input_headers = self._USE_HEADERS_YES
        self._input_delimiter = self._DEFAULT_INPUT_DELIMITER
        self._join_type = self._DEFAULT_JOIN_TYPE
        self._keep_non_matching_only = self._DEFAULT_KEEP_NON_MATCHING_ONLY
        self._geopredicate_criteria = self._DEFAULT_GEO_PREDICATE_CRITERIA

        self._join_layer_path = None
        self._join_layer_name = None
        self._join_layer_fields = None
        self._input_directory = None
        self._input_pattern = None
        self._input_x_field = None
        self._input_y_field = None
        self._output_directory = None

        self._init_options(argv)
    
    def _init_options(self, argv):
        """Verify and set up values from options/arguments"""

        opts = Join._load_options(argv)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise C_Exceptions.DisplayHelpError
            # MANDATORY ARGUMENTS
            elif opt == "--layer":
                self._join_layer_path = arg
            elif opt == "--layername":
                self._join_layer_name = arg
            elif opt == "--layerfields":
                self._join_layer_fields = arg.split()
            elif opt == "--indir":
                self._input_directory = arg
            elif opt == "--inpat":
                self._input_pattern = arg
            elif opt == "--inxfield":
                self._input_x_field = arg
            elif opt == "--inyfield":
                self._input_y_field = arg
            elif opt == "--outdir":
                self._output_directory = arg
            # OPTIONAL ARGUMENTS
            elif opt == "--indel":
                self._input_delimiter = arg
            elif opt == "--incrs":
                self._input_crs = arg
            elif opt == "--innoheaders":
                self._input_headers = self._USE_HEADERS_NO
            elif opt == "--jointype":
                self._join_type = arg
            elif opt == "--nonmatching":
                self._keep_non_matching_only = True
            elif opt == "--geopredicate":
                self._geopredicate_criteria = arg.split()

        if self._join_layer_path == None or \
            self._join_layer_name == None or \
            self._join_layer_fields == None or \
            self._input_directory == None or \
            self._input_pattern == None or \
            self._input_x_field == None or \
            self._input_y_field == None or \
            self._output_directory == None:
            raise C_Exceptions.MissingArgumentsError

    @staticmethod
    def _get_long_options():
        """Return a list of all long options"""

        return super(Join, Join)._get_long_options() + [
            "layer=",
            "layername=",
            "layerfields=",
            "indir=",
            "inpat=",
            "indel=",
            "inxfield=",
            "inyfield=",
            "incrs=",
            "innoheaders",
            "outdir=",
            "jointype=",
            "nonmatching",
            "geopredicate="
        ]
    
    @staticmethod
    def _get_short_options():
        """Return a list of all short options"""
        
        return super(Join, Join)._get_short_options()
    
    @staticmethod
    def _load_options(argv):
        """Load options from arguments"""

        return super(Join, Join)._load_options(argv, Join._get_short_options(), Join._get_long_options())

    def get_join_layer_name(self):
        """Return join layer name"""

        return self._join_layer_name

    def get_input_path_list(self):
        """Return input path list of files"""

        return Path(self._input_directory).glob(self._input_pattern)

    def create_input_layer(self, input_file, path_in_str, layer_name):
        """Create and return input layer"""

        input_file_uri = f"file://{path_in_str}?useHeader={self._input_headers}&delimiter={self._input_delimiter}&xField={self._input_x_field}&yField={self._input_y_field}&crs=epsg:{self._input_crs}"
        
        return super()._load_vector_layer(input_file_uri, layer_name, self._PROVIDER_LIBRARY_DELIMITED_TEXT)

    def create_join_layer(self):
        """Create and return join layer"""

        return super()._load_vector_layer(self._join_layer_path, self._join_layer_name, self._PROVIDER_LIBRARY_OGR)

    def _get_output_file_details(self, output_file_name):
        """Initialize and return output match type and file path"""

        if self._keep_non_matching_only:
            output_match_type = "NON_MATCHING"
            file_name_suffix = ".non-matching"
        else:
            output_match_type = "OUTPUT"
            file_name_suffix = ""
        
        output_file_path = f"{self._output_directory}/{output_file_name}.{self._join_layer_name}{file_name_suffix}.{self._OUTPUT_EXTENSION}"

        return output_match_type, output_file_path

    def join(self, processing, output_file_name, input_layer, join_layer):
        """Join attributes by location creating output file(s) discarting non-matching from the match results and return a join count"""

        output_match_type, output_file_path = self._get_output_file_details(output_file_name)

        try:
            r = processing.run("native:joinattributesbylocation", {
                'INPUT': input_layer,
                'JOIN': join_layer,
                'PREDICATE': self._geopredicate_criteria,
                'JOIN_FIELDS': self._join_layer_fields,
                'METHOD': self._join_type,
                'DISCARD_NONMATCHING': self._DEFAULT_DISCARD_NONMATCHING_FROM_MATCH_RESULTS,
                'PREFIX': f"{self._join_layer_name}_",
                output_match_type: output_file_path
            })
        except:
            raise C_Exceptions.UnexpectedError(sys.exc_info()[0])

        if 'JOINED_COUNT' in r:
            return r['JOINED_COUNT']
        else:
            return None
