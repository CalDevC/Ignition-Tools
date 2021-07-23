"""
description:
This script will generate tags that are named after each element in a provided list

usage instructions:
Fill in the variables at the top of this file with the information for your project 
and run the script in your project's script console.

Intial tag information should also be changed to meet your needs
"""


# Variables to change
FOLDER_NAME = "" # the name of the folder you want the tags to be generated in
path = "" # the complete path where you want the tags to be generated
nameArr = [] # the array that holds the names of the tags to be generated
collisionPolicy = "o" # what to do when trying to create a tag that already exsts
                      # a - Abort and throw an exception
                      # o - Overwrite and replace existing Tag's configuration
                      # i - Ignore that item in the list.
                      # m - merge, modifying values that are specified in the 
                      #     definition, without impacting values that aren't 
                      #     defined in the definition. Use this when you want 
                      #     to apply a slight change to tags, without having 
                      #     to build a complete configuration object.
                      # NOTE: Defaults to Overwrite

#Initial tag information
opcItemPath = "ns=1;s=" + FOLDER_NAME
opcServer = "Ignition OPC UA Server"
valueSource = "Memory" # the type of tag to generate
sampleMode = "TagGroup"
tagGroup = "Default" # the tag group to assign the tag to
dataType = "Float4" # the data type of the tag
                    # NOTE: this must be an Ignition data type
                    # a full list of Ignition's data types can be found here:
                    # https://docs.inductiveautomation.com/display/DOC80/Tag+Data+Types

for name in nameArr:

	tag = {
			"name": name,           
			"opcItemPath" : opcItemPath,
			"opcServer": opcServer,
			"valueSource": valueSource,
			"sampleMode" : sampleMode,
			"tagGroup" : tagGroup,
			"value": 0,
			"dataType": dataType
		}
	
	system.tag.configure(path, [tag], collisionPolicy)
