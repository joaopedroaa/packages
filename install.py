from apps import *


def save_files(DATA):
    for category in DATA:
        with open(f"./sh/install/{category}.sh", 'w') as file:
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
    "10-apps":      ["", "Apps",      "yay -S"],
    "11-apps_dev":  ["", "Apps Dev",  "yay -S"],
    "20-de_plasma": ["", "Plasma",    "yay -S"],
    "21-de_xfce":   ["", "xfce",      "yay -S"],
    "30-wm_i3":     ["", "I3",        "yay -S"],
    "31-wm_xmonad": ["", "Xmonad",    "yay -S"],
}

base_list = list(base)


def main():
    create_lines(base, 0, apps)
    create_lines(base, 1, development)
    create_lines(base, 2, plasma)
    create_lines(base, 3, xfce)
    create_lines(base, 4, i3)
    create_lines(base, 5, xmonad)
    save_files(base)


main()
