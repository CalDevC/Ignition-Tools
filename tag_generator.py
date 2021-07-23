"""
description:
This script will generate tags that are named after each element in a provided list

usage instructions:
Fill in the constant variables at the top of this file with the information for 
your project and run the script in your project's script console.
"""


# Variables to change
FOLDER_NAME = "" # the path where you want the tags to be generated
nameArr = [] # the array that holds the names of the tags to be generated

# Vairables
path = "" + FOLDER_NAME #Where to store new tags
collisionPolicy = "o" #Overwrite tags of the same name
typeDict = {
	
}

#Initial tag information
opcItemPath = "ns=1;s=" + FOLDER_NAME
opcServer = "Ignition OPC UA Server"
valueSource = "Memory"
sampleMode = "TagGroup"
tagGroup = "Default"

for name in nameArr:
	nameList = name.split("_")
	rawType = nameList[-1]
	if rawType in typeDict:
		type = typeDict[rawType]
	
	# Determine format
	if type == "Percent":
		formatString = "#,##0.##%"
	else:
		formatString = "#,##0.##"
		
	# Determine datatype
	if type == "Int":
		dataType = "Int4"
	elif type == "Bool":
		dataType = "Boolean"
	else:
		dataType = "Float4"

	tag = {
			"name": name,           
			"opcItemPath" : opcItemPath,
			"opcServer": opcServer,
			"valueSource": valueSource,
			"sampleMode" : sampleMode,
			"tagGroup" : tagGroup,
			"value": 0,
			"dataType": dataType,
			"formatString": formatString
		}
	
	system.tag.configure(path, [tag], collisionPolicy) #This line works in ignition
