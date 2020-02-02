#!/bin/bash

grep -n solid splitted.stl > patches_info.txt



grep -n patch0 patches_info.txt | cut -d":" -f2 > lines.txt
var1=$(sed -n '1p' lines.txt)
var2=$(sed -n '2p' lines.txt)
rm lines.txt
#echo $var1
#echo $var2
sed -n "$var1,$var2 p" splitted.stl > patch0.stl



grep -n patch1 patches_info.txt | cut -d":" -f2 > lines.txt
var1=$(sed -n '1p' lines.txt)
var2=$(sed -n '2p' lines.txt)
rm lines.txt
sed -n "$var1,$var2 p" splitted.stl > patch1.stl



grep -n patch2 patches_info.txt | cut -d":" -f2 > lines.txt
var1=$(sed -n '1p' lines.txt)
var2=$(sed -n '2p' lines.txt)
rm lines.txt
sed -n "$var1,$var2 p" splitted.stl > patch2.stl



grep -n patch3 patches_info.txt | cut -d":" -f2 > lines.txt
var1=$(sed -n '1p' lines.txt)
var2=$(sed -n '2p' lines.txt)
rm lines.txt
sed -n "$var1,$var2 p" splitted.stl > patch3.stl



grep -n patch4 patches_info.txt | cut -d":" -f2 > lines.txt
var1=$(sed -n '1p' lines.txt)
var2=$(sed -n '2p' lines.txt)
sed -n "$var1,$var2 p" splitted.stl > patch4.stl



cat patch0.stl patch1.stl patch2.stl patch3.stl patch4.stl > output_split.stl
