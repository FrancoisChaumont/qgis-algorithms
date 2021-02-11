import sys

# init path to qgis libraries
sys.path.append('/usr/lib/qgis')
sys.path.append('/usr/share/qgis/python/plugins')

# import qgis core libraries
from qgis.core import (
     QgsApplication, 
     # QgsProcessingFeedback
)

# init qgis application
QgsApplication.setPrefixPath('/usr', True)
app = QgsApplication([], False)
app.initQgis()

# import qgis native algorithm libraries
from qgis.analysis import QgsNativeAlgorithms

# add native algorithms to application
app.processingRegistry().addProvider(QgsNativeAlgorithms())

# import processing (needed to run algorithms)
import processing
from processing.core.Processing import Processing

# init processing
Processing.initialize()

def app_clean_exit():
     """Clean exit of the QGIS application by freeing resources..."""
     app.exitQgis()
