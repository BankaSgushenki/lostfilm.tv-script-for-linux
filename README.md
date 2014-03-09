lostfilm.tv-app
===============
A simple script that allows you not to miss the new series of the favorite show.


##Usage

Add to cron. For Ubunta something like: 
```sh
* * * * * export DISPLAY=:0.0 && export XAUTHORITY=/home/username/.Xauthority && sudo -u username /usr/bin/python /path_to/source.py
```
