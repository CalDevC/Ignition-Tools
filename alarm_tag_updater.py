"""
description:
This script will traverse a file structure and change specified alarm attributes 
for all tags within the structure that have alarms linked to them. By default all 
sub-directories within the specified path will also be affected. To disable this 
functionality set the 'ALTER_SUBDIR' flag to 'False'.

usage instructions:
Fill in the constant variables at the top of this file with the information for 
your project and run the script in your project's script console.
"""

#Variables to change
ATTRIBUTE    = "" # the name of the alarm attribute you wish to update
NEW_VALUE    = "" # the new value for your specified attribute
PATH         = "[default]" # the path of the direcory you want to make the changes in 
                          # (NOTE: ALL SUB-DIRECTORIES WILL BE AFFECTED UNLESS YOU SET THE ALTER_SUBDIR TO FALSE)
                          # if you want to make changes to every tag in your project then provide the name of your project's tag provider (include square brackets)
ALTER_SUBDIR = True # set to false if you do not want the changes to affect all subdirectories within your specified path


def updateAlarmTags(directory, attribute, new_value, alter_subdirectories):
	path_set = set()
	for path in system.tag.browse(directory):
		path_set.add(path["fullPath"])
		
	for path in path_set:
		tag_info = system.tag.getConfiguration(path)[0]
		
		if u'alarms' in tag_info:
			for alarm in tag_info[u'alarms']:
				alarmConfig = {alarm[u'name']: [ [ attribute, "Value", new_value] ]}
				system.tag.editAlarmConfig([path] , alarmConfig )
		
		if str(tag_info[u'tagType']) == 'Folder' and alter_subdirectories:
			updateAlarmTags(str(tag_info[u'path']), attribute, new_value, alter_subdirectories)
			
updateAlarmTags(PATH, ATTRIBUTE, NEW_VALUE, ALTER_SUBDIR)