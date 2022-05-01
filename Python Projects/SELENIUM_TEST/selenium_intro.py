## https://selenium-python.readthedocs.io/getting-started.html
## https://www.selenium.dev/documentation/webdriver/
## https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys, getopt, os
from turtle import home
from selenium import webdriver
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.by import By

class Webpage_Search:
    def python_search(self):
        driver = webdriver.Firefox()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        # looking at source-code we see element q on
        # "view-source:https://www.python.org/" is the search box
        elem = driver.find_element(By.NAME, 'q')           
        # clearing the search box for element q just incase
        elem.clear()                                        
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found" not in driver.page_source
        driver.minimize_window()

    def example_search(self):
        driver = webdriver.Firefox()
        driver.get("https://www.example.com")               
        
        # Get all the text and print it out available with tag name 'p'
        # Print out text to file
        elements = driver.find_elements(By.TAG_NAME, 'p')
        home_dir = os.getenv('HOME')
        f = open((home_dir + '/Documents/example_search.txt'), 'w') 
        text_string = ''
        f.write("Body Paragraph: " + text_string + '\n')
        for e in elements:
            text_string = text_string + e.text
            
        # Returns text of h1 of the element
        attr = driver.find_element(By.CSS_SELECTOR, "h1").text
        f.write('Header: ' + attr)
        f.close()


## Executing main function where output is determined by command line arguments
def main(n):
    search_result = Webpage_Search()
    try:
        OPTS, ARGS = getopt.getopt(n, 'ab')
    except getopt.GetoptError:
        sys.exit(print("Incorrect option sent"))
    for OPTS, ARGS in OPTS:
        if OPTS == '-a':
            search_result.python_search()
        elif OPTS == '-b':
            search_result.example_search()

if __name__ == '__main__':
    main(sys.argv[1:])      ## sys.argv is a list with the first index being marked by the file itself, "whatever.py"
