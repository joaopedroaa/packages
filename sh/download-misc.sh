source ~/dotfiles/.scripts/separate_echo.sh


separate_echo "ZSH / ohmyzsh"
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

separate_echo "ZSH / zinit"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma/zinit/master/doc/install.sh)"

separate_echo "ZSH / Antigen"
curl -L git.io/antigen > ~/antigen.zsh

separate_echo "asdf"
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.8.0

separate_echo "Kitty theme install" # https://github.com/connorholyday/kitty-snazzy
curl -o ~/.config/kitty/ktheme.conf https://raw.githubusercontent.com/connorholyday/kitty-snazzy/master/snazzy.conf

separate_echo "Install Phoenix"
mix archive.install hex phx_new


#-----------------------------------------------------------------------#

separate_echo "Cabal update"
cabal update


separate_echo "Yarn install"
yarn global add gatsby-cli
yarn global add bs-platform
yarn global add typescript
yarn global add neovim


separate_echo "pip3"
pip3 install --user flake8
pip3 install --user yapf
pip3 install --user neovim

pip3 install --user google-api-python-client
pip3 install --user httplib2
