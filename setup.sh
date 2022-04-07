#!/bin/bash
#
DIR=`pwd`
FDIR="$HOME/.local/share/fonts"

echo "Installing login manager(Ly)"
mkdir ly_install
cd ly_install
git clone --recurse-submodules https://github.com/nullgemm/ly.git
cd ly
make
sudo make install
sudo systemctl enable ly.service

echo "installing packages"
paru -S qtile polybar rofi nitrogen pcmanfm neovim xorg alacritty firefox ttf-spacemono python-pip zsh picom-git
pip install neovim
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

echo -e "\n[*] Installing fonts..."
if [[ -d "$FDIR" ]]; then
	cp -rf $DIR/fonts/* "$FDIR"
else
	mkdir -p "$FDIR"
	cp -rf $DIR/fonts/* "$FDIR"
fi

echo "Adding wallpapers"
cd ~/my-dot-files
mkdir ~/Wallpapers
cp Wallpapers/1.png ~/Wallpapers

echo "Copyig config files"
cd ~/my-dot-files
cp -rf .config ~
cp pipes.sh ~

echo "Cleaning up"
rm -rf ly_install

echo "Installing oh-my-zsh"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
