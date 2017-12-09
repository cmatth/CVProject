import guidata
_app = guidata.qapplication() # not required if a QApplication has already been created

import guidata.dataset.datatypes as dt
import guidata.dataset.dataitems as di

class VideoOptionGUI(dt.DataSet):
    type = di.ChoiceItem("Choose video type:",
                         ("Pre-Recorded Video", "Webcam Video (live)"))
