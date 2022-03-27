#!/bin/bash
#

DIR=`pwd`
FDIR="$HOME/.local/share/fonts"
PDIR="$HOME/.config/polybar"

cp -rf .config ~
cp .xbindkeysrc ~
cp .zshrc ~


mkdir ly_install
cd ly_install
git clone --recurse-submodules https://github.com/nullgemm/ly.git
cd ly
make
sudo make install
sudo systemctl enable ly.service


clear
#cat <<- EOF
#[*] Installing packages...
#[1] Install reqired
#[2] Intall all(PyCharm, OnlyOffice)

#EOF 
paru -S qtile xbindkeys rofi 1nitrogen pcmanfm neovim xorg alacritty firefox ttf-spacemono ttf-font-awesome python-pip ttf-icomoon-feather
pip install neovim 
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

#installing fonts
echo -e "\n[*] Installing fonts..."
if [[ -d "$FDIR" ]]; then
	cp -rf $DIR/fonts/* "$FDIR"
else
	mkdir -p "$FDIR"
	cp -rf $DIR/fonts/* "$FDIR"
fi
