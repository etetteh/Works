""" Rename files by removing numeric characters"""
import os

def rename_files():
    list_files = os.listdir("/home/enock/Documents/kernel_project/images")
    print(list_files)
    
    # rename files
    os.rename_files(list_files, list_files.translate(None, '0123456789'))