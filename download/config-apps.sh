source ~/dotfiles/.scripts/system.sh


echo_separate "Docker"
sudo chmod 666 /var/run/docker.sock
sudo usermod -aG docker joaopedro


echo_separate "Spotify / Spicetify" # https://github.com/khanhas/spicetify-cli/wiki/Basic-Usage
sudo chmod a+wr /opt/spotify
sudo chmod a+wr /opt/spotify/Apps -R
# spicetify config current_theme Bittersweet ; spicetify apply


echo_separate "MariaDB"
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql


echo_separate "Postgres"
sudo mkdir /var/lib/postgres
sudo chmod 775 /var/lib/postgres
sudo chown postgres /var/lib/postgres


# echo_separate "Reflector"
# reflector


# ----------------------------------------------------------------------------------------- #
# echo_separate "Fix netbeans 8 font"
# echo "netbeans_default_options=\"-J-client -J-Xss2m -J-Xms32m -J-XX:PermSize=32m -J-Dapple.laf.useScreenMenuBar=true -J-Dapple.awt.graphics.UseQuartz=true -J-Dsun.java2d.noddraw=true -J-Dsun.java2d.dpiaware=true -J-Dsun.zip.disableMemoryMapping=true -J-Dswing.aatext=true -J-Dawt.useSystemAAFontSettings=on\"" >> /usr/share/netbeans/etc/netbeans.conf


# echo_separate "populate archlinux"
# sudo pacman-key --populate archlinux
