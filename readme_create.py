import subprocess
from apps import *


def save_file(filename, info):
    with open(f"./{filename}", 'w') as file:
        file.write(info)


def save_readme(info):
    save_file("README.md", info)


def get_yay_info(appname):
    package_info = {}
    yay_output = str(subprocess.check_output(
        f"yay -Sii {appname}", shell=True))[2:]

    print(f"Getting {appname}")
    splited = yay_output.split("\\n")

    for lines in splited:
        line = lines.split(" : ")
        line[0] = line[0].strip()

        if(line[0] == "Repository"):
            package_info["repository"] = line[1]

        if(line[0] == "Name"):
            package_info["name"] = line[1]

        if(line[0] == "Description"):
            package_info["description"] = line[1]

        if(line[0] == "Architecture"):
            package_info["architecture"] = line[1]

        if(line[0] == "URL"):
            package_info["url"] = line[1]

        if(line[0] == "Installed Size"):
            package_info["installed"] = line[1]

    return package_info


def save_packages(README_DATA, dic):
    packages_infos = []
    total_size = 0

    for categories, apps in dic.items():
        if (categories[-1] != "!"):
            for app in apps:
                yayinfo = get_yay_info(app)
                packages_infos.append(yayinfo)
                # print(packages_infos)
    return packages_infos


def form_aur(README_DATA, dic):
    packages_infos = save_packages(README_DATA, dic)
    total_size = 0

    for line in packages_infos:
        name = line['name']
        url = line['url']

        description = line['description']
        repository = line['repository']

        if (repository == "aur"):
            aur_link = f"https://aur.archlinux.org/packages/{name}"
        else:
            architecture = line['architecture']
            aur_link = f"https://archlinux.org/packages/{repository}/{architecture}/{name}"

        README_DATA += f"| [{name}]({url}) | {description} | [{repository}]({aur_link}) |\n"

    print("-- ok")
    return README_DATA


readmeData = open(f"./READMET.md", 'r').read()
readmeData += f"\n| Name | Description | Repository |"
readmeData += f"\n| :--- | :---------- | :--------- |\n"


def main():
    save_readme(form_aur(form_aur(form_aur(
        form_aur(readmeData, system), development), plasma), xfce))


main()


# save_readme(form_aur(readmeData, plasma))
# get_yay_info("qbittorrent")
