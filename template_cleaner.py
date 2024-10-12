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
import css_file_reader


html_files_found = [] # store absolut path of each html file
css_files = [] # store absolut path of each css file
html_search_obj = {} # {"html": '../zappizza.github.io/index.html', id_att: ['abc'], css_att: ['xyz]}
css_search_obj = {} # {"css": '../zappizza.github.io/css/style.css', id_match: ['abc'], css_match: ['xyz], id_no_match: ['abc'], css_no_match: ['xyz]}

html_reader = HtmlFileReader()

def html_search(paths):
    print("====================================================================")
    print("=======================  Reading HTML files  =======================")
    html_file_list = html_reader.find_html_file(paths)
    print(f"Response from find_html_file: {html_file_list}")
    dup_list = []
    for path in html_file_list:
        dup_list.append(html_reader.read_file_and_collect_att(path))
    return list(set(sum(dup_list, [])))

def controller():
    user_input = os_helper.check_user_input(sys.argv)
    unique_att_list = html_search(user_input)
    print(f"Unique attributes found: {len(unique_att_list)}")

    
    print("===================================================================")
    print("===================================================================")
    print("=======================  Reading CSS files  =======================")


    css_searching = True
    css_directories = [user_input]
    while css_searching:
        print("===================================================================")
        css_list = css_file_reader.find_css_files(css_directories[0])
        css_directories.pop(0)
        print(f"css_directories: {css_directories}")
        print(f"CSS search result: {css_list}")

        # if css files found, append to the css_list for later
        if len(css_list[0]) >= 1:
            css_files.append(css_list[0])
        
        # if css directory found, search for more css files in these directories
        if len(css_list[1]) >= 1:
            for css_dir in css_list[1]:
                css_directories.append(css_dir)

        if len(css_directories) == 0:
            print("Ending the search")
            css_searching = False

    print("===================================================================")
    css_files_list = list(sum(css_files, []))
    print(f"List of all css files found: {css_files_list}")


    


    




controller()
print('End of the script')

