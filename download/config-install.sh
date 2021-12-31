source ~/dotfiles/.scripts/system.sh

echo_separate "locale"
sudo locale-gen


echo_separate "timedatectl"
# timedatectl set-timezone "$(curl --fail https://ipapi.co/timezone)"
timedatectl set-timezone America/Sao_Paulo
