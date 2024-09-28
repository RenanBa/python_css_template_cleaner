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

html_files = [] # store absolut path of each html file
css_files = [] # store absolut path of each css file
class_list_no_dup = []
id_found = []

def does_path_exist(path):
    print("Checking if path is a valid directory...")
    return os.path.exists(path)

def is_directoty(path):
    print("Checking if path is a valid directory...")
    return os.path.isdir(path)

def check_user_input(input):
    print("Checking user input...")
    if (len(input) > 1):
        if does_path_exist(input[1]) and is_directoty(input[1]):
            print(f"User input is valid: {input[1]}")
            return input[1]
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



def read_and_save_html_classes(file_path):
    print(file_path)
    att_found_html = []
    # Read each line ad collect all classes
    with open(file_path, mode='r',encoding='UTF-8') as html_file:
        for line in html_file:
            # if "id"
            if "class" in line:
                print(line)
                search = re.findall(r"class=\"([\s\wa-zA-Z0-9_-]*)\"", line)  # 
                print(search)
                class_list = " ".join(search).split(" ")
                if len(search) >= 1:
                    att_found_html.append(class_list)
            elif "id=" in line:
                search = re.findall(r"id=\"([\s\wa-zA-Z0-9_-]*)\"", line)  # 
                id_list = " ".join(search).split(" ")
                if len(search) >= 1:
                    att_found_html.append(id_list)
    
    # Consolidate the list of list into one single list
    new_class_list = sum(att_found_html, [])
    # Remove duplicated items in the list
    class_list_no_dup.append(list(set(new_class_list)))

    
# Find HTML files and then call read_and_save_html_classes to extract id and class
def get_html_classes(target_dir):
    current_dir_list = os.listdir(target_dir)
    for item in current_dir_list:
        item_type = item.split(".")
        if len(item_type) > 1:
            if item_type[1] == "html":
                print(f"HTML files found: {item_type[0]}.{item_type[1]}")
                read_and_save_html_classes(f"{target_dir}/{item_type[0]}.{item_type[1]}")
                # sys.exit("stoping before ")
    


def controller():

    user_input = check_user_input(sys.argv)
    current_dir = os.getcwd()
    target_dir = f"{current_dir}/{user_input}"

    # get_current_location()
    # print(f"target directory: {target_dir}")

    # change_dir(target_dir)
    # get_current_location()

    print(f"Attibutes list before: {class_list_no_dup}")
    
    get_html_classes(target_dir)
    
    # print(class_list_no_dup)
    # print(len(class_list_no_dup))

    # curent_dir_list = os.listdir(target_dir)
    # for item in curent_dir_list:
    #     print(item.split("."))
    


    




controller()
print('End of the file')

