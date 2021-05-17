import subprocess
from apps import *

def save_readme(info):
    with open(f"./README.md", 'w') as file:
        file.write(info)


def get_yay_info(appname):
    infos = {}
    yay_output = str(subprocess.check_output(
        f"yay -Sii {appname}", shell=True))[2:]

    splited = yay_output.split("\\n")

    for lines in splited:
        line = lines.split(" : ")
        line[0] = line[0].strip()

        if(line[0] == "Repository"):
            infos["repository"] = line[1]

        if(line[0] == "Name"):
            infos["name"] = line[1]

        if(line[0] == "Description"):
            infos["description"] = line[1]

        if(line[0] == "Architecture"):
            infos["architecture"] = line[1]

        if(line[0] == "URL"):
            infos["url"] = line[1]

    return infos


def form_aur(README_DATA, dic):
    readme_data_json = []
    for categories, apps in dic.items():
        if (categories[-1] == "!"):
            for app in apps:
                yayinfo = get_yay_info(app)
                yayinfo["categoriesName"] = categories
                readme_data_json.append(yayinfo)

    for line in readme_data_json:
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

readmeData = ""
readmeData += f"\n"
readmeData += f"| Name | Description | Repository |\n"
readmeData += f"| :--- | :---------- | :--------- |\n"

def main():
    # get_yay_info("qbittorrent")
    # get_yay_info("paru")
    # get_yay_info("mailspring")

    # final_readme_data = form_aur(readmeData, apps)
    final_readme_data = form_aur(form_aur(form_aur(form_aur(form_aur(
        form_aur(readmeData, apps), development), plasma), xfce), i3), xmonad)

    save_readme(final_readme_data)


main()
