#folder structure: one master folder containing all songs as .txt with german, english and backing track
#subfolders for each campus containing config files for each style
# parse config of all templates in all subfolders and store config and path in a list
#loop over all songs in master and foreach song over the config list and create a song foreach style in the corresponding path

#TODO beatuifulSOup to parse xml

import glob
import re
import xml.etree.ElementTree as ET
import base64

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

def ParseLanguage(input):
  output = {}
  input = input.split("\n")
  output["name"] = input[0]
  groups = ["Verse 1", "Verse 2", "Verse 3", "Verse 4", "Verse 5", "Verse 6", "Verse 7", "Verse 8", "Verse 9" ]
  for i in range(2,len(input)):
    print(input[i])
  return output

def ParseTextFile(file):
  #read input file
  f = open(file, "r")
  input = f.read()
  f.close()
  output = {}
  output["languages"] = []
  #split file into segments. One for each language and one for the arragements
  input = input.split("\n\n\n")
  #parse first language
  output["languages"].append(ParseLanguage(input[0]))
  #check for special characters and replace them
  #check for max 2 lines per slide
  #parse second language
  #check for special characters and replace them
  #check for max 2 lines per slide
  #check that both languages have same number of lines per slides
  #parse backing tracks
  return output

def CreateOutput(config, input):
  print("test")
  #if english call with english as text and german as caption
  #if german call with german and english as caption

def CreateSingleLanguage(config, input, text, caption, language):
  print("test")
  #open file with name from input language and style from config












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
  inputText = ParseTextFile(file)
  print(inputText)
  #loop over configs
    #createOutput(config, input)
  