#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

# move into the working directory
file_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(file_directory)

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")

