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


import os
import sys
from html_file_reader import *


html_files_found = [] # store absolut path of each html file
css_files = [] # store absolut path of each css file
html_search_obj = {} # {"html": '../zappizza.github.io/index.html', id_att: ['abc'], css_att: ['xyz]}
css_search_obj = {} # {"css": '../zappizza.github.io/css/style.css', id_match: ['abc'], css_match: ['xyz], id_no_match: ['abc'], css_no_match: ['xyz]}


html_reader = HtmlFileReader()


def does_path_exist(path):
    print("Checking if path exists...")
    return os.path.exists(path)

def is_directoty(path):
    print("Checking if path is a directory...")
    return os.path.isdir(path)

def check_user_input(input):
    print(f"Checking user input: {input}")
    # check if input has user
    if (len(input) > 1):
        # set the parent directory path
        parent_dir = f"../{input[1]}"
        if does_path_exist(parent_dir) and is_directoty(parent_dir):
            print(f"User input is valid: {input[1]}")
            return parent_dir
        else:
            print(f"User input is invlaid")
            sys.exit("Input is not a directory or doesn't exists")
    else:
        print(f"User input is invlaid")
        sys.exit("No directory name was entered")
    
def change_dir(path):
    print("Changing directory...")
    os.chdir(path)

def get_current_location():
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    return current_dir

    
def find_css_files(target_dir):
    print("Looking for css files... ")
    for file in os.listdir(target_dir):
        if "css" in file.split("."):
            print(f"CSS file found.. {file}")
            if does_path_exist(f"{target_dir}/{file}") and is_directoty(f"{target_dir}/{file}"):
                target_path = f"{target_dir}/{file}"
                print(f"Target location: {target_path}")
                change_dir(target_path)
                for css_file in os.listdir(get_current_location()):
                    if "css" == css_file.split(".")[-1]:
                        print(f"CSS file to be scanned: {css_file}")
                        file_path = f"{os.getcwd()}/{css_file}"
                        with open(file_path, mode='r',encoding='UTF-8') as target_file:
                            for line in target_file:
                                print(line)
                                # look for attributes that starts with . or # (class and id).
                                # attributes that start without . or # are HTML elements.
                                    # These attributes should be ignored, but if these attr are followed by . (a.read) then
                                    # the .read should be collected
                                # Attr and elements can be followed by spaces and or comma 
                                    # (a p {...} or .class, class1 {...})
                                    # also: .class1 p {...}
                                # All variation above should be checked for class and id
                                    # complex example:
                                        # .nav-tabs > li.active > a,
                                        # .nav-tabs > li.active > a:focus,
                                        # .nav-tabs > li.active > a:hover,
                                        # .nav-tabs > li > a:hover,
                                        # .nav-tabs > li > a { ... }
                                        # ul.top-info li p.info-text { ... }
                                    # Nested example:
                                        # @media (max-width: 767px) {
                                        #     .btn-primary,
                                                # .btn-dark {
                                                #     font-size: 13px;
                                                # }
                                        #     }

def controller():
    user_input = check_user_input(sys.argv)
    print("====================================================================")
    print("=======================  Reading HTML files  =======================")
    html_file_list = html_reader.find_html_file(user_input)
    print(f"Response from find_html_file: {html_file_list}")
    dup_list = []
    for path in html_file_list:
        dup_list.append(html_reader.read_file_and_collect_att(path))
    unique_list = list(set(sum(dup_list, [])))
    

    print(f"Unique attributes found: {len(unique_list)}")

    
    print("===================================================================")
    print("=======================  Reading CSS files  =======================")

    # find_css_files(user_input)
    


    




controller()
print('End of the script')

