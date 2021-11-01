import xml.etree.ElementTree as ET
import glob
import os
import re
import base64
import sys


def ParseConfigFiles(configAll):
    # parse masterConfig
    print('Parsing "masterConfig_Groups.pro6"')
    configAll["groupConfigs"] = {}
    __file = __file__.decode(sys.getfilesystemencoding())
    dirname = os.path.dirname(os.path.abspath(__file))
    folder = u"..\\masterConfig_Groups.pro6"
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

    # loop over all config files in the subfolders
    configAll["fileConfigs"] = []

    __file = __file__.decode(sys.getfilesystemencoding())
    dirname = os.path.dirname(os.path.abspath(__file))
    folder = u"..\\..\\**\\config_*.pro6"
    root = os.path.join(dirname, folder)
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
    if len(configAll["fileConfigs"]) == 0:
        raise ValueError(
            'Error: no configuration file was found in sub folder: {0}'.format(root))
