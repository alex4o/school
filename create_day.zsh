#/bin/zsh
#
today=$(date '+%d.%m.%Y')
if [ ! -d books/$today ]; then
	echo Creating dir for $today
	mkdir books/$today
else
	echo Already exist
	
fi
