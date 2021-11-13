# -- coding: utf-8 --

import uuid
import basicTypes_pb2
import presentation_pb2
import os
import copy


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
        output[i] = output[i].encode()
    return output


def CreateSlide(config, presentation, text, caption):
    slide = copy.deepcopy(config["slide7"])
    #update uuid
    slideUuid = []
    slideUuid.append(str(uuid.uuid4()))
    slide.uuid.string = slideUuid[0]
    slide.actions[0].uuid.string = str(uuid.uuid4())
    slide.actions[0].slide.presentation.base_slide.uuid.string = str(
        uuid.uuid4())
    myText = ReplaceSpecialCharacters(text)
    #create notes
    notes = config["notesRTF7"] + myText[0]
    if (False == config["singleLine7"]) and (len(myText) == 2):
        notes += config["notesSecondRTF7"] + myText[1]
    notes += "}"
    slide.actions[0].slide.presentation.notes.rtf_data = notes
    #add text element
    textElement = copy.deepcopy(config["textElement7"])
    textElement.element.uuid.string = str(uuid.uuid4())
    rftText = config["textStyle7"] + myText[0]
    if (False == config["singleLine7"]) and (len(myText) == 2):
        rftText += config["textStyleSecond7"] + myText[1]
    rftText += "}"
    textElement.element.text.rtf_data = rftText
    slide.actions[0].slide.presentation.base_slide.elements.append(textElement)
    #add caption element
    if "captionElement7" in config and caption != None:
        myCaption = ReplaceSpecialCharacters(caption)
        captionElement = copy.deepcopy(config["captionElement7"])
        captionElement.element.uuid.string = str(uuid.uuid4())
        rftCaption = config["captionStyle7"] + myCaption[0]
        if (False == config["singleLine7"]) and (len(myCaption) == 2):
            rftCaption += config["captionStyleSecond7"] + myCaption[1]
        rftCaption += "}"
        captionElement.element.text.rtf_data = rftCaption
        slide.actions[0].slide.presentation.base_slide.elements.append(
            captionElement)
    #add lower shape element
    if "lowerShapeElement7" in config:
        lowerShape = copy.deepcopy(config["lowerShapeElement7"])
        lowerShape.element.uuid.string = str(uuid.uuid4())
        slide.actions[0].slide.presentation.base_slide.elements.append(
            lowerShape)
    #add upper shape element
    if ("upperShapeElement7" in config) and (False == config["singleLine7"]) and (len(text) == 2):
        upperShape = copy.deepcopy(config["upperShapeElement7"])
        upperShape.element.uuid.string = str(uuid.uuid4())
        slide.actions[0].slide.presentation.base_slide.elements.append(
            upperShape)
    presentation.cues.append(slide)
    #create second slide in case single line is true
    if (True == config["singleLine7"]) and (len(text) == 2):
        slide = copy.deepcopy(config["slide7"])
        #update uuid
        slideUuid.append(str(uuid.uuid4()))
        slide.uuid.string = slideUuid[1]
        slide.actions[0].uuid.string = str(uuid.uuid4())
        slide.actions[0].slide.presentation.base_slide.uuid.string = str(
            uuid.uuid4())
        #create notes
        notes = config["notesRTF7"] + myText[1] + "}"
        slide.actions[0].slide.presentation.notes.rtf_data = notes
        #add text element
        textElement = copy.deepcopy(config["textElement7"])
        textElement.element.uuid.string = str(uuid.uuid4())
        rftText = config["textStyle7"] + myText[1] + "}"
        textElement.element.text.rtf_data = rftText
        slide.actions[0].slide.presentation.base_slide.elements.append(
            textElement)
        #add caption element
        if "captionElement7" in config and caption != None:
            myCaption = ReplaceSpecialCharacters(caption)
            captionElement = copy.deepcopy(config["captionElement7"])
            captionElement.element.uuid.string = str(uuid.uuid4())
            rftCaption = config["captionStyle7"] + myCaption[1] + "}"
            captionElement.element.text.rtf_data = rftCaption
            slide.actions[0].slide.presentation.base_slide.elements.append(
                captionElement)
        #add lower shape element
        if "lowerShapeElement7" in config:
            lowerShape = copy.deepcopy(config["lowerShapeElement7"])
            lowerShape.element.uuid.string = str(uuid.uuid4())
            slide.actions[0].slide.presentation.base_slide.elements.append(
                lowerShape)
        presentation.cues.append(slide)
    return slideUuid


def CreateGroup(config, groupConfig, presentation, name, language, caption):
    group = copy.deepcopy(groupConfig[name])
    #update uuid
    groupUuid = str(uuid.uuid4())
    group.group.uuid.string = groupUuid
    #create slides
    for i in range(0, len(language)):
        if caption == None:
            captionText = None
        else:
            captionText = caption[i]
        slideUuidStr = CreateSlide(
            config, presentation, language[i], captionText)
        #add slides to group
        for slide in slideUuidStr:
            slideUuid = basicTypes_pb2.UUID()
            slideUuid.string = slide
            group.cue_identifiers.append(slideUuid)
    presentation.cue_groups.append(group)
    return groupUuid


def CreateInstrumental(config, groupConfig, presentation):
    #add Instrumental group
    group = copy.deepcopy(groupConfig[groupConfig.keys()[0]])
    #update uuid
    groupUuid = str(uuid.uuid4())
    group.group.uuid.string = groupUuid
    group.group.name = "Instrumental"
    group.group.color.Clear()
    group.group.hotKey.Clear()
    #add Instrumental slide
    slide = copy.deepcopy(config["slide7"])
    #update uuid
    slideUuidStr = str(uuid.uuid4())
    slide.uuid.string = slideUuidStr
    slide.actions[0].uuid.string = str(uuid.uuid4())
    slide.actions[0].slide.presentation.base_slide.uuid.string = str(
        uuid.uuid4())
    presentation.cues.append(slide)
    slideUuid = basicTypes_pb2.UUID()
    slideUuid.string = slideUuidStr
    group.cue_identifiers.append(slideUuid)
    presentation.cue_groups.append(group)
    return groupUuid


def CreateArrangements(config, presentation, arrangements, uuids):
    for arrangement in arrangements:
        arr = presentation_pb2.Presentation.Arrangement()
        arrUuid = str(uuid.uuid4())
        arr.uuid.string = arrUuid
        arr.name = arrangement["name"]
        for group in arrangement["order"]:
            uuidGroup = basicTypes_pb2.UUID()
            uuidGroup.string = uuids[group]
            arr.group_identifiers.append(uuidGroup)
        presentation.arrangements.append(arr)
        presentation.selected_arrangement.string = arrUuid


def CreateOutput(config, groupConfig, name, language, caption, arrangements):
    presentation = copy.deepcopy(config["presentation7"])
    #update uuid
    presentation.uuid.string = str(uuid.uuid4())
    #update name
    songName = "{0}_{1}_{2}".format(
        name.encode('ascii','ignore'), language["name"], config["styleName7"])
    presentation.name = songName
    uuids = {}
    # create groups
    for group in language["groups"]:
        if caption == None:
            captionGroup = None
        else:
            captionGroup = caption["groups"][group]
        uuids[group] = CreateGroup(config, groupConfig, presentation, group,
                                   language["groups"][group], captionGroup)
    # create Instrumental
    uuids["Instrumental"] = CreateInstrumental(
        config, groupConfig, presentation)
    # create arrangements
    CreateArrangements(config, presentation, arrangements, uuids)
    # write output to file
    file = os.path.join(
        config["path7"], u"{0}_{1}_{2}.pro".format(name, language["name"],
                                                   config["styleName7"]))
    f = open(file, 'wb')
    f.write(presentation.SerializeToString())
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
