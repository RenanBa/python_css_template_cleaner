import os_helper
import re


class CssFileReader():

    def read_file(self, target_dir, att_list):
        print("============")
        # What does read_file do:
        # 1 - Read and save each line in a dictionary type {1: line, 2: line}
        # 2 - Check each line for regex pattern for classes and ids
        # 3 - If regex pattern found, save the css_blocks and flag which line is the match
        # 4 - Return loaded_file with all lines, and return 
        
        # holds the curly braces to define block start and end css_remove_blocks with regex matches css blocks
        css_remove_blocks = []
        # Load each line from the file without any modification {1: line, 2: line}
        loaded_file = {}
        # Track if the current line is part of a comment block or not
        comment_block = False
        # remove_block will be used to determine if the css_blocks will be saved to later modification
        remove_block = False
        count = 1
        with open(target_dir, mode='r',encoding='UTF-8') as target_file:
            css_blocks = {"target_line": []}
            block_track = False
            for line in target_file:
                loaded_file[count] = line
                
                # Check for css comment blocks
                if line[:2] == "/*":
                    comment_block = True
                
                if not comment_block:
                    search = re.findall(r"\.[a-zA-Z0-9_-]*,*|\#[a-zA-Z0-9_-]*,*", line)
                    # print(f"SEarch result: {search}")

                    # Check for characters that opens a css block
                    if "," in line or "{" in line:
                        block_track = True
                    
                    # Collect the whole css block for later modification if needed

                    if block_track:
                        # print(f"LIne: {count} | {line}")
                        css_blocks[count] = {"line_str": line, "att": []}

                    # print(css_blocks)
                    # Check if there are matches
                    if len(search) >= 1:
                        # Go over each match found in the current line
                        for item in search:
                            att = item[1:] # Remove . or # from the start of the string
                            if "," in item: # check if there are comma in the item and remove it
                                att = att[:-1]

                            # Check if the att is in the html files attribute list
                            if att not in att_list:
                                remove_block = True
                                css_blocks[count]["att"].append(item)

                                if count not in css_blocks["target_line"]:
                                    css_blocks["target_line"].append(count)

                                print(F"Item not in att_list: {att}")
                            # End of att no in att_list
                        # End of for each match (found in the current line)
                    # End of if search >= 1
                # End of if not comment_block

                if line[-3:-1] == "*/":
                    comment_block = False
                
                if "}" == line[-2:-1]:
                    block_track = False
                    css_blocks = {"target_line": []}

                if block_track and remove_block:
                    css_remove_blocks.append(css_blocks)
                    remove_block = False

                count += 1
            # End of for each line
        # End of With open

        return loaded_file, css_remove_blocks
    
    def update_css_blocks(self, css_blocks, att_list):
        new_css_block = {}
        for block in css_blocks:
            print("============ Updating CSS Blocks =================")
            print(block)
            # Get which list of lines that needs modification
            line_number_list = block["target_line"]
            delete_block = False
            for target_line in line_number_list:
                # Get line object with info about the line
                line_data = block[target_line]
                # Get the string line 
                line = line_data["line_str"][:-1]  # remove new line from end \n
                # line to be updated 
                list_line = line.split(" ")
                # Remove each attribute found in this line
                for attr in line_data["att"]:
                    if attr in list_line:
                        list_line.remove(attr)
                # End of for attr in line_date
                

                # AFter removing the line, check what is the line before and after the current line
                    # If the end of current line has { then check the line before
                    # If the line before has attribute then move the { to the line before
                    # IF the line before has attribute and ends with comman, remove the comma and move the { to it
                    # If the line has no attribute, then remove then delete all lines in the current block
                if len(list_line) == 1:
                    if list_line[-1] == "{":
                        
                        # While the previous line is an empty string 
                        prev_line = target_line - 1
                        if prev_line in block:
                            is_there_prev_line = True
                            while is_there_prev_line:

                                print("There is a line before: ", end=" ")
                                print(block[prev_line])
                                prev_line_str = block[prev_line]['line_str']
                                print(f"LIne number: {prev_line}")
                                print(f"How many lines in the block: {block.keys()}")
                                print(f"previous string: {prev_line_str}")
                                
                                if block[prev_line]['line_str'] != "":
                                    if prev_line_str[-1] == "," or prev_line_str[-2] == ",":
                                        print("The end of prev_line_str has a comma")
                                        # If previous line has attribute that is in the attribute list to be removed, then skip it
                                        # if prev_line_str not in att_list:
                                        if prev_line_str[-2] == ",":
                                            new_css_block[prev_line] = prev_line_str[:-2] + " {\n"
                                        else:
                                            new_css_block[prev_line] = prev_line_str[:-1] + " {\n"
                                        list_line = ""
                                        is_there_prev_line = False


                                        # Update and add the prev_line in the new_css_block
                                        # Empty up the current line and let the bellow actions take care
                                        # new_css_block[prev_line] = new_line
                                
                                # End of if comma check
                                prev_line = prev_line - 1
                                if prev_line not in block.keys():
                                    is_there_prev_line = False
                                    delete_block = True
                            # End of while loop
                        # End if exist a previous line in this block  
                        else:
                            delete_block = True                          

                            
                        # End of check if exist a previous line in block
                    # End of if last item is {
                # End of if list_line == 1


                # line from List to String
                new_line = " ".join(list_line)

                # if the new_line has no character, then don't add new line.
                if len(new_line) <= 0:
                    block[target_line]["line_str"] = new_line
                    new_css_block[target_line] = new_line
                else:
                    block[target_line]["line_str"] = new_line + "\n"
                    new_css_block[target_line] = new_line + "\n"

            # End of for target_line in line_number_list   
            if delete_block:
                for key in block.keys():
                    if "line_str" in block[key]:
                        new_css_block[key] = ""
                        print(f"Key deleted: {key}")


            

        print(new_css_block)    
        return new_css_block
    
    def write_new_file(self, old_file, new_lines, file_name):
        new_css_file = open(file_name, mode='w')
        # print(f"New file name: {file_name}")
        # print(new_lines[10])
        
        # while writing new file
        for index, line_number in enumerate(old_file):
            if line_number in new_lines:
                if new_lines[line_number] != "":
                    new_css_file.write(new_lines[line_number])
                    # print(new_lines[line_number])
            else:
                new_css_file.write(old_file[line_number])
                # print(old_file[line_number])


            # Edge case. 
            line_number += 1
            if line_number == len(old_file):
                writing = False
        new_css_file.close()
 
    def read_css_file_search_attr(self, target_dir, att_list):
        print(f"Reading file: {target_dir}")
        att_list = ["btn", "gap-60", "gap-40", "gap-30"]
        loaded_file, css_remove_blocks = self.read_file(target_dir, att_list)
        # print(loaded_file)
        # print(css_remove_blocks)
        updated_blocks = self.update_css_blocks(css_remove_blocks, att_list)
        
        # Create new file and start to write it
        print(target_dir)
        folder = "/".join(target_dir.split("/")[:-1])
        name = target_dir.split("/")[-1]
        new_file_name = f"{folder}/new_{name}"
        self.write_new_file(loaded_file, updated_blocks, new_file_name)


        # need to check if the previous line has a comma or check if the current line has a comma 
        # at the end. In this case the comma needs to be removed 

        # Also check if there is curly brace at the end. In this case the curly brace 
        # will need to be moved to the end of the previous line



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