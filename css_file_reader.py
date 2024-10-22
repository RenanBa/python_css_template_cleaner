import os_helper
import re
                    
def read_css_file_search_attr(target_dir, att_list):
    print(f"Reading file: {target_dir}")
    att_list = ["list-round", "list-arrow", "error-page", "error-body", "btn"]

    css_remove_blocks = []  # holds the curly braces to define block start and end
    # Load each line from the file without any modification {1: line, 2: line}
    loaded_file = {}
    # Track if the current line is part of a comment block or not
    comment_block = False
    # remove_block will be used to determine if the css_blocks will be saved to later modification
    remove_block = False
    count = 1
    with open(target_dir, mode='r',encoding='UTF-8') as target_file:
        css_blocks = []
        block_track = False
        for line in target_file:
            loaded_file[count] = line
            # loaded_file.append(line)
            print("============")
            
            # Check for css comment blocks
            if line[:2] == "/*":
                comment_block = True
            
            if not comment_block:
                search = re.findall(r"\.[a-zA-Z0-9_-]*,*|\#[a-zA-Z0-9_-]*,*", line)
                print(search)
                print(f"SEarch result: {search}")

                # Check for characters that opens a css block
                if "," in line or "{":
                    block_track = True
                
                # Collect the whole css block for later modification if needed
                if block_track:
                    css_blocks.append({"line_num": count, "line_str": line, "target": False})

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
                            css_blocks[-1]["target"] = True
                            print(F"Item not in att_list: {att}")

                            
                            # need to check if the previous line has a comma or check if the current line has a comma 
                            # at the end. In this case the comma needs to be removed 

                            # Also check if there is curly brace at the end. In this case the curly brace 
                            # will need to be moved to the end of the previous line

                            # sub = re.sub(r"\.[a-zA-Z0-9_-]*,*|\#[a-zA-Z0-9_-]*,*", "", line)
                            # print(f"SUB result: {sub}")
                            

                        else:
                            print(f"Do Nothing - Item is in the att list")
                            pass
                    # End of for each match (found in the current line)
                # End of if search >= 1
            # End of if not comment_block

            if line[-3:-1] == "*/":
                comment_block = False
            
            print(f"Is block tracking: {remove_block}")
            print(f"Is block tracking: {line[-2:-1]}")
            if "}" == line[-2:-1]:
                block_track = False
                css_blocks = []

            if block_track and remove_block:
                css_remove_blocks.append(css_blocks)
                remove_block = False

            count += 1
        # End of for each line
    # End of With open
    print(count)
    print(loaded_file)
    print(css_remove_blocks)



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