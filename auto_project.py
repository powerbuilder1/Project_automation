from github import Github
import sys
from dotenv import load_dotenv
import os
import subprocess
import pyautogui
import time

load_dotenv()
path = os.getenv("PATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create_repo():
    # get args
    args = sys.argv
    # get new repo name form args
    repo_name = args[1]
    # create Main Class obj
    g = Github(username, password)
    # create Auth User obj
    user = g.get_user()
    # create new repo
    new_repo = user.create_repo(name=repo_name, private=True, auto_init=True)
    # get clone url
    clone_url = new_repo.clone_url

def open_git_kraken():
    # bash command to start gitkraken
    command = "/usr/share/gitkraken/gitkraken %U"
    # open a new terminal window
    pyautogui.hotkey('ctrl', 'shift', 'n')
    # wait until terminal window is open
    time.sleep(2)
    # list of letters in command
    all_letters = []
    for letter in command:
        # avoid getting 7 instead of /
        if letter == '/':
            all_letters.append('divide')
        else:
            all_letters.append(letter)
    # add letter to submit command
    all_letters.append("enter")
    # write command in new terminal
    pyautogui.typewrite(all_letters)

def create():
    # create new repo
    create_repo()
    # open git-kraken
    open_git_kraken()




if __name__ == "__main__":
    open_git_kraken()
    # create()
