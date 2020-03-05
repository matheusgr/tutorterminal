[![Build Status](https://travis-ci.org/matheusgr/tutorterminal.svg?branch=master)](https://travis-ci.org/matheusgr/tutorterminal)

# Tutorterminal

A tool to create scripts to help and learn command line tools.

```text
# Hashs are used to describe text that will be shown to the user.
#
# !checkfile command checks that a file not exists and allow you to continue the script
!checkfile .git
#
# <bold><green>You can use ANSIMARKUP to format your text</green></bold>
#
## Double hashs mark text that are related and used as a help for the next command/input.
#
# run command prompts the user for a command that match the regex indicated...
run git init$
#
# And then you can check if a file exists:
checkfile .git
#
# You can ask the user to press ENTER to continue
enter
#
# And also automatically create a file (example.txt):
### exemple.txt
Arquivo de exemplo com 3 linhas:
Linha 0
Linha 1
Linha 2
###
#
# You can automatically run a command for the user with run_auto
#
run_auto ls
#
# And allow the user to run any command with run_free
run_free 
```


# Commands

# \#

```
# Anything to be displayed
```

Displays a text to the user. You can use [ansimarkups](https://github.com/gvalkov/python-ansimarkup) to format text.

# \##
```
## Anything to be displayed
```
**TODO** A text displayed to the user that can be invoked by the help command.


# \###
```
### filename
file content
may have any number of lines
###
```
Command to create a file that will include any text from that command until the next \###.


## checkfile and !checkfile
```
checkfile file_or_directory_to_be_checked if it exists
!checkfile file_or_directory_to_be_checked if it not exists
```
Checks if a file or directory exists (or not). If condition is not satisfied, the script will stop.

## run
```
run regex_of_command
```
Create a user prompt where user must type a command that satisfies the regex passed as argument.

## run_auto
```
run_auto command
```
Runs an command automatically as an user would (the prompt and command are displayed to the user).

## run_free
```
run_free
```
Allow user to run any command.

# Running tutorterminal
To run tutorterminal execute: 
``` python3 learn_script.py [files] ```

![tutorTermianlGit](https://user-images.githubusercontent.com/38442139/75818262-4fd3e680-5d77-11ea-830f-7734a4748b59.gif)
