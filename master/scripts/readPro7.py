# -- coding: utf-8 --

import sys
import os
import Tkinter
import Tkconstants
import tkFileDialog
import unicodedata
import presentation_pb2
import basicTypes_pb2


__file = __file__.decode(sys.getfilesystemencoding())
dirname = os.path.dirname(os.path.abspath(__file))
master = Tkinter.Tk()
filenames = tkFileDialog.askopenfilename(
    multiple=True, initialdir=dirname, title="Select Files to Read", filetypes=(("Pro7 files", "*.pro"),))
filenames = master.tk.splitlist(filenames)
for file in filenames:
    try:
        if not isinstance(file, unicode):
            file = unicode(file, "utf-8")
        presentation = presentation_pb2.Presentation()
        f = open(file, "rb")
        presentation.ParseFromString(f.read())
        f.close()
        f = open(file + ".txt", "w")
        f.write(str(presentation))
        f.close()
    except ValueError as err:
        print(err)
