from apps import *


def save_files(DATA, writeLocation):
    for category in DATA:
        with open(f"{writeLocation}/{category}.sh", 'w') as file:
            file.write(DATA[category][0])


def create_lines(DATA, index, dic):
    index_name = base_list[index]
    app_name = DATA[index_name][1]
    start_line = DATA[index_name][2]

    for categories, apps in dic.items():
        join_apps, title, count = "", "", 0

        for app in apps:
            join_apps += f"{app} "
            count += 1

        for word in categories.split("/"):
            title += f" {word.capitalize()} /"

        DATA[index_name][0] += f"echo \"{'=' * 30} {app_name} / {title[1:-1]}({count}) {'=' * 21}\"\n"
        DATA[index_name][0] += f"{start_line} {join_apps}--noconfirm\n"
        DATA[index_name][0] += f"clear\n\n"


base = {
    # filename           Name         Install Command
    "10-system":    ["", "System",    "yay -S"],
    "20-dev":       ["", "Dev",       "yay -S"],
    "30-plasma":    ["", "Plasma",    "yay -S"],
    "40-xfce":      ["", "xfce",      "yay -S"],
}

base_list = list(base)


def main():
    create_lines(base, 0, system)
    create_lines(base, 1, development)
    create_lines(base, 2, plasma)
    create_lines(base, 3, xfce)
    save_files(base, "./build")


main()
