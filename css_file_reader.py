import os_helper

def find_css_files(target_dir):
    print("Looking for css files... ")
    for file in os_helper.list_dir(target_dir):
        if "css" in file.split("."):
            print(f"CSS file found.. {file}")
            if os_helper.does_path_exist(f"{target_dir}/{file}") and os_helper.is_directoty(f"{target_dir}/{file}"):
                target_path = f"{target_dir}/{file}"
                print(f"Target location: {target_path}")
                os_helper.change_dir(target_path)
                for css_file in os_helper.list_dir(os_helper.get_current_location()):
                    if "css" == css_file.split(".")[-1]:
                        print(f"CSS file to be scanned: {css_file}")
                        file_path = f"{os_helper.get_current_location()}/{css_file}"
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