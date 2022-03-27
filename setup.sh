#!/bin/bash
#

DIR=`pwd`
FDIR="$HOME/.local/share/fonts"

#Installing login manager(Ly)
mkdir ly_install
cd ly_install
git clone --recurse-submodules https://github.com/nullgemm/ly.git
cd ly
make
sudo make install
sudo systemctl enable ly.service

#installing packages
paru -S qtile xbindkeys rofi nitrogen pcmanfm neovim xorg alacritty firefox ttf-spacemono python-pip zsh starship
pip install neovim 
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
chsh -s /bin/zsh

#installing fonts
echo -e "\n[*] Installing fonts..."
if [[ -d "$FDIR" ]]; then
	cp -rf $DIR/fonts/* "$FDIR"
else
	mkdir -p "$FDIR"
	cp -rf $DIR/fonts/* "$FDIR"
fi

#Copying config files
cp -rf .config ~
cp .xbindkeysrc ~
cp .zshrc ~
