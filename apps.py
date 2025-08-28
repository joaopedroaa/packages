system = {
    "system":                   ["tree", "words", "stow"],
    "book":                     ["calibre", "fbreader"],
    "color":                    ["python-pywal"],
    "wine":                     ["wine", "winetricks", "lutris"],
    "game":                     ["mcaselector"],
    "clock":                    ["ntp"],
    "keyboard ":                ["xkeycaps"],
    "cleaning":                 ["bleachbit"],
    "socialnetwork":            ["sherlock-git"],
    "screen":                   ["redshift", "caffeine-ng-git"],
    "bluetooth":                ["bluez", "bluez-libs", "bluez-utils", "blueberry"],
    "security":                 ["gnome-keyring"],
    "fontviewers":              ["font-manager"],
    "net":                      ["httpie"],
    "filesharing/ftp":          ["openssh"],

    # -----------------------------------------------------------------------------------#
    #                               Application
    # -----------------------------------------------------------------------------------#
    "apps/arch":                ["paru"],
    "apps/email":               ["mailspring"],
    "apps/password":            ["bitwarden"],

    "apps/network":             ["ipscan"],
    "apps/network/nmap":        ["nmap", "zenmap"],
    "apps/vulnerability":       ["lynis"],

    "apps/hamachi":             ["logmein-hamachi", "haguichi"],
    "apps/torrent":             ["qbittorrent", "stremio"],
    "apps/browsers":            ["firefox", "chromium", "i2p-bin"],

    "apps/messaging":           ["element-desktop"],
    "apps/messaging/discord":   ["discord_arch_electron", "betterdiscordctl-git"],

    "apps/spotify":             ["spotify", "zenity", "ffmpeg-compat-57"],
    "apps/spotify/spicetify":   ["spicetify-cli", "spicetify-themes-git"],

    # -----------------------------------------------------------------------------------#
    #                               Driver
    #
    # "driver/open":              ["xf86-video-nouveau",              # Driver
    #                              "mesa",                            # OpenGL
    #                              "lib32-mesa"],                     # OpenGL multilib
    #
    # "driver/nvidia390xx":       ["nvidia-390xx",                    # Driver
    #                              "nvidia-390xx-utils",              # OpenGL
    #                              "lib32-nvidia-390xx-utils",        # OpenGL multilib
    #                              "nvidia-390xx-settings"],
    # -----------------------------------------------------------------------------------#
    "driver":                   ["mesa-demos"],


    "driver/nvidia":            ["nvidia",                          # Driver
                                 "nvidia-utils",                    # OpenGL
                                 "lib32-nvidia-utils",              # OpenGL multilib
                                 "nvidia-settings"],


    "driver/nvidia-games":      ["dxvk-bin",
                                 "nvidia-dkms",
                                 "vulkan-icd-loader",
                                 "lib32-vulkan-icd-loader"],


   # -----------------------------------------------------------------------------------#
    #                               Hardware
    # -----------------------------------------------------------------------------------#
    "hardware/boot":            ["os-prober", "grub-customizer"],
    "hardware/boot/create":     ["etcher-bin", "woeusb"],

    "hardware/cpu":             ["cpu-x-git", "s-tui", "stress"],
    "hardware/gpu":             ["gwe"],
    "hardware/hd":              ["gparted-git", "gsmartcontrol", "gnome-disk-utility"],
    "hardware/hd/size":         ["ncdu", "dust", "agedu", "duf"],



    # -----------------------------------------------------------------------------------#
    #                               Audio
    # -----------------------------------------------------------------------------------#
    "audio/cli":                ["playerctl"],
    "audio/synthesis":          ["festival", "festival-us"],
    "audio/alsa":               ["alsa-firmware", "alsa-lib", "alsa-plugins", "alsa-utils"],
    "audio/pulseaudio":         ["pulseaudio", "pulseaudio-alsa", "pulseeffects-legacy", "pavucontrol"],


    # -----------------------------------------------------------------------------------#
    #                               Media
    # -----------------------------------------------------------------------------------#
    "media/image/viewers":      ["feh", "gwenview"],
    "media/image/editors":      ["krita", "inkscape"],
    "media/image/wallsetter":   ["nitrogen", "imagemagick"],
    "media/image/screenshot":   ["flameshot-git", "gcolor2", "scrot"],

    "media/video/players":      ["vlc", "mplayer", "obs-studio"],
    "media/video/edit":         ["video-trimmer"],

    "media/documents":          ["evince", "okular"],
    "media/documents/zathura":  ["zathura",
                                 "zathura-pdf-poppler",
                                 "zathura-djvu",
                                 "zathura-ps"],


    # -----------------------------------------------------------------------------------#
    #                               Terminal
    # -----------------------------------------------------------------------------------#
    "terminal/emulators":               ["alacritty-git", "kitty", "xcompmgr", "konsole", "yakuake"],
    "terminal/multiplexers":            ["tmux"],

    "terminal/shell/zsh":               ["zsh", "zinit"],
    "terminal/shell/zsh/config":        ["antigen-git", "lscolors-git"],

    "terminal/commandline":             ["xclip", "xsel", "iftop", "lsd"],
    "terminal/commandline/net":         ["httpstat-go"],
    "terminal/commandline/color":       ["bat", "most"],
    "terminal/commandline/finder":      ["fd", "fzf", "the_silver_searcher"],
    "terminal/commandline/taskmanager": ["gotop-bin", "htop", "tiptop-cli"],
    "terminal/commandline/sysinfo":     ["neofetch", "inxi", "tldr", "macchina"],
    "terminal/commandline/lazy":        ["lazygit", "lazydocker"],
    "terminal/commandline/fun":         ["cava", "cbonsai", "lolcat", "hollywood"],

    "terminal/commandline/git":         ["git-open-git", "git-delta"],
    "terminal/commandline/time":        ["calcurse"],
    "terminal/commandline/hexviewer":   ["hexyl"],

    "terminal/commandline/images":      ["pacgraph"],
    "terminal/commandline/video":       ["youtube-dl"],




    # -----------------------------------------------------------------------------------#
    #                               Files
    # -----------------------------------------------------------------------------------#
    "file/archivemanagers":             ["ark", "xarchiver"],
    "file/archivemanagers/console":     ["rar", "unrar", "zip", "unzip", "p7zip"],

    "filesystem":                       ["sshfs", "ntfs-3g"],
    "filesystem/mtp":                   ["mtpfs", "jmtpfs"],
    "filesystem/gvfs":                  ["gvfs", "gvfs-mtp", "gvfs-gphoto2"],

    "filemanager/console":              ["ranger", "nnn", "lf"],
    "filemanager/console/image":        ["w3m", "ueberzug"],

    "filemanager/graph":                ["pcmanfm"],
    "filemanager/graph/dolphin":        ["dolphin", "dolphin-plugins"],
    "filemanager/graph/thunar":         ["thunar", "thunar-archive-plugin", "thunar-volman"],
    "filemanager/graph/thunar/tumbler": ["tumbler", "ffmpegthumbnailer"],


    # -----------------------------------------------------------------------------------#
    #                               Fonts
    # -----------------------------------------------------------------------------------#
    "fonts/editor":             ["gucharmap"],
    # "fonts/nerd":               ["nerd-fonts-complete"],
    "fonts/misc!":              ["awesome-terminal-fonts"],
    "fonts/ttc!":               ["ttc-iosevka",
                                 "ttc-iosevka-ss15"],
    "fonts/ttf!":               ["ttf-fira-code",
                                 "ttf-material-design-icons-extended",
                                 "ttf-material-design-icons-git",
                                 "ttf-ibm-plex",
                                 "ttf-liberation",
                                 "ttf-roboto",
                                 "ttf-dejavu",
                                 "ttf-droid",
                                 "ttf-inconsolata",
                                 "ttf-liberation",
                                 "ttf-unifont",
                                 "ttf-ms-fonts",
                                 "ttf-liberation",
                                 "ttf-font-icons"],
    "fonts/emoji!":              ["noto-fonts-emoji"],

}

development = {
    "apps/cli":                 ["vsce", "exercism", "wakatime", "ngrok"],
    "apps/api":                 ["insomnia-bin", "postman-bin"],
    "apps/vm":                  ["docker"],
    "apps/virtualbox":          ["virtualbox", "virtualbox-host-dkms"],

    # "config/android":           ["android-sdk", "android-tools", "kdeconnect"],
    "config/archiso":           ["archiso-git", "qemu", "edk2-ovmf"],

    # -----------------------------------------------------------------------------------#
    #                               Development environments
    # -----------------------------------------------------------------------------------#
    "editors":                  ["visual-studio-code-insiders-bin",
                                 "visual-studio-code-bin",
                                 "neovim"],
    "editors/emacs":            ["emacs", "ripgrep"],

    # -----------------------------------------------------------------------------------#
    #                               Lang
    # -----------------------------------------------------------------------------------#
    # "lang/java":                ["jdk", "glassfish5", "processing"],
    # "lang/php":                ["apache", "mysql", "php", "php-apache", "phpmyadmin"],
    "lang/js":                  ["nvm-git", "yarn"],
    "lang/json":                ["jq"],
    "lang/shell":               ["shellcheck"],
    "lang/ocaml":               ["opam"],
    "lang/python":              ["python", "autopep8"],
    "lang/elixir":              ["elixir", "inotify-tools"],
    "lang/haskell":             ["ghc", "cabal-install", "stack"],
    "lang/lisp":                ["racket"],
    "lang/mark":                ["pandoc-bin"],
    "db/postgres":              ["postgresql", "pgadmin4-desktop"]

}



plasma = {
    "desktop":                  ["superpaper"],
    "desktop/taskbars":         ["plank"],
    # "desktop/kvantum":          ["kvantum-qt5-git"],
    # "desktop/kvantum/theme":    ["kvantum-theme-layan-git"], No AUR package found
}

xfce = {
    "xfce":                     ["xfce4-settings"],
    "compositor":               ["picom"],
    "applauncher":              ["dmenu", "rofi", "rofi-calc"],
    "desktop":                  ["lxappearance", "dunst-git"],

    # -----------------------------------------------------------------------------------#
    #                               Display manager
    # -----------------------------------------------------------------------------------#
    "dm/xorg!":                 ["xorg", "xorg-xinit-git"],
    "dm/lightdm":               ["lightdm",
                                 "lightdm-gtk-greeter",
                                 "lightdm-gtk-greeter-settings",
                                 "lightdm-webkit2-greeter"],


    # -----------------------------------------------------------------------------------#
    #                               Themes
    # -----------------------------------------------------------------------------------#
    "themes/icons!":            ["tela-icon-theme-git", "flatery-icon-theme-git"],
    "themes/cursors!":          ["capitaine-cursors"],
    "themes/colors!":           ["chicago95-gtk-theme-git",
                                 "gruvbox-material-gtk-theme-git",
                                 "yaru-gtk-theme",
                                 "materia-gtk-theme"],


    # -----------------------------------------------------------------------------------#
    #                               i3
    # -----------------------------------------------------------------------------------#
    "wm":                       ["wmctrl"],
    "i3":                       ["i3-gaps", "autotiling", "perl-anyevent-i3"],
    "i3/lock":                  ["i3lock"],
    "i3/bar":                   ["i3blocks", "py3status", "polybar"],


    # -----------------------------------------------------------------------------------#
    #                               xmonad
    # -----------------------------------------------------------------------------------#
    "xmonad":                   ["xmonad", "xmonad-contrib", "xmonad-utils", "xmonad-log"],
    "xmonad/haskell":           ["haskell-dbus"],
    "xmonad/bar":               ["xmobar"]
}
