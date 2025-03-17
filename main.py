import main_utils
import git_utils

# Firefox
print("Downloading Firefox...")
url = "https://mozilla-firefox.en.uptodown.com/windows/download"
main_utils.download(url)
print()

# Git
print("Downloading Git...")
url = "https://git-for-windows.en.uptodown.com/windows/download"
main_utils.download(url)
print()

# VS Code
print("Downloading VS Code...")
url = "https://visual-studio-code.en.uptodown.com/windows/download"
main_utils.download(url)
print()

# NVIDIA App
print("Downloading NVIDIA App...")
url = "https://nvidia-app.en.uptodown.com/windows/download"
main_utils.download(url)
print()

# WinRAR
print("Downloading WinRAR...")
url = "https://winrar.en.uptodown.com/windows/download"
main_utils.download(url)
print()

# KMPlayer 64X
print("Downloading KMPlayer...")
url = "https://kmplayer-64x.en.uptodown.com/windows/download"
main_utils.download(url)
print()

# Predator Sense
print("Downloading Predator Sense...")
url = "https://global-download.acer.com/GDFiles/Application/Predator%20Sense/Predator%20Sense_Acer_3.00.3136_W10x64_A.zip?acerid=637295963588423777&Step1=&Step2=&Step3=PREDATOR%20PH315-52&OS=ALL&LC=en&BC=ACER&SC=PA_6"
main_utils.download_file(url, "PredatorSense.zip")
print()

# Traffic Monitor
print("Downloading Traffic Monitor...")
url = "https://github.com/zhongyang219/TrafficMonitor"
git_utils.get_latest_release(url, True)
print()