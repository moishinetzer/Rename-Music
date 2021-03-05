import os
import re


def checkfornumber(text):
    if re.match("^([0-9]+[ ]*[.]*[-]*[)]*[ ]*)", text):
        return re.split("^([0-9]+[ ]*[.]*[-]*[)]*[ ]*)", text)[2]
    else:
        return text


def copyedit(text, copycount=1):  # Find a way to count the occurrences instead of just +1
    copysplit = re.split("([.])", text)
    copysplit.insert(-2, (" Copy" * copycount))
    return "".join(copysplit)


cp = 1

for root, dirs, files in os.walk('.'):
    for file in files:
        if file != "Thumbs.db" and file != checkfornumber(file):
            try:
                os.renames("{}\{}".format(root, file), "{}\\{}".format(root, checkfornumber(file)))
                print("Renaming {} to {}".format(file, checkfornumber(file)))
            except FileExistsError:
                os.renames("{}\{}".format(root, file), "{}\\{}".format(root, copyedit(checkfornumber(file), cp)))
                print("Found a copy! Renaming {} to {}".format(file, copyedit(checkfornumber(file), cp)))
                cp += 1

input("Finished renaming all files press enter... ")
