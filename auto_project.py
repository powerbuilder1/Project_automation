from github import Github
import sys
from dotenv import load_dotenv
import os
import subprocess
import pyautogui
import time

load_dotenv()
project_path = os.getenv("PROJECT_PATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# get args
args = sys.argv
# get new repo name form args
repo_name = args[1]

def create_repo():
    # create Main Class obj
    g = Github(username, password)
    # create Auth User obj
    user = g.get_user()
    # create new repo
    new_repo = user.create_repo(name=repo_name, private=True, auto_init=True)
    # get clone url
    clone_url = new_repo.clone_url
    return clone_url

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

def set_size_and_pos(width, height, x, y):
    # get window id
    command = "xdotool search --onlyvisible --name gitkraken"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = proc.communicate()
    # get list of all window_ids
    window_ids = str(stdout, "utf8").split("\n")[:-1]
    # set focus window
    if len(window_ids) == 0:
        print("[ERROR] No window found!")
    command = f"xdotool windowsize {width} {height} {window_ids[0]}"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = proc.communicate()
    command = f"xdotool windowmove {window_ids[0]} {x}, {y}"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout, stderr) = proc.communicate()


def clone_repo_git_kraken(clone_url):
    # hotkey for git clone
    pyautogui.hotkey('ctrl', 'n')

    #

    # list of letters in command
    all_letters = []
    print(project_path)
    for letter in project_path:
        # avoid getting 7 instead of /
        if letter == '/':
            all_letters.append('divide')
        else:
            all_letters.append(letter)
    # set/ write project path
    pyautogui.typewrite(all_letters)

    # tab to url
    pyautogui.press('tab', presses=2)

    all_letters = []
    print(clone_url)
    for letter in clone_url:
        # avoid getting 7 instead of /
        if letter == '/':
            all_letters.append('divide')
        else:
            all_letters.append(letter)
    # set/ write clone url
    pyautogui.typewrite(all_letters)

    # tab to Full path input field
    pyautogui.press('tab')

    # set/ write repo name
    pyautogui.typewrite(repo_name)

    # submit
    pyautogui.press('enter')

    # wait until popup
    time.sleep(2)

    # tab to open
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    # final submit
    pyautogui.press('enter')


def create():
    # create new repo
    url = create_repo()
    # open git-kraken
    open_git_kraken()
    # wait until git kraken is open
    time.sleep(8)
    # clone repo
    clone_repo_git_kraken(url)


    # # terminal with project path
    # pyautogui.hotkey('ctrl', 'shift', 'n')
    #
    # command = f"cd ~/Dokumente/Projekte/Project_automation/{repo_name}/"
    # # list of letters in command
    # all_letters = []
    # for letter in command:
    #     # avoid getting 7 instead of /
    #     if letter == '/':
    #         all_letters.append('divide')
    #     else:
    #         all_letters.append(letter)
    # # add letter to submit command
    # all_letters.append("enter")
    # # write command in new terminal
    # pyautogui.typewrite(all_letters)




if __name__ == "__main__":
    # create()

    set_size_and_pos(800, 800, 0, 0)
