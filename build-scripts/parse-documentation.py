# Script for parsing the MB documentation and creating a json table with all of the avaliable pages

from typing import Dict
import requests
import json
import os
import re

# https://download.autodesk.com/us/motionbuilder/sdk-documentation/
# https://download.autodesk.com/us/motionbuilder/sdk-documentation/contents-data.html

URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/scripts/toc-treedata.js"

DOCUMENTATION_DIR = os.path.join(
    os.path.dirname(__file__), "..", "documentation")

class FDictTags:
    Title = "ttl"
    Url = "ln"
    Id = "id"
    Children = "children"
    Ic = "ic"


def RequestData(Url: str):
    Response = requests.get(Url)
    return Response.text


def SaveData(Content, Filename):
    Filepath = os.path.join(DOCUMENTATION_DIR, "%s.json" % Filename)
    with open(Filepath, "w+") as File:
        json.dump(Content, File)


def RawContentToDict(RawContent):
    JsonString = ""

    for Line in RawContent.split(";"):
        if "ttl:" in Line:
            JsonString = Line
            break

    if not JsonString:
        return {}

    JsonString = JsonString.split("=")[1]

    for Key in ["id", "ttl", "ln", "ic", "children"]:
        JsonString = JsonString.replace('%s:' % Key, '"%s":' % Key)

    return json.loads(JsonString)


def nested(inDict):
    Items = []
    for dict in inDict:
        if FDictTags.Children in dict:
            Items += nested(dict[FDictTags.Children])
        else:
            Items.append(dict)
    return Items


def ConstructFlatJson(Data: dict, Filename: str, IgnoreTitles = []):
    DictToSave = {}
    for object in nested([Data]):
        if object[FDictTags.Title] in IgnoreTitles:
            continue
        DictToSave[object[FDictTags.Title]] = {"url": object[FDictTags.Url], "id": object[FDictTags.Id]}

    SaveData(DictToSave, Filename)


def ConstructExampleJson(Data: dict, Filename: str):
    DictToSave = {}
    
    for object in Data[FDictTags.Children][0][FDictTags.Children]:
        Category = object[FDictTags.Title]
        for Page in object[FDictTags.Children]:
            Title = "%s: %s" % (Category, Page[FDictTags.Title])
            DictToSave[Title] = {"url": Page[FDictTags.Url], "id": Page[FDictTags.Id]}

    SaveData(DictToSave, Filename)


def main():
    RawContent = RequestData(URL)
    Data = RawContentToDict(RawContent)

    ConstructFlatJson(Data[0], "guide")
    ConstructFlatJson(Data[1], "c", IgnoreTitles = ["methods."])
    ConstructFlatJson(Data[2], "python")
    ConstructExampleJson(Data[3], "examples")


if __name__ == "__main__":
    main()
