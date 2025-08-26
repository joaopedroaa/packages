#!/bin/bash

# Imprime um cabeçalho de seção formatado para melhor visualização.
echo_separate() {
    echo ""
    echo "################################################################################"
    echo "## $1"
    echo "################################################################################"
}

# Habilita, reinicia e verifica o status de um serviço systemd.
# USO: systemctl_enable <nome_do_servico>
systemctl_enable() {
    echo "--- Configurando Serviço: $1 ---"
    sudo systemctl enable "$1"
    sudo systemctl restart "$1"
    sudo systemctl status "$1"
}


# ============================================================================== #
# ==                         CONFIGURAÇÃO DO SISTEMA                            == #
# ============================================================================== #

echo_separate "Configuração de Localização (Locale)"
sudo locale-gen # Gera os locales definidos em /etc/locale.gen

echo_separate "Configuração de Fuso Horário"
sudo timedatectl set-timezone America/Sao_Paulo # timedatectl set-timezone "$(curl --fail https://ipapi.co/timezone)"

# ============================================================================== #
# ==                         GERENCIAMENTO DE SERVIÇOS                          == #
# ============================================================================== #

echo_separate "Habilitando e Iniciando Serviços (Systemd)"

systemctl_enable systemd-timesyncd
systemctl_enable docker
systemctl_enable httpd
systemctl_enable mysqld
systemctl_enable postgresql
systemctl_enable logmein-hamachi


# ============================================================================== #
# ==                  CONFIGURAÇÃO DE APLICAÇÕES E PERMISSÕES                   == #
# ============================================================================== #

echo_separate "Configuração do Docker"
sudo usermod -aG docker "$USER"
sudo chmod 666 /var/run/docker.sock


echo_separate "Configuração do Spotify / Spicetify"
# Para mais informações: https://github.com/khanhas/spicetify-cli/wiki/Basic-Usage
sudo chmod a+wr /opt/spotify
sudo chmod a+wr /opt/spotify/Apps -R
# Exemplo de uso do Spicetify:
# spicetify config current_theme Bittersweet ; spicetify apply


echo_separate "Setup Inicial do MariaDB"
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql


echo_separate "Setup Inicial do PostgreSQL"
sudo mkdir -p /var/lib/postgres/data
sudo chown -R postgres:postgres /var/lib/postgres
sudo chmod -R 700 /var/lib/postgres/data # 700 é mais seguro para o diretório de dados


# ============================================================================== #
# ==               TAREFAS OPCIONAIS                                           == #
# ============================================================================== #

# --- Habilitar DXVK em um Wineprefix ---
# echo_separate "Instalando DXVK"
# setup_dxvk install

# --- Atualizar lista de espelhos do Arch Linux ---
# echo_separate "Atualizando lista de espelhos (Reflector)"
# sudo reflector --verbose --country 'Brazil' -l 10 --sort rate --save /etc/pacman.d/mirrorlist

# --- Popular chaves do Arch Linux ---
# echo_separate "Populando chaves do Arch Linux (pacman-key)"
# sudo pacman-key --populate archlinux


echo ""
echo "================================================================================"
echo "==                   Script de configuração finalizado.                       =="
echo "================================================================================"
