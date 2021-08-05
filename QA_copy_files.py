#!/usr/bin/env python3
"""Implement a program that copies files in accordance with the configuration file."""
import shutil as sh
import xml.etree.ElementTree as ET
import os

Config_file = "config.xml"

def copy_config_xml(file:str):

    #Checking whether the XML file is
    if file[-4:].lower() != ".xml":
        print('Check the file extension.\nThe program supports only "xml" format files"')
        return

    #Getting data from a file to copy
    root = ET.parse(Config_file).getroot() 
    for tag in root.findall('file'):
        try:
            value_source_path = tag.get('source_path') 
            value_file_name = tag.get('file_name') 
            target_path = os.path.join(value_source_path, value_file_name)
            value_destination_path = tag.get('destination_path')
            if not os.path.exists(value_destination_path):
                os.makedirs(value_destination_path) 
            sh.copy(target_path, value_destination_path)
        except PermissionError:
            print("'{}' Access denied, run the application as an administrator".format(value_destination_path))
            continue
        except FileNotFoundError:
            print('The path {} is not exist.'.format(target_path))
            continue

if __name__ == "__main__":
    copy_config_xml(Config_file)

