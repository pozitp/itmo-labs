#!/bin/bash

# remove folder
chmod -R 777 ~/lab0
rm -rf ~/lab0

# create directories
mkdir -p ~/lab0 ~/lab0/mudkip3 ~/lab0/sandslash0 ~/lab0/weezing1

# add files and change permissions
echo $'Тип диеты\tErgovore' > ~/lab0/electrode3 && chmod u=rw,g=w,o= ~/lab0/electrode3 
echo $'Ходы\tBody Slam Bounce\nCounter Covet Double-Edge Endeavor Gravity Heal Bell Helping Hand\nHyper Voice Icy Wind Last Resort Magic Coat Mega Kick Mega Punch Mimic\nMud-Slap Pain Split Recycle Role Play Rollout Seismic Toss Shock Wave\nSleep Talk Snore Water Pulse Uproar' > ~/lab0/igglybuff7 && chmod 640 ~/lab0/igglybuff7
echo $'Живет\tForest Grassland\nRainforest' > ~/lab0/leafeon5 && chmod u=r,go= ~/lab0/leafeon5
echo $'weigth=55.8 height=31.0 atk=7\ndef=4' > ~/lab0/mudkip3/accelgor && chmod 400 ~/lab0/mudkip3/accelgor
echo $'Способности\tTorrent Damp Cloud Nine' > ~/lab0/mudkip3/psyduck && chmod u=rw,go= ~/lab0/mudkip3/psyduck
echo $'Живет\nTaiga Tundra' > ~/lab0/mudkip3/glaceon && chmod u=r,o=r,g= ~/lab0/mudkip3/glaceon
echo $'satk7 sdef=5 spd=4' > ~/lab0/mudkip3/mareep && chmod 006 ~/lab0/mudkip3/mareep
echo $'Тип покемона\tDARK\nNONE' > ~/lab0/mudkip3/zorua && chmod 404 ~/lab0/mudkip3/zorua
echo $'Развитые способности\tRegenerator' > ~/lab0/weezing1/tangela && chmod 664 ~/lab0/weezing1/tangela

# create directories and change permissons
mkdir -p ~/lab0/mudkip3/vulpix && chmod 755 ~/lab0/mudkip3/vulpix
mkdir -p ~/lab0/sandslash0/houndoom && chmod u=rx,go=x ~/lab0/sandslash0/houndoom
mkdir -p ~/lab0/sandslash0/rapidash && chmod 513 ~/lab0/sandslash0/rapidash
mkdir -p ~/lab0/sandslash0/aipom && chmod u=rx,g=rwx,o=wx ~/lab0/sandslash0/aipom
mkdir -p ~/lab0/sandslash0/scraggy && chmod 500 ~/lab0/sandslash0/scraggy
mkdir -p ~/lab0/weezing1/larvesta && chmod 771 ~/lab0/weezing1/larvesta
mkdir -p ~/lab0/weezing1/venipede && chmod a=wx ~/lab0/weezing1/venipede
mkdir -p ~/lab0/weezing1/ducklett && chmod 357 ~/lab0/weezing1/ducklett
mkdir -p ~/lab0/weezing1/magikarp && chmod u=rwx,g=rx,o=wx ~/lab0/weezing1/magikarp

# change permissions for root directories
chmod u=rx,g=rwx,o=wx ~/lab0/weezing1
chmod 524 ~/lab0/sandslash0
chmod 363 ~/lab0/mudkip3


ln -sf ~/lab0/mudkip3 ~/lab0/Copy_38
ln -sf ~/lab0/leafon5 ~/lab0/mudkip3/psyduckleafon

chmod u+r ~/lab0/mudkip3/mareep
cat ~/lab0/mudkip3/mareep ~/lab0/mudkip3/psyduck > ~/lab0/igglybuff7_78
chmod u-r ~/lab0/mudkip3/mareep

cp -a ~/lab0/sandslash0/. ~/lab0/weezing1/venipede/
cat ~/lab0/electrode3 > ~/lab0/mudkip3/accelgorelectrode

chmod u+w ~/lab0/sandslash0/aipom
cp ~/lab0/leafeon5 ~/lab0/sandslash0/aipom/
chmod u-w ~/lab0/sandslash0/aipom

ln -f ~/lab0/igglybuff7 ~/lab0/mudkip3/mareepigglybuff

chmod u+r ~/lab0/mudkip3 ~/lab0/mudkip3/mareep
wc -m ~/lab0/mudkip3/* | tail -1 | grep -Go '[0-9]*' 2>> /tmp/error_375301.log > /tmp/wc_375301.log
chmod u-r ~/lab0/mudkip3 ~/lab0/mudkip3/mareep

chmod u+r ~/lab0/weezing1/ducklett ~/lab0/mudkip3
ls -Rltr ~/lab0/ | grep "on" | tail -2 2> /dev/null
chmod u-r ~/lab0/weezing1/ducklett ~/lab0/mudkip3

chmod u+r ~/lab0/mudkip3/mareep 
cat ~/lab0/mudkip3/psyduck ~/lab0/mudkip3/glaceon ~/lab0/mudkip3/mareep ~/lab0/mudkip3/zorua | grep -v 'r$' 2>> /tmp/error_375301.log
chmod u-r ~/lab0/mudkip3/mareep

chmod u+r ~/lab0/mudkip3
grep -in "ck" ~/lab0/mudkip3/*
chmod u-r ~/lab0/mudkip3

find ~/lab0/ -type f -name "a*" -exec sh -c "wc -m $1 2>> /tmp/errror_375301.log" -- {} \;
find ~/lab0/ -type f -name "p$" -exec sh -c "cat $1 | sort 2>> /tmp/error_375301.log" -- {} \;


# rm ~/lab0/leafeon5
# rm ~/lab0/mudkip3/glaceon
# rm ~/lab0/Copy_*
# rm ~/lab0/mudkip3/mareepigglybu*
# rm -r ~/lab0/weezing1
# rm -r ~/lab0/weezing1/larvesta
