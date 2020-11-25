import glob
import re
import xml.etree.ElementTree as ET
import base64
import sys

def ParseConfigFiles(configs):
  #loop over all config files in the subfolders
  for file in  glob.glob("../**/config_*.pro6", recursive = True):
    configDict = {}
    #save path
    configDict["path"] = file
    #save style name
    configDict["styleName"] = re.search('config_(.*).pro6', file).group(1)
    #read config file
    f = open(file, "r")
    configInput = f.read()
    f.close()
    tree = ET.parse(file)
    #get needed elements
    rvPresentationDocument = tree.getroot()
    groups = rvPresentationDocument.find("array[@rvXMLIvarName='groups']")
    group = groups.find("RVSlideGrouping")
    slides = group.find("array[@rvXMLIvarName='slides']")
    slide = slides.find("RVDisplaySlide")
    displayElements = slide.find("array[@rvXMLIvarName='displayElements']")
    textElement = displayElements.find("RVTextElement[@displayName='TextElement']")
    rtfDataText = textElement.find("NSString[@rvXMLIvarName='RTFData']")
    textStyle = base64.standard_b64decode(rtfDataText.text).split(b'strokec0 ')[0] + b'strokec0 '
    captionElement = displayElements.find("RVTextElement[@displayName='CaptionTextElement']")
    captionStyle = ""
    if captionElement:
      rtfDataText = captionElement.find("NSString[@rvXMLIvarName='RTFData']")
      captionStyle = base64.standard_b64decode(rtfDataText.text).split(b'strokec0 ')[0] + b'strokec0 '
    lowerShapeElement = displayElements.find("RVShapeElement[@displayName='BottomLineShapeElement']")
    upperShapeElement = displayElements.find("RVShapeElement[@displayName='TopLineShapeElement']")
    #remove not needed elements
    displayElements.remove(textElement)
    if captionElement:
      displayElements.remove(captionElement)
    if lowerShapeElement:
      displayElements.remove(lowerShapeElement)
    if upperShapeElement:
      displayElements.remove(upperShapeElement)
    slides.remove(slide)
    groups.remove(group)
    #add elements to configDict
    configDict["rvPresentationDocument"] = rvPresentationDocument
    configDict["group"] = group
    configDict["slide"] = slide
    configDict["textElement"] = textElement
    configDict["textStyle"] = textStyle
    configDict["captionElement"] = captionElement
    configDict["captionStyle"] = captionStyle
    configDict["lowerShapeElement"] = lowerShapeElement
    configDict["upperShapeElement"] = upperShapeElement
    #append current config to config list
    configs.append(configDict)

def ParseSlide(input, position, output, startingLine):
  #TODO check for special characters and replace them
  slide = []
  #slide has atleast one line so it can be added directly
  slide.append(input[position])
  lines = 1
  #if slide has two lines add second line
  if position + lines < len(input) and input[position + lines] != "":
    slide.append(input[position + lines])
    lines += 1
  #check for empty line after slide
  if position + lines < len(input) and input[position + lines] != "":
    raise Exception("EmptyLineError | line: {0}".format(startingLine + lines), "An empty line was expected after the end of the slide.")
  output.append(slide)
  return position + lines + 1

def ParseGroup(input, position, output, allowedGroups, startingLine):
  outputGroup = {}
  #check if group name is as required
  if input[position] not in allowedGroups:
     raise Exception("UnknownGroupError | line: {0}".format(startingLine), "The group '{0}' was not found.".format(input[position]))
  else:
    outputGroup["name"] = input[position]
    #check empty line after group name
    if input[position + 1] != "":
       raise Exception("EmptyLineError | line: {0}".format(startingLine + 1), "An empty line was expected after group '{0}' but not found.".format(outputGroup["name"]))
    else:
      outputGroup["slides"] = []
      i = position + 2
      #loop over all slides until next group is found
      while i < len(input):
        if input[i] in allowedGroups:
          break
        i = ParseSlide(input, i, outputGroup["slides"], startingLine + i - position)
      output.append(outputGroup)
  return i

def ParseLanguage(input, allowedGroups, startingLine):
  language = {}
  input = input.split("\n")
  language["name"] = input[0]
  language["groups"] = []
  #check for empty line after language name
  if input[1] != "":
    raise Exception("EmptyLineError | line: {0}".format(startingLine + 1), "An empty line was expected after language '{0}' but not found.".format(language["name"]))
  i = 2
  #loop over all input data and parse groups
  while i < len(input):
   i = ParseGroup(input, i, language["groups"], allowedGroups, startingLine + i)
  return language

def ParseArrangement(input, position, output, allowedGroups, startingLine):
  arrangement = {}
  arrangement["name"] = input[position]
  #check for empty line after arrangement name
  if input[position + 1] != "":
    raise Exception("EmptyLineError | line: {0}".format(startingLine + 1), "An empty line was expected after arrangement '{0}' but not found.".format(arrangement["name"]))
  else:
    i = position + 2
    arrangement["order"] = []
    #loop over all groups in arrangement, verify they are as required and add them to the arrangement
    while i < len(input) and input[i] != "":
      if input[i] not in allowedGroups:
        raise Exception("UnknownGroupError | line: {0}".format(startingLine + i - position), "The group '{0}' was not found.".format(input[i]))
      else:
        arrangement["order"].append(input[i])
      i += 1
    output.append(arrangement)
  return i + 1

def ParseArrangements(input, allowedGroups, startingLine):
  splitInput = input.split("\n")
  if splitInput[0] != "Arrangements":
    raise Exception("KeyWordError | line: {0}".format(startingLine), "The KeyWord 'Arrangements' was expected but not found.")
  elif splitInput[1] != "":
    raise Exception("EmptyLineError | line: {0}".format(startingLine + 1), "An empty line was expected after KeyWord 'Arrangements' but not found.")
  else:
    i = 2
    arragements = []
    while i < len(splitInput):
      i = ParseArrangement(splitInput, i, arragements, allowedGroups, startingLine + i)
  return arragements

def ParseTextFile(file):
  allowedGroups = ["Verse 1", "Verse 2", "Verse 3", "Verse 4", "Verse 5", "Verse 6", "Verse 7", "Verse 8", "Verse 9", "Chorus 1", "Chorus 2", "Chorus 3", "Chorus 4", "Chorus 5", "Chorus 6", "Chorus 7", "Chorus 8", "Chorus 9", "Bridge 1", "Bridge 2", "Bridge 3", "Bridge 4", "Bridge 5", "Bridge 6", "Bridge 7", "Bridge 8", "Bridge 9", "Tag 1", "Tag 2", "Tag 3", "Tag 4", "Tag 5", "Tag 6", "Tag 7", "Tag 8", "Tag 9", "Postchorus 1", "Postchorus 2", "Postchorus 3", "Postchorus 4", "Postchorus 5", "Postchorus 6", "Postchorus 7", "Postchorus 8", "Postchorus 9", "Prechorus 1", "Prechorus 2", "Prechorus 3", "Prechorus 4", "Prechorus 5", "Prechorus 6", "Prechorus 7", "Prechorus 8", "Prechorus 9"]
  #read input file
  f = open(file, "r")
  originalInput = f.read()
  f.close()
  output = {}
  output["languages"] = []
  #remove trailing newlines
  originalInput = originalInput.rstrip("\n")
  #split file into segments. One for each language and one for the arragements
  input = originalInput.split("\n\n\n")
  #parse first language
  output["languages"].append(ParseLanguage(input[0], allowedGroups, 1))
  #parse second language if available
  if len(input) == 3:
    pos = originalInput.find(input[1])
    line = originalInput.count("\n", 0, pos) + 1
    output["languages"].append(ParseLanguage(input[1], allowedGroups, line))
  #TODO check that both languages have same number of lines per slides
  #parse backing tracks
  pos = originalInput.find(input[-1])
  line = originalInput.count("\n", 0, pos) + 1
  output["arrangements"] = ParseArrangements(input[-1], allowedGroups, line)
  return output

def CreateOutput(config, inputText):
  







def tempPrintConfig(configs):
  f = open("debug.txt", "w")
  for config in configs:
    f.write(config["path"] + "\n")
    f.write(config["styleName"] + "\n")
    f.write(str(ET.tostring(config["rvPresentationDocument"])) + "\n")
    f.write(str(ET.tostring(config["group"])) + "\n")
    f.write(str(ET.tostring(config["slide"])) + "\n")
    f.write(str(ET.tostring(config["textElement"])) + "\n")
    f.write(str(config["textStyle"]) + "\n")
    if config["captionElement"]:
      f.write(str(ET.tostring(config["captionElement"])) + "\n")
    if config["captionStyle"]:
      f.write(str(config["captionStyle"]) + "\n")
    if config["lowerShapeElement"]:
      f.write(str(ET.tostring(config["lowerShapeElement"])) + "\n")
    if config["upperShapeElement"]:
      f.write(str(ET.tostring(config["upperShapeElement"])) + "\n")
  f.close()

#main
configs = []
ParseConfigFiles(configs)
#tempPrintConfig(configs)
#loop over all files in master
for file in  glob.glob("*.txt", recursive = False):
  try:
    inputText = ParseTextFile(file)
  except Exception as inst:
    errorName, errorText = inst.args
    print("| {0} | file: {1} | {2} |".format(errorName, file, errorText))
  #loop over configs and create output
  for config in configs:
    CreateOutput(config, inputText)

