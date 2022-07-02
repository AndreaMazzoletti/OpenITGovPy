import sys
import requests
import json
import os

data_dir = "./data"

def print_greetings():
    print("##################################################################\n### Welcome to OpenITGovPy, enjoy italian government open data ### \n##################################################################")
    print("Created for the v3 API, for reference see https://www.dati.gov.it/api\n")
    return

def quit():
    print("Quitting...")
    exit()
    return

def convert_bytes_to_json(my_bytes):
    return json.loads(my_bytes.decode(encoding='UTF-8'))

def get_selected_objects_from_input(keyword):
    response = requests.get("https://www.dati.gov.it/opendata/api/3/action/package_list")
    tmp_list = convert_bytes_to_json(response.content)
    return list(filter(lambda x: keyword in x ,tmp_list["result"]))


def get_id_dowload_links(ids):
    ids_infos = []
    print("Getting download links, this might take a while...")
    for _id in ids:
        response = requests.get("https://www.dati.gov.it/opendata/api/3/action/package_show?id=" + _id)
        converted_object = convert_bytes_to_json(response.content)
        try:
            # TODO: save as file.format
            ids_infos.append({
                "download_link": converted_object["result"]["url"],
                "name": converted_object["result"]["name"] + "-" +  converted_object["result"]["id"] 
            })
        except KeyError:
            print("Error while downloading " + converted_object["result"]["url"])
    return ids_infos

def create_download_directory_if_not_exists(name):
    if not os.path.exists(name):
        print("Data directory not found, creating one in the current folder...")
        os.makedirs(name)
        print("Done")
    else: 
        print("Found data directory")

def dowload_data_to_disk(download_links):
    print("Downloading data...")
    for download_link in download_links:
        try:
            response = requests.get(download_link["download_link"], stream=True)
            if response.ok:
                print("Downloading " + download_link["name"] + " to " + data_dir, os.path.abspath(data_dir) + "...")
                with open(data_dir + "/" + download_link["name"], 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024 * 8):
                        if chunk:
                            f.write(chunk)
                            f.flush()
                            os.fsync(f.fileno())
                print("Done!")
            else:
                print("Download failed for file " + download_link["name"])
        except:
            print("Error during download, probably it's due the download link absence (naughty open data mantainer)")
    print("All available files were downloaded\n")
    return 


def prompt():
    print('Enter the keyword to search (blank for the entire database): ')
    keyword = input()
    items_to_download_info = get_selected_objects_from_input(keyword)
  
    if(len(items_to_download_info) <= 0):
        print("No items were found, do you want to search for another keyword?[Y/n]")
        answer = input()
        if(answer.lower() != "y"):
            quit()
        else:
            prompt()
    print(str(len(items_to_download_info)) + " entries were found, do you want to download them?[Y/n]",  )
    answer = input()
    if(answer.lower() != "y"):
        quit()
    print("Preparing the downloads, hold on...")
    download_links = get_id_dowload_links(items_to_download_info)
    print("Preparing directories for the download")
    create_download_directory_if_not_exists(data_dir)
    dowload_data_to_disk(download_links)
    print("End of program workflow, do you want to search for another keyword?[Y/n]")
    answer = input()
    if(answer.lower() != "y"):
        quit()
    else:
        prompt()

def main():
    print_greetings()
    prompt()

main()