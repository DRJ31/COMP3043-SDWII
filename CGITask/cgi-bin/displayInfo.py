#!/usr/bin/env python3
import cgi, codecs, sys

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer) # Support Chinese

# Variables
form = cgi.FieldStorage()
template = open("../information.html", 'r')  # An html template for information
content = template.read()


# Functions
def getVal(form, attr):  # Get value from html form
    if form.getvalue(attr):
        return form.getvalue(attr)
    return ""


def arrayToString(arr):  # Convert array to string
    if type(arr) is str:
        return arr
    string = ""
    for element in arr:
        string += element
        if element != arr[-1]:  # Check if it is the last element of array
            string += ", "
    return string


# Main function
if __name__ == '__main__':
    # Print data type of text
    print("Content-type:text/html")
    print()
    # Print main content of text
    print(content.format(
        getVal(form, 'username'),
        arrayToString(getVal(form, 'skills[]')),
        getVal(form, 'cities'),
        getVal(form, 'position'),
        arrayToString(getVal(form, 'jobs')),
        getVal(form, 'experience')
    ))



