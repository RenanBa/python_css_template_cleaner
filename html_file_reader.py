import re
import os


class HtmlFileReader():
    def print_test(self):
        print("METHOD FROM ANOTHER FILE")
        return True

    def find_html_file(self, search_dir):
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

    def search_class_in_line(self, line):
        search = re.findall(r"(class[a-zA-Z0-9_-]*=|class[a-zA-Z0-9_-]* = |class[a-zA-Z0-9_-]* == )\"([\s\wa-zA-Z0-9_-]*)\"", line)  # 
        # Check for js script
        if len(search) == 0:
            search_js = re.findall(r"\.[a-zA-Z0-9_-]*\(\"([a-zA-Z0-9_-]*)\"\)", line)
            return search_js
        # Second search to extract the classes from tuples and add into list
        if len(search) >= 1:
            sec_search = re.findall(r"class[a-zA-Z0-9_-]*=\"([\s\wa-zA-Z0-9_-]*)\"", line)
            class_list = " ".join(sec_search).split(" ")
            return class_list

    def search_id_in_line(self, line):
        search = re.findall(r"id=\"([\s\wa-zA-Z0-9_-]*)\"", line)  # 
        id_list = " ".join(search).split(" ")
        # Check for js script
        if len(search) == 0:
            search_js = re.findall(r"\.[a-zA-Z0-9_-]*\(\"([a-zA-Z0-9_-]*)\"\)", line)
            return search_js

        if len(search) >= 1:
            return id_list

    def read_file_and_collect_att(self, file_path):
        att_found_html = []
        with open(file_path, mode='r',encoding='UTF-8') as html_file:
            for line in html_file:
                if "class" in line:
                    att_found_html.append(self.search_class_in_line(line))
                if "id=" in line:
                    att_found_html.append(self.search_id_in_line(line))
            print(f"HTML file ({file_path}) scanned for classes and ids.")
        new_class_list = sum(att_found_html, [])
        return new_class_list
