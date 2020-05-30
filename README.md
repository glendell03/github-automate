# github-automate

- clone the repository
- open it on your code editor

## Edit this line 

***linux*** 

chrome_options.binary_location = "/usr/bin/google-chrome"

***Mac (Uncomment if your mac user)***

#chrome_options.binary_location = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"

***Windows (Uncomment if your windows user)***

#chrome_options.binary_location = "C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe"

***Username and Password***
- driver.find_element_by_xpath(username_input).send_keys("YOUR USERNAME")
- driver.find_element_by_xpath(password_input).send_keys("YOUR PASSWORD")

## Run
- Open terminal and go to the directory
- run python3 main.py Name-of-repository
- ex. python3 main.py github-automate
