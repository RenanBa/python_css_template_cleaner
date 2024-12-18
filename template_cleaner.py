#!/usr/bin/env python3
# template_cleaner.py


# Objective: Script to remove unecessary code from CSS and SCSS files.
# When using HTML/CSS template, there is always so much unused classes and ids.
# Input: Directory where the web application is.
# Output:
    # Load the web app to record current page layout for later validation
    # List of all CSS, SCSS, JS and HTML files found (along with how many unique class and id)
    # List the CSS and SCSS files initial size
    # Initial number of class and id in the CSS and SCSS files
    # List of how many classes and id in CSS and SCSS files that are not being used
    # List the CSS and SCSS files size after removing unused classes and id (along with how much size was freed)
    # After finish removing, open web app and compare with initial layout
    # Create a css and scss file backup before removing unused attributes
    # If layout is different than initial layout, prompt to revert the changes
    # Able to use a backup file to later restore the css and scss files


import os_helper
import sys
from html_file_reader import *
from css_file_reader import *


html_files = [] # store absolut path of each html file
css_files = [] # store absolut path of each css file
html_search_obj = {} # {"html": '../zappizza.github.io/index.html', id_att: ['abc'], css_att: ['xyz]}
css_search_obj = {} # {"css": '../zappizza.github.io/css/style.css', id_match: ['abc'], css_match: ['xyz], id_no_match: ['abc'], css_no_match: ['xyz]}
html_attributes = []

html_reader = HtmlFileReader()
css_reader = CssFileReader()

def get_html_attributes(html_files):
    # collect html/css attributes using list of html files
    print("=======================  Reading HTML files  =======================")
    for path in html_files:
        html_attributes.append(html_reader.read_file_and_collect_att(path))
    return list(set(sum(html_attributes, []))) # Unify lists and remove duplicated values

def controller():
    user_input = os_helper.check_user_input(sys.argv)
    
    print("===================================================================")
    print("===================================================================")
    print("=======================  Reading files  =======================")

    # Walk through the given directory tree
    for root, dirs, files in os.walk(user_input, topdown=True):
        # Remove files starting with dots
        for dir in dirs:
            if dir.startswith("."):
                dirs.remove(dir)
        
        # Check and collect html or css files
        for file in files:
            file_path = os.path.join(root, file)
            if 'css' in file:
                css_files.append(file_path)
            if 'html' in file:
                html_files.append(file_path)

    html_attr_list = get_html_attributes(html_files)
    
    print("======================= Reading CSS files  =======================")
    css_reader.read_css_file_search_attr(css_files[2], html_attr_list)
        

    print("===================================================================")
    # css_files_list = list(sum(css_files, []))
    # print(f"List of all css files found: {css_files}")
    # print(f"css files found: {css_files}")
    # print(f"Unique html attributes found: {len(html_attr_list)}")
    # print(f"Unique html attributes found: {html_attr_list}")
    

controller()
print('End of the script')

