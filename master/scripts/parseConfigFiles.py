import xml.etree.ElementTree as ET
import glob
import os
import re
import base64
import sys
import presentation_pb2
import basicTypes_pb2


def ParseConfigFiles(configAll):
    ParseMasterConfigPro6(configAll)
    ParseMasterConfigPro7(configAll)
    ParseConfigFilesPro6(configAll)
    ParseConfigFilesPro7(configAll)
    if (len(configAll["fileConfigs"]) == 0) and (len(configAll["fileConfigs7"]) == 0):
        raise ValueError(
            'Error: No configuration file was found in sub folders')


def ParseMasterConfigPro6(configAll):
    print('Parsing "masterConfig_Groups.pro6"')
    configAll["groupConfigs"] = {}
    __file = __file__.decode(sys.getfilesystemencoding())
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file)))
    folder = u"masterConfig_Groups.pro6"
    root = os.path.join(dirname, folder)
    try:
        tree = ET.parse(root)
    except:
        raise ValueError(
            'Error: "masterConfig_Groups.pro6" was not found in master directory')
    groups = tree.find("array[@rvXMLIvarName='groups']")

    for group in groups:
        groupOut = {}
        groupOut["color"] = group.get("color")
        groupOut["hotKey"] = group[0][0].get("hotKey")
        configAll["groupConfigs"][group.get("name")] = groupOut


def ParseMasterConfigPro7(configAll):
    print('Parsing "masterConfig_Groups.pro"')
    __file = __file__.decode(sys.getfilesystemencoding())
    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file)))
    folder = u"masterConfig_Groups.pro"
    root = os.path.join(dirname, folder)
    presentation = presentation_pb2.Presentation()
    f = open(root, "rb")
    presentation.ParseFromString(f.read())
    f.close()
    #store all groups in masterconfig
    configAll["groupConfigs7"] = {}
    for groups in presentation.cue_groups:
        groups.ClearField("cue_identifiers")
        configAll["groupConfigs7"][groups.group.name] = groups


def ParseConfigFilesPro6(configAll):
    # loop over all config files in the subfolders
    configAll["fileConfigs"] = []
    __file = __file__.decode(sys.getfilesystemencoding())
    dirname = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file))))
    folder = u"config_*.pro6"
    root = os.path.join(dirname, u"**")
    root = os.path.join(root, folder)
    print(root)
    for file in glob.glob(root):
        print('Parsing "{0}"'.format(file))
        configDict = {}
        # save path
        configDict["path"] = os.path.dirname(os.path.abspath(file))
        # save style name
        configDict["styleName"] = re.search('config_(.*).pro6', file).group(1)
        # read config file
        tree = ET.parse(file)
        # get needed elements
        rvPresentationDocument = tree.getroot()
        groups = rvPresentationDocument.find("array[@rvXMLIvarName='groups']")
        group = groups.find("RVSlideGrouping")
        slides = group.find("array[@rvXMLIvarName='slides']")
        slide = slides.find("RVDisplaySlide")
        if ("Only one line" == slide.get("notes")):
            configDict["singleLine"] = True
        else:
            configDict["singleLine"] = False
        displayElements = slide.find("array[@rvXMLIvarName='displayElements']")
        textElement = displayElements.find(
            "RVTextElement[@displayName='TextElement']")
        rtfDataText = textElement.find("NSString[@rvXMLIvarName='RTFData']")
        textStyle = base64.standard_b64decode(
            rtfDataText.text).split(b'This is the template Text')[0]
        captionElement = displayElements.find(
            "RVTextElement[@displayName='CaptionTextElement']")
        captionStyle = ""
        if captionElement != None:
            rtfDataText = captionElement.find(
                "NSString[@rvXMLIvarName='RTFData']")
            captionStyle = base64.standard_b64decode(
                rtfDataText.text).split(b'This is the caption template')[0]
        lowerShapeElement = displayElements.find(
            "RVShapeElement[@displayName='BottomLineShapeElement']")
        upperShapeElement = displayElements.find(
            "RVShapeElement[@displayName='TopLineShapeElement']")
        arrangements = rvPresentationDocument.find(
            "array[@rvXMLIvarName='arrangements']")
        arrangement = arrangements[0]
        arrangementNSString = arrangement[0][0]
        # remove not needed elements
        displayElements.remove(textElement)
        if captionElement != None:
            displayElements.remove(captionElement)
        if lowerShapeElement != None:
            displayElements.remove(lowerShapeElement)
        if upperShapeElement != None:
            displayElements.remove(upperShapeElement)
        slides.remove(slide)
        groups.remove(group)
        arrangements.remove(arrangement)
        arrangement[0].remove(arrangementNSString)
        # add elements to configDict
        configDict["rvPresentationDocument"] = rvPresentationDocument
        configDict["group"] = group
        configDict["slide"] = slide
        configDict["textElement"] = textElement
        configDict["textStyle"] = textStyle
        configDict["captionElement"] = captionElement
        configDict["captionStyle"] = captionStyle
        configDict["lowerShapeElement"] = lowerShapeElement
        configDict["upperShapeElement"] = upperShapeElement
        configDict["arrangement"] = arrangement
        configDict["arrangementNSString"] = arrangementNSString
        # append current config to config list
        configAll["fileConfigs"].append(configDict)


def ParseConfigFilesPro7(configAll):
    # loop over all config files in the subfolders
    configAll["fileConfigs7"] = []

    __file = __file__.decode(sys.getfilesystemencoding())
    dirname = os.path.dirname(os.path.abspath(__file))
    folder = u"..\\..\\**\\config_*.pro"
    root = os.path.join(dirname, folder)
    for file in glob.glob(root):
        print('Parsing "{0}"'.format(file))
        configDict = {}
        # save path
        configDict["path7"] = os.path.dirname(os.path.abspath(file))
        # save style name
        configDict["styleName7"] = re.search('config_(.*).pro', file).group(1)
        presentation = presentation_pb2.Presentation()
        f = open(file, "rb")
        presentation.ParseFromString(f.read())
        f.close()
        presentation.selected_arrangement.Clear()
        presentation.ClearField("cue_groups")
        presentation.ccli.Clear()
        #check if single line and get notesRTF
        if "Only one line" in presentation.cues[0].actions[0].slide.presentation.notes.rtf_data:
            configDict["singleLine7"] = True
            configDict["notesRTF7"] = presentation.cues[0].actions[0].slide.presentation.notes.rtf_data.split(
                'Only one line')[0]
        else:
            configDict["singleLine7"] = False
            configDict["notesRTF7"] = presentation.cues[0].actions[0].slide.presentation.notes.rtf_data.split(
                'This is the template Text')[0]
            configDict["notesSecondRTF7"] = presentation.cues[0].actions[0].slide.presentation.notes.rtf_data.split(
                'With second line')[0].split('This is the template Text')[1]
        presentation.cues[0].actions[0].slide.presentation.notes.rtf_data = ""
        #get elements
        for elements in presentation.cues[0].actions[0].slide.presentation.base_slide.elements:
            if elements.element.name == "TextElement":
                configDict["textElement7"] = elements
                configDict["textStyle7"] = elements.element.text.rtf_data.split(
                    'This is the template Text')[0]
                if configDict["singleLine7"] == False:
                    configDict["textStyleSecond7"] = elements.element.text.rtf_data.split(
                        'With second line')[0].split('This is the template Text')[1]
            elif elements.element.name == "CaptionTextElement":
                configDict["captionElement7"] = elements
                configDict["captionStyle7"] = elements.element.text.rtf_data.split(
                    'This is the caption template')[0]
                if configDict["singleLine7"] == False:
                    configDict["captionStyleSecond7"] = elements.element.text.rtf_data.split(
                        'and caption second line')[0].split('This is the caption template')[1]
            elif elements.element.name == "BottomLineShapeElement":
                configDict["lowerShapeElement7"] = elements
            elif elements.element.name == "TopLineShapeElement":
                configDict["upperShapeElement7"] = elements
        presentation.cues[0].actions[0].slide.presentation.base_slide.ClearField(
            "elements")
        configDict["slide7"] = presentation.cues[0]
        presentation.ClearField("arrangements")
        presentation.ClearField("cues")
        configDict["presentation7"] = presentation
        # append current config to config list
        configAll["fileConfigs7"].append(configDict)
