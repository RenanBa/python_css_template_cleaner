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
import re


class_list_no_dup = []
html_files_found = [] # store absolut path of each html file
css_files = [] # store absolut path of each css file
html_search_obj = {} # {"html": '../zappizza.github.io/index.html', id_att: ['abc'], css_att: ['xyz]}
css_search_obj = {} # {"css": '../zappizza.github.io/css/style.css', id_match: ['abc'], css_match: ['xyz], id_no_match: ['abc'], css_no_match: ['xyz]}




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

    
def find_html_file(search_dir):
    print("Searching for HML files...")
    current_dir_list = os.listdir(search_dir)
    print(f"Listing all files in current dir: {current_dir_list}")
    html_files = []
    for item in current_dir_list:
        item_type = item.split(".")
        if len(item_type) > 1:
            if item_type[1] == "html":
                print(f"HTML files found: {item_type[0]}.{item_type[1]}")
                html_files.append(f"{search_dir}/{item_type[0]}.{item_type[1]}")
    return html_files

def search_class_in_line(line):
    # print(f"css found in this line: {line}")
    search = re.findall(r"(class[a-zA-Z0-9_-]*=|class[a-zA-Z0-9_-]* = |class[a-zA-Z0-9_-]* == )\"([\s\wa-zA-Z0-9_-]*)\"", line)  # 
    # print(f"Regx search found: {search}")
    # Check for js script
    if len(search) == 0:
        search_js = re.findall(r"\.[a-zA-Z0-9_-]*\(\"([a-zA-Z0-9_-]*)\"\)", line)
        return search_js
    # Second search to extract the classes from tuples and add into list
    if len(search) >= 1:
        sec_search = re.findall(r"class[a-zA-Z0-9_-]*=\"([\s\wa-zA-Z0-9_-]*)\"", line)
        class_list = " ".join(sec_search).split(" ")
        return class_list

def search_id_in_line(line):
    search = re.findall(r"id=\"([\s\wa-zA-Z0-9_-]*)\"", line)  # 
    id_list = " ".join(search).split(" ")
    # Check for js script
    if len(search) == 0:
        search_js = re.findall(r"\.[a-zA-Z0-9_-]*\(\"([a-zA-Z0-9_-]*)\"\)", line)
        return search_js

    if len(search) >= 1:
        return id_list


def read_file_and_collect_att(file_path):
    print(f"Scanning HTML file... path: {file_path}")
    # html_files_found.append(file_path)
    att_found_html = []
    with open(file_path, mode='r',encoding='UTF-8') as html_file:
        for line in html_file:
            if "class" in line:
                att_found_html.append(search_class_in_line(line))
            if "id=" in line:
                att_found_html.append(search_id_in_line(line))
        print("HTML file scanned for classes and ids.")
    # Consolidate the list of list into one single list
    new_class_list = sum(att_found_html, [])
    # Remove duplicated items in the list
    class_list_no_dup.append(new_class_list)

    
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

    print(f"Attibutes list before: {class_list_no_dup}")
    html_file_list = find_html_file(user_input)
    print(f"call find_html_file: {html_file_list}")
    read_file_and_collect_att(html_file_list[0])

    # print(f"Attibutes list after: {class_list_no_dup}")

    # all_attributes = list(set(collect_html_att(user_input)))
    # # print(f"Unique attributes found: {all_attributes}")
    # print(f"Unique attributes found: {len(all_attributes)}")

    
    print("===================================================================")
    print("=======================  Reading CSS files  =======================")

    # find_css_files(user_input)
    


    




controller()
print('End of the script')

