import requests
def get_image_urls(url, items=[]):
    params = {"fo": "json", "c": 100, "at": "results,pagination"}
    call = requests.get(url, params=params)
    data = call.json()
    results = data['results']
    for result in results:
        if "collection" not in result.get("original_format") and "webpage" not in result.get("original_format"):
            if result.get("image_url"):
                item = result.get("image_url")[-1]
                items.append(item)
        if data["pagination"]["next"] is not None:
            next_url = data["pagination"]["next"]
            print("getting next page: {0}".format(next_url))
            get_image_urls(next_url, items)
        return items

image_urls = get_image_urls("https://www.loc.gov/collections/slave-narratives-from-the-federal-writers-project-1936-to-1938/", items=[])
len(image_urls)
image_urls[:5]
import json
r = requests.get("https://www.loc.gov/item/98513999/?fo=json")
r_data = r.json()
print(json.dumps(r_data["item"]["rights_information"], indent=2))
print(json.dumps(r_data["item"]["rights_advisory"], indent=2))
print(json.dumps(r_data["item"]["rights"], indent=2))
print(json.dumps(r_data["item"]["restriction"], indent=2))
import os
def get_image_files(image_urls_list, path):
    for count, url in enumerate(image_urls_list):
        if count % 100 == 0:
            print("at item {0}",format(count))
        try:
            filename = url.split('/')[-1]
            filename = os.path.join(path, filename)
            full_url = "https:{0}".format(url)
            image_response = requests.get(full_url, stream=True)
            with open(filename, 'wb') as fd:
                for chunk in image_response.iter_content(chunk_size=100000):
                    fd.write(chunk)
        except ConnectionError as e:
            print(e)
get_image_files(image_urls, "images")
from urllib.parse import urlparse
def get_and_save_images(results_url, path):
    params = {"fo": "json", "c": 100, "at": "results,pagination"}
    call = requests.get(results_url, params=params)
    data = call.json()
    results = data['results']
    for result in results:
        if "collection" not in result.get("original_format") and "webpage" not in result.get("original_format"):
            if result.get("image_url"):
                image = "https:" + result.get("image_url")[-1]
                identifier = urlparse(result["id"])[2].rstrip('/')
                identifier = identifier.split('/')[-1]
                filename = "{0}.jpg".format(identifier)
                filename = os.path.join(path, filename)
                image_response = requests.get(image, stream=True)
                with open(filename, 'wb') as fd:
                    for chunk in image_response.iter_content(chunk_size=100000):
                        fd.write(chunk)
    if data["pagination"]["next"] is not None:
        next_url = data["pagination"]["next"]
        print("getting next page: {0}".format(next_url))
        get_and_save_images(next_url, path)
get_and_save_images("https://www.loc.gov/collections/slave-narratives-from-the-federal-writers-project-1936-to-1938/","images_named")
