import re

# Wrapper class for an AHK script that allows a user to store any value in a variable
#
# @author 2018-07-19 Adam Goins and Kaitlyn Lee
#
# @internal
#   @history 2018-07-19 Adam Goins and Kaitlyn Lee - Original version.
#   @history 2018-07-23 Kaitlyn Lee - Added test and documentation.
#
class NovaScript:

    # Constructs a blank NovaScript
    def __init__(self):
        self.m_metadata = dict()
        self.m_body     = ""

    # Set the meta data
    #
    # @param params The metadata dict with stored values
    #
    def setMetadata(self, params):
        self.m_metadata = params

    # Returns the metadata dict
    #
    # @return Dictionary with stored values
    #
    def getMetadata(self):
        return self.m_metadata

    # Adds a key-value pair to the metadata dict
    #
    # @param key The key
    #
    # @param value The value
    #
    def set(self, key, value):
        self.m_metadata[key] = value

    # Returns the value related to the key
    #
    # @param key The key
    #
    # @return The value
    #
    def get(self, key):
        return self.m_metadata[key]

    # Returns the key related to the value
    #
    # @param value The value
    #
    # @param value The key
    #
    def find(self, value):
        for key in self.m_metadata:
            if self.m_metadata[key] == value:
                return key

    # Writes an AHK script by replacing [$KEY] with the value
    #
    # @param filename The output AHK file
    #
    def writeAHK(self, filename):
        try:
            scriptBody = self.m_body

            for key in self.m_metadata:
                value = self.m_metadata[key]
                scriptBody = scriptBody.replace("[$" + key + "]", value)

            file = open(filename, "w")
            file.write(scriptBody)
            file.close()

        except:
            print("ERROR: Could not write file:", filename)
            return None

    # Writes a NovaScript with the metadata header
    # Key-value pair layout: KEY:=VALUE
    #
    # @param filename The output NovaScript file
    #
    def writeNova(self, filename):

        metadata = []
        metadata += "[METADATA]\n"

        for key in self.m_metadata.keys():
            value = self.m_metadata[key]
            metadata += key + ":=" + value + "\n"

        metadata += "[/METADATA]\n\n"

        try:
            file = open(filename + ".nova", "w")

            # Write the metadata header
            for line in metadata:
                file.write(line)

            # Write the body of the AHK script with [$KEY] in place of hardcoded values
            file.write(self.m_body)
            file.close()

        except:
            print("ERROR: Could not write file:", filename)
            return None

    # Reads an AHK script and sets m_body to the file contents
    #
    # @param filename The input AHK file
    #
    def readAHK(self, filename):
        try:
            self.clearData()
            file = open(filename, "r")
            self.m_body = file.read()

        except:
            print("ERROR: Could not read AHK:", filename)
            return None

    # Reads a NovaScript, parses the metadata header and body, populates m_metadata and m_body.
    #
    # @param filename The input NovaScript file
    #
    def readNova(self, filename):
        try:
            self.clearData()
            file = open(filename, "r")

            fileContents = file.read()
            mdHeader = self.readHeader(fileContents)
            self.parseHeader(mdHeader)
            self.m_body = self.readBody(fileContents)

        except:
            print("ERROR: Could not read Nova:", filename)
            return None

    # Helper method that returns the body of the NovaScript
    #
    # @param content The NovaScript file contents
    #
    # @return The body of the script
    #
    def readBody(self, content):

        startTag   = "[/METADATA]\n\n"
        startIndex = content.index(startTag) + len(startTag)
        return content[startIndex::]

    # Helper method that returns the metadata header of the NovaScript
    #
    # @param content The NovaScript file contents
    #
    # @return The metadata header of the script
    #
    def readHeader(self, content):

        startTag = "[METADATA]"
        endTag   = "[/METADATA]"

        startIndex = content.index(startTag) + len(startTag)
        endIndex   = content.index(endTag)

        return content[startIndex: endIndex]

    # Helper method that parses the NovaScript metadata header and populates m_metadata.
    #
    # @param header The NovaScript metadata header
    #
    def parseHeader(self, header):

        # Reset to blank dictionary before adding to it.
        self.m_metadata = dict()
        
        for line in header.split("\n"):
            # Matches everything before := as a key and everything after as a value
            match = re.match( r'(.*):=(.*)', line, re.M | re.I )
            if not match:
                # No match was found
                continue

            key   = match.group(1)
            value = match.group(2)
            self.set(key, value)

    # Cleans the member variables
    def clearData(self):
        self.m_metadata = dict()
        self.m_body = ""