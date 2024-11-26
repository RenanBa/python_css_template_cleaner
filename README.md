# Objective: Script to remove unnecessary code from CSS and SCSS files.
When using HTML/CSS templates, there are always so many unused classes and IDs that it is difficult to determine whether a given CSS block is used.

## How to run the script:
Input: Directory where the web application is.
e.g. $ ./template_cleaner.py your_app.io

Output:
  - Load the web app to record the current page layout for later validation
  - List of all CSS, SCSS, JS, and HTML files found (along with how many unique classes and id)
  - List the CSS and SCSS file's initial size
  - Initial number of classes and ids in the CSS and SCSS files
  - List of how many classes and id in CSS and SCSS files that are not being used
  - List the CSS and SCSS files size after removing unused classes and id (along with how much size was freed)
  - After finishing removing, open the web app and compare it with the initial layout
  - Create a CSS and SCSS file backup before removing unused attributes
  - If the layout is different than the initial layout, prompt to revert the changes
  - Able to use a backup file to restore the CSS and SCSS files later
