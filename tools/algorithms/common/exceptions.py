class Error(Exception):
    """Base class for exceptions in this module"""
    pass

class DisplayHelpError(Error):
    """Exception raised when user requests to display help"""
    def __init__(self):
        print("Display help requested by user:")

class MissingArgumentsError(Error):
    """Exception raised when missing some mandatory arguments"""
    def __init__(self):
        print("Missing mandatory argument(s)! Use -h/--help for usage")

class UnknownError(Error):
    """Exception raised when an unknown error occurred"""
    def __init__(self, error_message):
        print(f"Unknown error occurred: {error_message}")

class UnexpectedError(Error):
    """Exception raised when an unexpected error occurred"""
    def __init__(self, error_message):
        print(f"Unexpected error occurred: {error_message}")

class OptionsError(Error):
    """Exception raised when failed to initialize options"""
    def __init__(self, error_message):
        print(f"Failed to initialize options: {error_message}")

class LoadVectorLayerError(Error):
    """Exception raised when failed to create and buffer a layer"""
    def __init__(self, layer_name='UNDEFINED'):
        print(f"Failed to load layer {layer_name}!")

class LoadVectorLayerNotValidError(Error):
    """Exception raised when failed to load a vector layer"""
    def __init__(self, layer_name='UNDEFINED'):
        print(f"Failed to load vector layer {layer_name}!")

class ProcessingError(Error):
    """Exception raised when a processing error occurred"""
    def __init__(self, error_message):
        print(f"Processing error occurred: {error_message}")
