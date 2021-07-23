# Ignition-Tools
Helpful python scripts for Inductive Automation's Ignition that can automate tedious or time consuming tasks.

## Usage Instructions
Each script has documentation written at the top of the file to describe the scripts purpose and how to use it, but for convience a description of each file is listed here. Most of these scripts need to be run inside the script console within your ignition project.

## The Scripts
### alarm_tag_updater.py
#### description:
This script will traverse a file structure and change specified alarm attributes for all tags within the structure that have alarms linked to them. By default all sub-directories within the specified path will also be affected. To disable this functionality set the 'ALTER_SUBDIR' flag to 'False'.
#### usage instructions:
Fill in the constant variables at the top of this file with the information for your project and run the script in your project's script console.

### tag_generator.py
#### description:
This script will generate tags that are named after each element in a provided list

#### usage instructions:
Fill in the variables at the top of this file with the information for your project 
and run the script in your project's script console.

Intial tag information should also be changed to meet your needs
