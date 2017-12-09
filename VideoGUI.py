import VideoOptionGUI as vog
import Tkinter
import tkFileDialog

def video_type():
    # Give user option to choose live or pre-recorded video.
    param = vog.VideoOptionGUI()
    param.edit()
    if param.type == 1:
        return param.type
    else:
        return video_selector()

def video_selector():
    # Have user select the video file.
    root = Tkinter.Tk()
    root.withdraw()
    video_file_path = tkFileDialog.askopenfilename()
    return video_file_path