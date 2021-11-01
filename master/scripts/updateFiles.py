# -- coding: utf-8 --

import glob
import re
import xml.etree.ElementTree as ET
import base64
import sys
import copy
import uuid
import io
import os
import codecs
import unicodedata
import Tkinter
import Tkconstants
import tkFileDialog


class ScriptException(Exception):
    def __init__(self, name, line, text):
        self.name = name
        self.line = line
        self.text = text

    def __str__(self):
        return repr(self)


def ParseConfigFiles(configAll):
    # parse masterConfig
    print('Parsing "masterConfig_Groups.pro6"')
    configAll["groupConfigs"] = {}
    tree = ET.parse("masterConfig_Groups.pro6")
    groups = tree.find("array[@rvXMLIvarName='groups']")

    for group in groups:
        groupOut = {}
        groupOut["color"] = group.get("color")
        groupOut["hotKey"] = group[0][0].get("hotKey")
        configAll["groupConfigs"][group.get("name")] = groupOut

    # loop over all config files in the subfolders
    configAll["fileConfigs"] = []

    for file in glob.glob("../**/config_*.pro6"):
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


def ParseSlide(input, position, output, startingLine):
    slide = []
    # slide has atleast one line so it can be added directly
    slide.append(input[position].strip())
    lines = 1
    # if slide has two lines add second line
    if position + lines < len(input) and input[position + lines] != "":
        slide.append(input[position + lines].strip())
        lines += 1
    # check for empty line after slide
    if position + lines < len(input) and input[position + lines] != "":
        raise ScriptException(
            "EmptyLineError", "{0}".format(startingLine + lines),
            "An empty line was expected after the end of the slide.")
    output.append(slide)
    return position + lines + 1


def ParseGroup(input, position, output, groupConfig, startingLine):
    # check if group name is as required
    if input[position] not in groupConfig:
        raise ScriptException(
            "UnknownGroupError", "line: {0}".format(startingLine),
            "The group '{0}' was not found.".format(input[position]))
    elif input[position] in output:
        raise ScriptException(
            "GroupUsedTwice", "line: {0}".format(position + 1),
            "The group '{0}' was used multiple times.".format(input[position]))
    else:
        name = input[position]
        output[name] = []
        # check empty line after group name
        if input[position + 1] != "":
            raise ScriptException(
                "EmptyLineError", "line: {0}".format(startingLine + 1),
                "An empty line was expected after group '{0}' but not found.".
                format(output["name"]))
        else:
            i = position + 2
            # loop over all slides until next group is found
            while i < len(input):
                if input[i] in groupConfig:
                    break
                i = ParseSlide(input, i, output[name],
                               startingLine + i - position)
    return i


def ParseLanguage(input, groupConfig, startingLine):
    language = {}
    input = input.split("\n")
    language["name"] = input[0]
    language["groups"] = {}
    # check for empty line after language name
    if input[1] != "":
        raise ScriptException(
            "EmptyLineError", "line: {0}".format(startingLine + 1),
            "An empty line was expected after language '{0}' but not found.".
            format(language["name"]))
    i = 2
    # loop over all input data and parse groups
    while i < len(input):
        i = ParseGroup(input, i, language["groups"], groupConfig,
                       startingLine + i)
    return language


def ParseArrangement(input, position, output, groupConfig, startingLine):
    arrangement = {}
    arrangement["name"] = input[position]
    # check for empty line after arrangement name
    if input[position + 1] != "":
        raise ScriptException(
            "EmptyLineError", "line: {0}".format(startingLine + 1),
            "An empty line was expected after arrangement '{0}' but not found."
            .format(arrangement["name"]))
    else:
        i = position + 2
        arrangement["order"] = []
        # loop over all groups in arrangement, verify they are as required and add them to the arrangement
        while i < len(input) and input[i] != "":
            if input[i] not in groupConfig:
                raise ScriptException(
                    "UnknownGroupError",
                    "line: {0}".format(startingLine + i - position),
                    "The group '{0}' was not found.".format(input[i]))
            else:
                arrangement["order"].append(input[i])
            i += 1
        output.append(arrangement)
    return i + 1


def ParseArrangements(input, groupConfig, startingLine):
    splitInput = input.split("\n")
    arragements = []
    if splitInput[0] != "Arrangements":
        raise ScriptException(
            "KeyWordError", "line: {0}".format(startingLine),
            "The KeyWord 'Arrangements' was expected but not found.")
    elif len(splitInput) == 1:
        # no arrangement available
        pass
    elif splitInput[1] != "":
        raise ScriptException(
            "EmptyLineError", "line: {0}".format(startingLine + 1),
            "An empty line was expected after KeyWord 'Arrangements' but not found."
        )
    else:
        i = 2

        while i < len(splitInput):
            i = ParseArrangement(splitInput, i, arragements, groupConfig,
                                 startingLine + i)
    return arragements


def CheckOutput(output):
    # if two languages check all groups have same number of slides and lines per slide
    if len(output["languages"]) == 2:
        # check if both languages have same number of groups
        if len(output["languages"][0]["groups"]) != len(
                output["languages"][1]["groups"]):
            raise ScriptException(
                "GroupError", "-",
                "The language '{0}' has '{1}' groups but language '{2}' has '{3}'"
                .format(output["languages"][0]["name"],
                        len(output["languages"][0]["groups"]),
                        output["languages"][1]["name"],
                        len(output["languages"][1]["groups"])))
        # check if all groups are in both languages
        for group in output["languages"][0]["groups"]:
            if group not in output["languages"][1]["groups"]:
                raise ScriptException(
                    "GroupError", "group: {0}".format(group),
                    "The group '{0}' was found in language '{1}' but not in '{2}'"
                    .format(group, output["languages"][0]["name"],
                            output["languages"][1]["name"]))
        # check if all groups have same number of slides and lines per slide
        for group in output["languages"][0]["groups"]:
            if len(output["languages"][0]["groups"][group]) != len(
                    output["languages"][1]["groups"][group]):
                raise ScriptException(
                    "GroupError", "group: {0}".format(group),
                    "The group '{0}' has '{1}' slides in language '{2}' but '{3}' slides in language '{4}'"
                    .format(group,
                            len(output["languages"][0]["groups"][group]),
                            output["languages"][0]["name"],
                            len(output["languages"][1]["groups"][group]),
                            output["languages"][1]["name"]))
            for i in range(0, len(output["languages"][0]["groups"][group])):
                if len(output["languages"][0]["groups"][group][i]) != len(
                        output["languages"][1]["groups"][group][i]):
                    raise ScriptException(
                        "SlideError", "group: {0}".format(group),
                        "Slide number '{0}' in group '{1}' has '{2}' lines in language '{3}' but '{4}' lines in language '{5}'"
                        .format(
                            i, group,
                            len(output["languages"][0]["groups"][group][i]),
                            output["languages"][0]["name"],
                            len(output["languages"][1]["groups"][group][i]),
                            output["languages"][1]["name"]))
        # check if arangements only consist of available groups
        for arrangement in output["arrangements"]:
            for group in arrangement["order"]:
                if group not in output["languages"][0][
                        "groups"] and group != "Instrumental":
                    raise ScriptException(
                        "ArrangementError",
                        "arrangement: {0}".format(arrangement["name"]),
                        "The group '{0}' used in arrangement '{1}' was not found"
                        .format(group, arrangement["name"]))


def ParseTextFile(directory, file, groupConfig):
    # read input file
    f = open(os.path.join(directory, file), 'rb')
    originalInput = f.read().decode("utf-8")
    f.close()
    output = {}
    output["name"] = unicodedata.normalize("NFC", file).replace(".txt", "")
    output["languages"] = []
    # remove trailing newlines
    originalInput = originalInput.rstrip("\n")
    # split file into segments. One for each language and one for the arragements
    input = originalInput.split("\n\n\n")
    # parse first language
    output["languages"].append(ParseLanguage(input[0], groupConfig, 1))
    # parse second language if available
    if len(input) == 3:
        pos = originalInput.find(input[1])
        line = originalInput.count("\n", 0, pos) + 1
        output["languages"].append(ParseLanguage(input[1], groupConfig, line))
    # parse backing tracks
    pos = originalInput.find(input[-1])
    line = originalInput.count("\n", 0, pos) + 1
    output["arrangements"] = ParseArrangements(input[-1], groupConfig, line)
    CheckOutput(output)
    return output


def ReplaceSpecialCharacters(text):
    output = copy.deepcopy(text)
    for i in range(0, len(output)):
        # Ä
        #text[i] = text[i].replace(chr(195) + chr(8222), "\\'c4")
        #text[i] = text[i].replace("Ä", "\\'c4")
        output[i] = output[i].replace(u'\u00c4', "\\'c4")
        # Ö
        #text[i] = text[i].replace(chr(195) + chr(8211), "\\'d6")
        #text[i] = text[i].replace("Ö", "\\'d6")
        output[i] = output[i].replace(u'\u00d6', "\\'d6")
        # Ü
        #text[i] = text[i].replace(chr(195) + chr(339), "\\'dc")
        #text[i] = text[i].replace("Ü", "\\'dc")
        output[i] = output[i].replace(u'\u00dc', "\\'dc")
        # ä
        #text[i] = text[i].replace(chr(195) + chr(164), "\\'e4")
        #text[i] = text[i].replace("ä", "\\'e4")
        output[i] = output[i].replace(u'\u00e4', "\\'e4")
        # ö
        #text[i] = text[i].replace(chr(195) + chr(182), "\\'f6")
        #text[i] = text[i].replace("ö", "\\'f6")
        output[i] = output[i].replace(u'\u00f6', "\\'f6")
        # ü
        #text[i] = text[i].replace(chr(195) + chr(188), "\\'fc")
        #text[i] = text[i].replace("ü", "\\'fc")
        output[i] = output[i].replace(u'\u00fc', "\\'fc")
        # ß
        #text[i] = text[i].replace(chr(195) + chr(376), "\\'df")
        #text[i] = text[i].replace("ß", "\\'df")
        output[i] = output[i].replace(u'\u00df', "ss")
        # ’
        #text[i] = text[i].replace(chr(226) + chr(8364) + chr(8482), "\\'27")
        #text[i] = text[i].replace("’", "\\'27")
        output[i] = output[i].replace(u'\u2019', "\\'27")
    return output


def ReplaceSpecialCharactersForNotes(text):
    output = copy.deepcopy(text)
    for i in range(0, len(output)):
        # Ä
        output[i] = output[i].replace(u'\u00c4', u"\u00c3\u201e")
        # Ö
        output[i] = output[i].replace(u'\u00d6', u"\u00c3\u2013")
        # Ü
        output[i] = output[i].replace(u'\u00dc', u"\u00c3\u0153")
        # ä
        output[i] = output[i].replace(u'\u00e4', "ä")
        # ö
        output[i] = output[i].replace(u'\u00f6', "ö")
        # ü
        output[i] = output[i].replace(u'\u00fc', "ü")
        # ß
        output[i] = output[i].replace(u'\u00df', u"\u00c3\u0178")
        # ’
        output[i] = output[i].replace(u'\u2019', "'")
    return output


def CreateSlide(config, group, text, caption):
    slide = copy.deepcopy(config["slide"])
    # add uuid
    slide.set("UUID", str(uuid.uuid4()))
    # add notes
    myNotes = text
    notes = myNotes[0]
    if (False == config["singleLine"]) and (len(myNotes) == 2):
        notes += "\n" + myNotes[1]
    slide.set("notes", notes)
    displayElements = slide.find("array[@rvXMLIvarName='displayElements']")
    # create textElement
    textElement = copy.deepcopy(config["textElement"])
    # add uuid
    textElement.set("UUID", str(uuid.uuid4()))
    # replace special characters
    myText = ReplaceSpecialCharacters(text)
    # update RTFData
    inputText = config["textStyle"] + myText[0]
    if (False == config["singleLine"]) and (len(myText) == 2):
        inputText += b'\\\n' + myText[1]
    inputText += b'}'
    rtfData = base64.standard_b64encode(inputText)
    nsString = textElement.find("NSString[@rvXMLIvarName='RTFData']")
    nsString.text = rtfData.decode()
    displayElements.append(textElement)
    # create captionElement
    if config["captionElement"] != None and caption != None:
        captionElement = copy.deepcopy(config["captionElement"])
        # add uuid
        captionElement.set("UUID", str(uuid.uuid4()))
        # replace special characters
        myCaption = ReplaceSpecialCharacters(caption)
        # updateRTFData
        inputText = config["captionStyle"] + myCaption[0]
        if (False == config["singleLine"]) and (len(myCaption) == 2):
            inputText += b'\\\n' + myCaption[1]
        inputText += b'}'
        rtfData = base64.standard_b64encode(inputText)
        nsString = captionElement.find("NSString[@rvXMLIvarName='RTFData']")
        nsString.text = rtfData.decode()
        displayElements.append(captionElement)
    # create lowerShapeElement
    if config["lowerShapeElement"] != None:
        lowerShapeElement = copy.deepcopy(config["lowerShapeElement"])
        # add uuid
        lowerShapeElement.set("UUID", str(uuid.uuid4()))
        displayElements.append(lowerShapeElement)
    # create upperShapeElement
    if (config["upperShapeElement"] !=
            None) and (False == config["singleLine"]) and (len(text) == 2):
        upperShapeElement = copy.deepcopy(config["upperShapeElement"])
        # add uuid
        upperShapeElement.set("UUID", str(uuid.uuid4()))
        displayElements.append(upperShapeElement)
    slides = group.find("array[@rvXMLIvarName='slides']")
    slides.append(slide)
    if (True == config["singleLine"]) and (len(text) == 2):
        slide = copy.deepcopy(config["slide"])
        # add uuid
        slide.set("UUID", str(uuid.uuid4()))
        # add notes
        notes = myNotes[1]
        slide.set("notes", notes)
        displayElements = slide.find("array[@rvXMLIvarName='displayElements']")
        # create textElement
        textElement = copy.deepcopy(config["textElement"])
        # add uuid
        textElement.set("UUID", str(uuid.uuid4()))
        # update RTFData
        inputText = config["textStyle"] + myText[1]
        inputText += b'}'
        rtfData = base64.standard_b64encode(inputText)
        nsString = textElement.find("NSString[@rvXMLIvarName='RTFData']")
        nsString.text = rtfData.decode()
        displayElements.append(textElement)
        # create captionElement
        if config["captionElement"] != None and caption != None:
            captionElement = copy.deepcopy(config["captionElement"])
            # add uuid
            captionElement.set("UUID", str(uuid.uuid4()))
            inputText = config["captionStyle"] + myCaption[1]
            inputText += b'}'
            rtfData = base64.standard_b64encode(inputText)
            nsString = captionElement.find(
                "NSString[@rvXMLIvarName='RTFData']")
            nsString.text = rtfData.decode()
            displayElements.append(captionElement)
            # create lowerShapeElement
        if config["lowerShapeElement"] != None:
            lowerShapeElement = copy.deepcopy(config["lowerShapeElement"])
            # add uuid
            lowerShapeElement.set("UUID", str(uuid.uuid4()))
            displayElements.append(lowerShapeElement)
        # create upperShapeElement
        if (config["upperShapeElement"] !=
                None) and (False == config["singleLine"]) and (len(text) == 2):
            upperShapeElement = copy.deepcopy(config["upperShapeElement"])
            # add uuid
            upperShapeElement.set("UUID", str(uuid.uuid4()))
            displayElements.append(upperShapeElement)
        slides = group.find("array[@rvXMLIvarName='slides']")
        slides.append(slide)


def CreateGroup(config, groupConfig, output, name, language, caption):
    group = copy.deepcopy(config["group"])
    # set name
    group.set("name", name)
    # set uuid
    groupUuid = str(uuid.uuid4())
    group.set("uuid", groupUuid)
    # set group color
    group.set("color", groupConfig[name]["color"])
    # add slides to group
    for i in range(0, len(language)):
        if caption == None:
            captionText = None
        else:
            captionText = caption[i]
        CreateSlide(config, group, language[i], captionText)
    # set group hotKey
    firstSlide = group.find("array[@rvXMLIvarName='slides']")[0]
    firstSlide.set("hotKey", groupConfig[name]["hotKey"])
    # add group to array
    groups = output.find("array[@rvXMLIvarName='groups']")
    groups.append(group)
    return groupUuid


def CreateInstrumental(config, groupConfig, output):
    instrumental = copy.deepcopy(config["group"])
    # set name
    instrumental.set("name", "Instrumental")
    # set uuid
    groupUuid = str(uuid.uuid4())
    instrumental.set("uuid", groupUuid)
    # set group color
    instrumental.set("color", groupConfig["Instrumental"]["color"])
    # add empty slide
    slide = copy.deepcopy(config["slide"])
    slide.set("notes", "")
    # add uuid
    slide.set("UUID", str(uuid.uuid4()))
    slides = instrumental.find("array[@rvXMLIvarName='slides']")
    slides.append(slide)
    # set instrumental hotKey
    firstSlide = instrumental.find("array[@rvXMLIvarName='slides']")[0]
    firstSlide.set("hotKey", groupConfig["Instrumental"]["hotKey"])
    # add instrumental to array
    groups = output.find("array[@rvXMLIvarName='groups']")
    groups.append(instrumental)
    return groupUuid


def CreateArrangements(output, arrangements, uuids):
    arrangementsOutput = output.find("array[@rvXMLIvarName='arrangements']")
    for arrangement in arrangements:
        arrangementOutput = copy.deepcopy(config["arrangement"])
        # add uuid
        arrangementOutput.set("uuid", str(uuid.uuid4()))
        arrangementOutput.set("name", arrangement["name"])
        groupIds = arrangementOutput.find("array[@rvXMLIvarName='groupIDs']")
        for group in arrangement["order"]:
            nsString = copy.deepcopy(config["arrangementNSString"])
            nsString.text = uuids[group]
            groupIds.append(nsString)
        arrangementsOutput.append(arrangementOutput)


def CreateOutput(config, groupConfig, name, language, caption, arrangements):
    output = copy.deepcopy(config["rvPresentationDocument"])
    # add uuid
    output.set("uuid", str(uuid.uuid4()))
    # add title
    output.set(
        u"CCLISongTitle", u"{0}_{1}_{2}".format(name, language["name"],
                                                config["styleName"]))
    uuids = {}
    # create groups
    for group in language["groups"]:
        if caption == None:
            captionGroup = None
        else:
            captionGroup = caption["groups"][group]
        uuids[group] = CreateGroup(config, groupConfig, output, group,
                                   language["groups"][group], captionGroup)
    # create Instrumental
    uuids["Instrumental"] = CreateInstrumental(config, groupConfig, output)
    # create arrangements
    CreateArrangements(output, arrangements, uuids)
    # write output to file
    file = os.path.join(
        config["path"], u"{0}_{1}_{2}.pro6".format(name, language["name"],
                                                   config["styleName"]))
    f = open(file, 'w')
    temp = ET.tostring(output)
    f.write(temp)
    f.close()


def CreateOutputs(config, groupConfig, inputText):
    # check if two languages are provided
    if len(inputText["languages"]) == 2:
        CreateOutput(config, groupConfig, inputText["name"],
                     inputText["languages"][0], inputText["languages"][1],
                     inputText["arrangements"])
        CreateOutput(config, groupConfig, inputText["name"],
                     inputText["languages"][1], inputText["languages"][0],
                     inputText["arrangements"])
    else:
        CreateOutput(config, groupConfig, inputText["name"],
                     inputText["languages"][0], None,
                     inputText["arrangements"])


# main
configAll = {}
# TODO add try and errors in parsing
try:
    ParseConfigFiles(configAll)
except ScriptException as e:
    print("| {0} | {1} | {2} |".format(name, line, text))
except Exception as e:
    print(e)
# loop over all files in master
__file = __file__.decode(sys.getfilesystemencoding())
dirname = os.path.dirname(os.path.abspath(__file))
folder = u"textFiles"
root = os.path.join(dirname, folder)
master = Tkinter.Tk()
filenames = tkFileDialog.askopenfilename(
    multiple=True, initialdir=root, title="Select Files to generate", filetypes=(("txt files", "*.txt"),))
filenames = master.tk.splitlist(filenames)
for file in filenames:
    try:
        file = os.path.basename(file).decode("utf-8")
        if file.endswith(".txt"):
            print(u"Generating {0}".format(unicodedata.normalize("NFC", file)))
            inputText = ParseTextFile(root, file, configAll["groupConfigs"])
            # loop over configs and create output
            for config in configAll["fileConfigs"]:
                CreateOutputs(config, configAll["groupConfigs"], inputText)
    except ScriptException as e:
        print("| {0} | {1} | {2} | {3} |".format(file, e.name, e.line, e.text))
    except Exception as e:
        print(e)
