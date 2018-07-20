import re

class NovaScript:

    def __init__(self):
        self.m_metadata = dict()
        self.m_body     = ""

    def setMetadata(self, params):
        self.m_metadata = params

    def set(self, key, value):
        self.m_metadata[key] = value

    def get(self, key):
        return self.m_metadata[key]

    def find(self, value):
        for key in self.m_metadata:
            if self.m_metadata[key] == value:
                return key


    def writeAHK(self, filename):
        scriptBody = self.m_body
        for key in self.m_metadata:
            value = self.m_metadata[key]
            scriptBody = scriptBody.replace("[$" + key + "]", value)

        file = open(filename, "w")
        file.write(scriptBody)
        file.close()

    def writeNova(self, filename):

        metadata = []
        metadata += "[METADATA]"

        for key in self.m_metadata:
            value = self.m_metadata[key]
            metadata += key + ":=" + value

        metadata += "[/METADATA]"

        file = open(filename, "w")

        # Write the metadata header with the values for the variablenames
        for line in metadata:
            file.write(line)

        # Write the body of the AHK script with [$VARIABLENAME] in place of hardcoded values
        file.write(self.m_body)
        file.close()

    def readAHK(self, filename):
        try:

            file = open(filename, "r")

            self.m_metadata = dict()
            self.m_body     = file.read()

        except:
            print("ERROR: File doesn't exist:", filename)
            return None


    def readNova(self, filename):

        file = open(filename, "r")

        fileContents = file.read()
        mdHeader = self.readHeader(fileContents)

        self.parseHeader(mdHeader)
        self.m_body = self.readBody(fileContents)

    def readBody(self, content):

        startTag   = "[/METADATA]"
        startIndex = content.index(startTag) + len(startTag)
        return content[startIndex::]

    def readHeader(self, content):

        startTag = "[METADATA]"
        endTag   = "[/METADATA]"

        startIndex = content.index(startTag) + len(startTag)
        endIndex   = content.index(endTag)

        return content[startIndex: endIndex]

    def parseHeader(self, header):

        # Reset to blank dictionary before adding to it.
        self.m_metadata = dict()
        
        for line in header.split("\n"):

            match = re.match( r'(.*):=(.*)', line, re.M | re.I )
            if not match:
                # No match was found
                continue

            key   = match.group(1)
            value = match.group(2)
            self.set(key, value)