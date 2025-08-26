

systemctl_enable () {
  clear
  echo "========================================  $1  ========================================"
  sudo systemctl enable $1
  sudo systemctl restart $1
  sudo systemctl status $1
}

# ----------------------------------------------------------------------------------------- #


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
# setup_dxvk install
