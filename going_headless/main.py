import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


try:
    repository_name = (sys.argv[1])
except:
    print("Please enter repository name")
    print("Python3 main.py ->Repository name<-")
    quit()


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = "/usr/bin/google-chrome"


driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'), chrome_options=chrome_options)
driver.get('https://github.com/login')


def loading(x):
    print(x)
    for i in range(0,100):
        time.sleep(0.01)
        width = (i + 1)/2
        width = int(width)
        bar = "[" + u"\u001b[32;1m#\u001b[0m" * width + " " * (50 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print


username_input = '//*[@id="login_field"]'
password_input = '//*[@id="password"]'
login_submit = '//*[@id="login"]/form/div[4]/input[9]'
new_repo = '//*[@id="repos-container"]/h2/a'
new_repo_name = '//*[@id="repository_name"]'
create_repo = '//*[@id="new_repository"]/div[3]/button'

loading("Creating Github Repository....")
driver.find_element_by_xpath(username_input).send_keys("glendell03")
driver.find_element_by_xpath(password_input).send_keys("glendellbringino703")
driver.find_element_by_xpath(login_submit).click()
driver.find_element_by_xpath(new_repo).click()
driver.find_element_by_xpath(new_repo_name).send_keys(repository_name)
time.sleep(1)
driver.find_element_by_xpath(create_repo).click()


copy = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[1]/div/div/h1/strong/a').text
echo_readme = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]/span[1]').text
git_init = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]/span[2]').text
git_add = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]/span[3]').text
git_commit = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]/span[4]').text
git_remote = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]/span[5]').text
git_push = driver.find_element_by_xpath('//*[@id="empty-setup-new-repo-echo"]/span[6]').text
driver.close()


directory = f"/home/glendell03/{copy}"
cmd = f"cd {directory}"
try:
    os.mkdir(directory)
except OSError:
    print(f"{directory} is already exist")
    quit()
else:
    loading("\nCreating Repository Folder....")
    print(u"\u001b[32;1\nmSuccesfully created " + directory + u"\u001b[0m")

class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)
    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

with cd(directory):
    os.system(echo_readme)
    os.system(git_init)
    os.system(git_add)
    os.system(git_commit)
    os.system(git_remote)
    os.system(git_push)
    os.system(cmd)
    os.system('code .')



    





