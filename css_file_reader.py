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
    
    def update_css_blocks(self, css_blocks):
        new_css_block = {}
        for block in css_blocks:
            print("============ Checking CSS Blocks=================")
            # print(block["target_line"])
            # Get which list of lines that needs modification
            line_number_list = block["target_line"]
            for target_line in line_number_list:
                # Get line object with info about the line
                line_data = block[target_line]
                # Get the string line 
                line = line_data["line_str"][:-1]  # remove new line from end \n
                print(f"line_data: {line_data}")
                
                # line to be updated 
                list_line = line.split(" ")
                for attr in line_data["att"]:
                    # print("--- check css attribute ---")
                    # print(f"attr: {attr}")
                    # print(f"list_line: {list_line}")


                    if attr in list_line:
                        # remove the attribute name from the list
                        list_line.remove(attr)
                        # print(f"Block has previous line: {block}")
                        # if block[target_line -1]:
                        #     print(f"Block has previous line: {block[target_line -1]}")
                        # print(True)
                    # print(f"list_line after: {list_line}")
                # End of for attr in line_date
                
                new_line = " ".join(list_line)

                # if the new_line has no character, then don't add new line.
                if len(new_line) <= 0:
                    line_data["line_str"] = new_line
                    # update new_line object
                    new_css_block[target_line] = new_line
                else:
                    line_data["line_str"] = new_line + "\n"
                    new_css_block[target_line] = new_line

            # End of for target_line in line_number_list     
            
        print("/n")
        print(new_css_block)    
        return new_css_block
    
    def write_new_file(self, lines, new_lines, file_name):
        # new_css_file = open(file_name, mode='w+')
        # folder = file_name.split("/")[:-1]
        print(f"New file name: {file_name}")
        print(new_lines)
        # for line in lines:
        #     if 


        

                    
    def read_css_file_search_attr(self, target_dir, att_list):
        print(f"Reading file: {target_dir}")
        att_list = ["list-check", "list-round", "btn", "no-padding", "gap-60", "gap-40", "gap-30"]
        loaded_file, css_remove_blocks = self.read_file(target_dir, att_list)
        print(loaded_file)
        print(css_remove_blocks)
        updated_blocks = self.update_css_blocks(css_remove_blocks)
        
        print(target_dir)
        folder = "/".join(target_dir.split("/")[:-1])
        name = target_dir.split("/")[-1]
        self.write_new_file(loaded_file, updated_blocks, f"{folder}/new_{name}")


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