sudo apt update
sudo apt install vim gdb wget git curl zsh python3 python3-pip libssl-dev -y
# install pip & ipython 
sudo apt-get install ipython3 -y
sudo apt-get install gcc-multilib -y
# install pwntools
pip3 install pwntools
# install on-my-zsh   
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# install peda pwngdb
cd 
git clone https://github.com/longld/peda.git ~/peda
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
# install one_gadget
sudo apt install gem ruby ruby-dev -y
sudo gem install one_gadget
sudo gem install seccomp-tools
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
sed -i 's/^ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
echo "plugins+=(zsh-autosuggestions)" >> ~/.zshrc
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
echo "plugins+=(zsh-syntax-highlighting)" >> ~/.zshrc
