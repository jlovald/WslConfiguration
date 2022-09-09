import json
import glob
import os 
import re
import random

def substitue(st):
    removeDriveLetter = re.sub("/mnt/c/", "C:\\\\", st)
    
    return re.sub("/", "\\\\", removeDriveLetter) 
dirname = os.path.dirname(os.path.realpath(__file__))
f = open(f'{dirname}/settings.json')
data = json.load(f)

profileGuid='{f9ceaf27-504c-58d7-927c-d1d6a7ac7d3c}'
terminalSettingsPath = data["TerminalSettingsPath"]
backgroundImagePath = data["BackgroundsPath"]
jpgs = glob.glob(f"{backgroundImagePath}/*.jpg")
pngs = glob.glob(f"{backgroundImagePath}/*.png")

jpgs.extend(pngs)
backgrounds = jpgs
# print(backgrounds)
f.close()

windowsPaths = list(map(substitue, backgrounds))

# print(windowsPaths)



with open(terminalSettingsPath, "r+") as f:
    data = json.load(f)
    profiles = data["profiles"]["list"]
    elem = next(filter(lambda profile: profile["guid"] == profileGuid, profiles), None)
    
    random.shuffle(windowsPaths)
    # print(elem["backgroundImage"])
    # print(windowsPaths[0])
    windowsPaths = [value for value in windowsPaths if value != elem["backgroundImage"]]
    elem["backgroundImage"] = windowsPaths[0]
    # print(elem["backgroundImage"])
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate() 

