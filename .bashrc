# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

export PATH=$PATH:~/.bin/python/

alias python='python3'
alias s='cd ~/.scratch'
alias bashrc='kate ~/.bashrc'
alias sourceit='source ~/.bashrc'

alias web='cd ~/.scratch/web'


# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
