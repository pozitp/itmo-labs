#!/bin/bash

# убираем раннее созданную папку
chmod -R 700 ~/lab0
rm -rf ~/lab0 /tmp/error_375301.log /tmp/wc_375301.log

# 1. Создать приведенное в варианте дерево каталогов и файлов с содержимым. В качестве корня дерева использовать каталог lab0 своего домашнего каталога. Для создания и навигации по дереву использовать команды: mkdir, echo, cat, touch, ls, pwd, cd, more, cp, rm, rmdir, mv.
mkdir -p ~/lab0 ~/lab0/mudkip3 ~/lab0/sandslash0 ~/lab0/weezing1

# 2. Установить согласно заданию права на файлы и каталоги при помощи команды chmod, используя различные способы указания прав.

# electrode3: владелец должен читать и записывать файл; группа-владелец должна записывать файл; остальные пользователи должны не иметь никаких прав
echo $'Тип диеты\tErgovore' > ~/lab0/electrode3 && chmod u=rw,g=w,o= ~/lab0/electrode3
# igglybuff7: rw--w----
echo $'Ходы\tBody Slam Bounce\nCounter Covet Double-Edge Endeavor Gravity Heal Bell Helping Hand\nHyper Voice Icy Wind Last Resort Magic Coat Mega Kick Mega Punch Mimic\nMud-Slap Pain Split Recycle Role Play Rollout Seismic Toss Shock Wave\nSleep Talk Snore Water Pulse Uproar' > ~/lab0/igglybuff7 && chmod 640 ~/lab0/igglybuff7
echo $'Живет\tForest Grassland\nRainforest' > ~/lab0/leafeon5 && chmod u=r,go= ~/lab0/leafeon5 # leafeon5: r--------
echo $'weigth=55.8 height=31.0 atk=7\ndef=4' > ~/lab0/mudkip3/accelgor && chmod 400 ~/lab0/mudkip3/accelgor # accelgor: r--------# psyduck: владелец должен читать и записывать файл; группа-владелец должна не иметь никаких прав; остальные пользователи должны не иметь никаких прав
echo $'Способности\tTorrent Damp Cloud Nine' > ~/lab0/mudkip3/psyduck && chmod u=rw,go= ~/lab0/mudkip3/psyduck
echo $'Живет\nTaiga Tundra' > ~/lab0/mudkip3/glaceon && chmod u=r,o=r,g= ~/lab0/mudkip3/glaceon # glaceon: r-----r--
echo $'satk7 sdef=5 spd=4' > ~/lab0/mudkip3/mareep && chmod 006 ~/lab0/mudkip3/mareep # mareep: права 006
echo $'Тип покемона\tDARK\nNONE' > ~/lab0/mudkip3/zorua && chmod 404 ~/lab0/mudkip3/zorua # zorua: права 404
echo $'Развитые способности\tRegenerator' > ~/lab0/weezing1/tangela && chmod 664 ~/lab0/weezing1/tangela # tangela: права 664

# создаём файлы и меняем права
mkdir -p ~/lab0/mudkip3/vulpix && chmod 755 ~/lab0/mudkip3/vulpix # vulpix: права 755
# houndoom: владелец должен записывать директорию и переходить в нее; группа-владелец должна только переходить в директорию; остальные пользователи должны только переходить в директорию
mkdir -p ~/lab0/sandslash0/houndoom && chmod u=rx,go=x ~/lab0/sandslash0/houndoom
mkdir -p ~/lab0/sandslash0/rapidash && chmod 513 ~/lab0/sandslash0/rapidash # rapidash: r-x--x-wx
# aipom: владелец должен читать директорию и переходить в нее; группа-владелец должна читать, записывать директорию и переходить в нее; остальные пользователи должны записывать директорию и переходить в нее
mkdir -p ~/lab0/sandslash0/aipom && chmod u=rx,g=rwx,o=wx ~/lab0/sandslash0/aipom
mkdir -p ~/lab0/sandslash0/scraggy && chmod 500 ~/lab0/sandslash0/scraggy # scraggy: права 500
mkdir -p ~/lab0/weezing1/larvesta && chmod 771 ~/lab0/weezing1/larvesta # larvesta: права 771
# venipede: владелец должен записывать директорию и переходить в нее; группа-владелец должна записывать директорию и переходить в нее; остальные пользователи должны записывать директорию и переходить в нее
mkdir -p ~/lab0/weezing1/venipede && chmod a=wx ~/lab0/weezing1/venipede
mkdir -p ~/lab0/weezing1/ducklett && chmod 357 ~/lab0/weezing1/ducklett # ducklett: права 357
mkdir -p ~/lab0/weezing1/magikarp && chmod u=rwx,g=rx,o=wx ~/lab0/weezing1/magikarp # magikarp: rwxr-x-wx

echo "[TASK 1] Completed"

# меняем права директориям
chmod u=rx,g=rwx,o=wx ~/lab0/weezing1 # weezing1: r-xrwx-wx
chmod 524 ~/lab0/sandslash0 # sandslash0: r-x-w-r--
chmod 363 ~/lab0/mudkip3 # mudkip3: -wxrw--wx

echo "[TASK 2] Completed"


# 3. Скопировать часть дерева и создать ссылки внутри дерева согласно заданию при помощи команд cp и ln, а также комманды cat и перенаправления ввода-вывода.

# создать символическую ссылку c именем Copy_38 на директорию mudkip3 в каталоге lab0
ln -s ~/lab0/mudkip3 ~/lab0/Copy_38
# cоздать символическую ссылку для файла leafeon5 с именем lab0/mudkip3/psyduckleafeon
ln -s ~/lab0/leafeon5 ~/lab0/mudkip3/psyduckleafeon

# объеденить содержимое файлов lab0/mudkip3/mareep, lab0/mudkip3/psyduck, в новый файл lab0/igglybuff7_78
cat ~/lab0/mudkip3/mareep ~/lab0/mudkip3/psyduck > ~/lab0/igglybuff7_78

# скопировать рекурсивно директорию sandslash0 в директорию lab0/weezing1/venipede
cp -a ~/lab0/sandslash0/. ~/lab0/weezing1/venipede/
# скопировать содержимое файла electrode3 в новый файл lab0/mudkip3/accelgorelectrode
cat ~/lab0/electrode3 > ~/lab0/mudkip3/accelgorelectrode

# скопировать файл leafeon5 в директорию lab0/sandslash0/aipom
cp ~/lab0/leafeon5 ~/lab0/sandslash0/aipom/

# cоздать жесткую ссылку для файла igglybuff7 с именем lab0/mudkip3/mareepigglybuff
ln ~/lab0/igglybuff7 ~/lab0/mudkip3/mareepigglybuff

echo "[TASK 3] Completed"

ls -lR ~/lab0

echo "[TREE] Completed"

# 4. Используя команды cat, wc, ls, head, tail, echo, sort, grep выполнить в соответствии с вариантом задания поиск и фильтрацию файлов, каталогов и содержащихся в них данных.

# Подсчитать количество символов содержимого файлов в директории mudkip3, результат записать в файл в директории /tmp, ошибки доступа перенаправить в файл в директории /tmp
wc -m ~/lab0/mudkip3/* 2>> /tmp/error_375301.log | tail -1 | grep -Go '[0-9]*' > /tmp/wc_375301.log

# Вывести два последних элемента рекурсивного списка имен и атрибутов файлов в директории lab0, содержащих строку "on", список отсортировать по убыванию даты доступа к файлу, подавить вывод ошибок доступа
ls -Rlt ~/lab0/ 2> /dev/null | grep "on" | tail -2

# Вывести содержимое файлов: psyduck, glaceon, mareep, zorua, исключить строки, заканчивающиеся на 'r', ошибки доступа перенаправить в файл в директории /tmp
cat ~/lab0/mudkip3/psyduck ~/lab0/mudkip3/glaceon ~/lab0/mudkip3/mareep ~/lab0/mudkip3/zorua 2>> /tmp/error_375301.log | grep -v 'r$'

# Вывести содержимое файлов с номерами строк в директории mudkip3, оставить только строки, содержащие "ck", регистр символов игнорировать, ошибки доступа не подавлять и не перенаправлять
cat -n ~/lab0/mudkip3/* | grep -i "ck"

shopt -s globstar
# Рекурсивно подсчитать количество символов содержимого файлов из директории lab0, имя которых начинается на 'a', отсортировать вывод по увеличению количества, добавить вывод ошибок доступа в стандартный поток вывода
x=$(ls -1dp ~/lab0/**/a* 2> /dev/null | grep -v /$  | grep -v /$ | wc -m 2>&1)
echo "$x"

# Рекурсивно вывести содержимое файлов из директории lab0, имя которых заканчивается на 'p', строки отсортировать по имени a->z, ошибки доступа перенаправить в файл в директории /tmp
x=$(ls -1dp ~/lab0/**/*p 2> /dev/null | grep -v /$ | cat 2>> /tmp/error_375301.log)
echo "$x"

shopt -u globstar

echo "[TASK 4] Completed"


# 5. Выполнить удаление файлов и каталогов при помощи команд rm и rmdir согласно варианту задания.

# Удалить файл leafeon5
rm ~/lab0/leafeon5
# Удалить файл lab0/mudkip3/glaceon
rm ~/lab0/mudkip3/glaceon
# удалить символические ссылки Copy_*
rm ~/lab0/Copy_*
# удалить жесткие ссылки lab0/mudkip3/mareepigglybu*
rm ~/lab0/mudkip3/mareepigglybu*
# Удалить директорию weezing1
rm -r ~/lab0/weezing1
# Удалить директорию lab0/weezing1/larvesta
rm -r ~/lab0/weezing1/larvesta

echo "[TASK 5] Completed"