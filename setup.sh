#!/bin/bash
#
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
