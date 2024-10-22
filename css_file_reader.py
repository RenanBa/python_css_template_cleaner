import os_helper
import re
                    
def read_css_file_search_attr(target_dir, att_list):
    print(f"Reading file: {target_dir}")
    att_list = ["list-round", "list-arrow", "error-page", "error-body", "btn"]

    css_remove_blocks = []  # holds the curly braces to define block start and end
    loaded_file = []
    comment_block = False
    remove_block = False
    count = 0
    with open(target_dir, mode='r',encoding='UTF-8') as target_file:
        css_blocks = []
        block_track = False
        for line in target_file:
            loaded_file.append(line)
            print("============")
            
            # Check for css comment blocks
            if line[:2] == "/*":
                comment_block = True
            
            if not comment_block:
                # print(f"counting line: {count}")
                search = re.findall(r"\.[a-zA-Z0-9_-]*,*|\#[a-zA-Z0-9_-]*,*", line)
                # print(line)
                print(search)
                print(f"SEarch result: {search}")

                if "," in line or "{":
                    block_track = True
                
                if block_track:
                    css_blocks.append({"line_num": count, "line_str": line, "target": False})


                if len(search) >= 1:
                    for item in search:
                        att = item[1:]
                        
                        if "," in item: # check if there are comma in the item
                            att = att[:-1]

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