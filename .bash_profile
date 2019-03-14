#####
# .bash_profile
# 
# Sourced for any login shell, it's purpose is to source other files when loging in with bash as the shell
#
#
#####

echo "Sourcing .bash_profile"

# Import general system definitions
source $HOME/.profile

# Import bash runtime definitions
source $HOME/.bashrc

