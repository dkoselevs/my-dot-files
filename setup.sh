#!/bin/bash
#
copy_stuff(){
    cp -rf .config ~
    cp .xbindkeysrc ~
    cp .zshrc ~
}

download_install_ly(){
    mkdir ly_install
    cd ly_install
    git clone --recurse-submodules https://github.com/nullgemm/ly.git
    cd ly
    make
    sudo make install
    sudo systemctl enable ly.service
}

clear
cat <<- EOF
[*] Installing packages...
[1] Install reqired
[2] Intall all(PyCharm, OnlyOffice)

EOF 
read -p "[?] Select Option : "
if [ $REPLY = "1" ]; then
paru -S qtile xbindkeys rofi polybar nitrogen pcmanfm neovim
elif [ $REPLY = "2" ]; then
paru -S qtile xbindkeys rofi polybar nitrogen pcmanfm neovim onlyoffice-bin pycharm-professional
else
echo -e "[!] Invalid Option, Exiting...  Your option - $REPLY"
exit 1
fi

copy_stuff
download_install_ly
