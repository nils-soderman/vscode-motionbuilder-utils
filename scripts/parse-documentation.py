# Script for parsing the MB documentation and creating a json table with all of the avaliable pages

import requests
import json
import os
import re

# https://download.autodesk.com/us/motionbuilder/sdk-documentation/
# https://download.autodesk.com/us/motionbuilder/sdk-documentation/contents-data.html

URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/scripts/toc-treedata.js"

DOCUMENTATION_DIR = os.path.join(os.path.dirname(__file__), "..", "documentation")


def RequestData(Url: str):
    Response = requests.get(Url)
    return Response.text


def ExtractData(Data: str, Requirement: str, Filename: str):
    Items = re.findall(
        '(id: "(.*)"\n,ttl: "(.*)"\n,ln: "%s(.*)")' % Requirement, Data)
    ExtractedData = {}

    for Match, Id, Title, Url in Items:
        Id = Id
        Url = Requirement + Url
        Title = Title

        ExtractedData[Title] = {"url": Requirement + Url, "id": Id}

    SaveData(ExtractedData, Filename)


def SaveData(Content, Filename):
    Filepath = os.path.join(DOCUMENTATION_DIR, "%s.json" % Filename)
    with open(Filepath, "w+") as File:
        json.dump(Content, File)


def main():
    Data = RequestData(URL)
    ExtractData(Data, "./", "guide")
    ExtractData(Data, "SDKRef", "c")
    ExtractData(Data, "PythonSDK", "python")
    ExtractData(Data, "SDKSamples", "examples")


if __name__ == "__main__":
    main()
