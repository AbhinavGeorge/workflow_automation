import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import info
#create a file called info.py and add username and password as variables in it

import time

projectName = input("Enter the name of the project:")
initialization = input("do you want to initialize repo with python(p) or node(j)[leave blank for no]:")

#needed things
webDriver = webdriver.Chrome()
webDriver.get("https://github.com/login")

#loging in
webDriver.find_element_by_xpath('//*[@id="login_field"]').send_keys(info.username)
webDriver.find_element_by_name('password').send_keys(info.password)
webDriver.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]').click()

#creating a new repo
newRepo = webDriver.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
webDriver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(projectName)
time.sleep(2)
webDriver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()
webDriver.quit()

#creating a local directory
os.system("mkdir ~/code/" + projectName)

#github stuff
os.system("git init ~/code/"+ projectName)
os.system("touch ~/code/" + projectName + "/README.md")

#github functions

def gitHub():
    os.chdir("/home/anonymous/code/"+projectName)

def addingFiles():
    os.system("git add .")
    os.system('git commit -m "first commit"')
    os.system("git branch -M main")
    os.system("git remote add origin https://github.com/AbhinavGeorge/"+projectName+".git")
    os.system("git push -u origin main")

#setting up language

#python
if initialization == "p":
    gitHub()
    os.system("touch ~/code/"+projectName+"/main.py")
    addingFiles()
    
#nodejs with express
elif initialization == "j":
    gitHub()
    os.system("touch app.js")
    os.system("npm init -y")
    os.system("npm install express")
    addingFiles()

#no language
else:
    gitHub()
    addingFiles()
