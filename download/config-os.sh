source ~/dotfiles/.scripts/system.sh

systemctl_enable () {
  clear
  echo "========================================  $1  ========================================"
  sudo systemctl enable $1
  sudo systemctl restart $1
  sudo systemctl status $1
}

gpt_import (){
  gpg --keyserver pool.sks-keyservers.net --recv-keys $1
}

# ----------------------------------------------------------------------------------------- #

echo_separate "GPT keys"
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | gpg --import -
gpt_import EF6E286DDA85EA2A4BA7DE684E2C6E8793298290 # Tor
gpt_import 14F26682D0916CDD81E37B6D61B7B526D98F0353 # Firefox


echo_separate "Systemctl"
systemctl_enable systemd-timesyncd
systemctl_enable docker
systemctl_enable httpd
systemctl_enable mysqld
systemctl_enable postgresql
systemctl_enable logmein-hamachi


echo_separate "locale"
sudo locale-gen


echo_separate "timedatectl"
# timedatectl set-timezone "$(curl --fail https://ipapi.co/timezone)"
timedatectl set-timezone America/Sao_Paulo


# enable DXVK in a wineprefix
setup_dxvk install
