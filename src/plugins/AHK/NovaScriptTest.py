# Test NovaScript by reading an AHK script, writing the related NovaScript, writing an AHK script with the values
# filled in, reading in the outputted NovaScript, and writing the AHK script after the NovaScript is read.

from src.plugins.AHK.NovaScript.NovaScript import NovaScript

# Create blank NovaScript
test_script = NovaScript()

# Read in the test AHK script
test_script.readAHK("inputAHKScript")

# Create lists to store keys and values to later add to the metadata dictionary
parameters = [
    "ONE",
    "TWO",
    "THREE"
]
values = [
    "1",
    "2",
    "3"
]

# Create a temporary dictionary to store the keys and values
tempDict = dict()
for i in range(3):
    key = parameters[i]
    value = values[i]
    tempDict[key] = value

# Store the metadata
test_script.setMetadata(tempDict)

# Get the metadata
test_metadata = test_script.getMetadata()
print("AHK READ")
print("----------")
print("EXPECTED VALUES: 1 2 3", end='')
print("\tVALUES: ", end='')
for key in test_metadata.keys():
    print(test_script.get(key) + " ", end='')
print()

print("EXPECTED: ONE\t OUTCOME: " + test_script.find("1"))
print("EXPECTED: TWO\t OUTCOME: " + test_script.find("2"))
print("EXPECTED: THREE\t OUTCOME: " + test_script.find("3"))
print()
# Write out the NovaScript with the metadata header
test_script.writeNova("NovaTestScript")

# Write AHK script with plugged in values
test_script.writeAHK("outputAHKScript")

# Read in NovaScript
test_script.readNova("NovaTestScript.nova")

# Check the new keys and values after Nova read
test_metadata = test_script.getMetadata()
print("Nova READ")
print("----------")
print("EXPECTED VALUES: 1 2 3", end='')
print("\tVALUES: ", end='')
for key in test_metadata.keys():
    print(test_script.get(key) + " ", end='')
print()

print("EXPECTED: ONE\t OUTCOME: " + test_script.find("1"))
print("EXPECTED: TWO\t OUTCOME: " + test_script.find("2"))
print("EXPECTED: THREE\t OUTCOME: " + test_script.find("3"))

# Write out AHK after Nova read
test_script.writeAHK("afterNovaRead")
