source ~/dotfiles/.scripts/system.sh


echo_separate "ZSH / ohmyzsh"
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


echo_separate "ZSH / zinit"
bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/zdharma-continuum/zinit/HEAD/scripts/install.sh)"

echo_separate "ZSH / Antigen"
curl -L git.io/antigen > ~/antigen.zsh


echo_separate "asdf"
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.8.1


echo_separate "Doom Emacs"
git clone --depth 1 https://github.com/hlissner/doom-emacs ~/.emacs.d
~/.emacs.d/bin/doom install


echo_separate "Kitty theme install" # https://github.com/connorholyday/kitty-snazzy
curl -o ~/.config/kitty/ktheme.conf https://raw.githubusercontent.com/connorholyday/kitty-snazzy/master/snazzy.conf


echo_separate "Cabal update"
cabal update


echo_separate "Mix"
mix archive.install hex phx_new


echo_separate "Docker image"
sudo docker pull dpage/pgadmin4


echo_separate "Yarn install"
yarn global add gatsby-cli
yarn global add bs-platform
yarn global add typescript
yarn global add neovim


echo_separate "pip3"
pip3 install --user flake8
pip3 install --user yapf
pip3 install --user neovim
pip3 install --user google-api-python-client
pip3 install --user httplib2


echo_separate "Spotify"
cd ~/.cache && git clone https://github.com/abba23/spotify-adblock.git && cd spotify-adblock
sudo make && sudo make install



echo_separate "Wine Dependencies"
sudo pacman -S --needed wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses opencl-icd-loader lib32-opencl-icd-loader libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader

# echo_separate "asdf"
# asdf plugin add erlang
# asdf plugin add elixir

# asdf install erlang 24.0
# asdf install elixir master

# asdf global erlang  24.0
# asdf global elixir  master

# asdf current
