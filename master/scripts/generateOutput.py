# -- coding: utf-8 --

import copy
import uuid
import base64
import os
import xml.etree.ElementTree as ET


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


def CreateArrangements(config, output, arrangements, uuids):
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
    CreateArrangements(config, output, arrangements, uuids)
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
