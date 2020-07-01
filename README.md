# WandDecoder
Decodes Opera's *wand.dat* file so you can see your passwords stored in Opera Wand. Also works for Opera Mail.

Original work by sna@reteam.org, but it seems to have disappeared.
Explanation from http://securityxploded.com/operapasswordsecrets.php used.
pyDes from pydes.sourceforge.net

Compatible with Opera 33.0 (and an unknown number of versions above and below, the wand format doesn't seem to change much) and Opera Mail 1.0.
Works with Python 3 and maybe still with Python 2.

# Usage
Download WandDecoder.py and pyDes.py, then run *python WandDecoder.py somepath/wand.dat* to print all your wand secrets.
