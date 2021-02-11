class AlgorithmTools(object):
    """Help on available algorithms, usage, ..."""

    @staticmethod
    def list_all(app):
        """List all algorithms"""

        for alg in app.processingRegistry().algorithms():
            print(alg.id(), "->", alg.displayName())

    @staticmethod
    def display_usage(processing, provider, algorithm):
        """Display algorithm usage help"""
        
        processing.algorithmHelp(f"{provider}:{algorithm}")

