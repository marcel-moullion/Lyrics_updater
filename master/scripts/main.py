# -- coding: utf-8 --
import sys
import parseConfigFiles as config
import parseTextFiles as text
import generateOutput as output
import generateOutput7 as output7
import os
import Tkinter
import Tkconstants
import tkFileDialog
import unicodedata

configAll = {}
try:
    config.ParseConfigFiles(configAll)
    # loop over all files in master
    __file = __file__.decode(sys.getfilesystemencoding())
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file)))
    folder = u"textFiles"
    root = os.path.join(dirname, folder)
    master = Tkinter.Tk()
    filenames = tkFileDialog.askopenfilename(
        multiple=True, initialdir=root, title="Select Files to generate", filetypes=(("txt files", "*.txt"),))
    filenames = master.tk.splitlist(filenames)
    for file in filenames:
        try:
            if not isinstance(file, unicode):
                file = unicode(file, "utf-8")
            file = os.path.basename(file)
            if file.endswith(".txt"):
                print(u'Generating "{0}"'.format(
                    unicodedata.normalize("NFC", file).encode('ascii', 'ignore')))
                inputText = text.ParseTextFile(
                    root, file, configAll["groupConfigs"])
                # loop over configs and create output
                for config in configAll["fileConfigs"]:
                    output.CreateOutputs(
                        config, configAll["groupConfigs"], inputText)
                # loop over configs from pro7 and create output
                for config in configAll["fileConfigs7"]:
                    output7.CreateOutputs(
                        config, configAll["groupConfigs7"], inputText)
        except ValueError as err:
            print(err)
    print("Generation Succesful. This window can be closed")
except ValueError as err:
    print("Exception occured: check following text:")
    print(err)
