enable_systemctl () {
  clear
  echo "========================================  $1  ========================================"
  sudo systemctl enable $1
  sudo systemctl restart $1
  sudo systemctl status $1
}

import_gpt (){
  gpg --keyserver pool.sks-keyservers.net --recv-keys $1
}


source ~/dotfiles/.scripts/separate_echo.sh
# ----------------------------------------------------------------------------------------- #

separate_echo "GPT keys"
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | gpg --import -
import_gpt 931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90 # Spotify Public Repository
import_gpt 2EBF997C15BDA244B6EBF5D84773BD5E130D1D45
import_gpt 8FD3D9A8D3800305A9FFF259D1742AD60D811D58
import_gpt EF6E286DDA85EA2A4BA7DE684E2C6E8793298290 # Tor
import_gpt 14F26682D0916CDD81E37B6D61B7B526D98F0353 # Firefox


separate_echo "Systemctl"
enable_systemctl docker
enable_systemctl httpd
enable_systemctl mysqld
enable_systemctl postgresql


separate_echo "Docker"
sudo chmod 666 /var/run/docker.sock
sudo usermod -aG docker joaopedro


separate_echo "Spotify / Spicetify" # https://github.com/khanhas/spicetify-cli/wiki/Basic-Usage
sudo chmod a+wr /opt/spotify
sudo chmod a+wr /opt/spotify/Apps -R
# spicetify config current_theme Bittersweet ; spicetify apply


separate_echo "MariaDB"
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql


separate_echo "Postgres"
sudo mkdir /var/lib/postgres
sudo chmod 775 /var/lib/postgres
sudo chown postgres /var/lib/postgres





# ----------------------------------------------------------------------------------------- #
# separate_echo "Fix netbeans 8 font"
# echo "netbeans_default_options=\"-J-client -J-Xss2m -J-Xms32m -J-XX:PermSize=32m -J-Dapple.laf.useScreenMenuBar=true -J-Dapple.awt.graphics.UseQuartz=true -J-Dsun.java2d.noddraw=true -J-Dsun.java2d.dpiaware=true -J-Dsun.zip.disableMemoryMapping=true -J-Dswing.aatext=true -J-Dawt.useSystemAAFontSettings=on\"" >> /usr/share/netbeans/etc/netbeans.conf


# separate_echo "populate archlinux"
# sudo pacman-key --populate archlinux
