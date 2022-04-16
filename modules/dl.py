import requests


def download(links: dict, path: str, architecture: str):
    for name in list(links):
        if architecture in name or 'neutral' in name:
            if 'msixbundle' not in name:
                print(f"Downloading {name}")
                with open(path + '\\' + name, 'wb') as f:
                    f.write(requests.get(links[name]).content)

    bundles = dict()
    for name in list(links):
        if 'msixbundle' in name and 'emsixbundle' not in name:
            bundles[name.split('_')[1]] = [links[name], name]

    print("Found versions of app:")
    for name in list(bundles):
        print(name)

    version = input("Which version do you want to download? \nType here: ")

    with open(path + '\\' + bundles[version][1], 'wb') as f:
        print(f"Downloading {bundles[version][1]}")
        f.write(requests.get(bundles[version][0]).content)

    print("DOWNLOAD COMPLETE")
