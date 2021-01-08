# OTP-
Generate mode
This program generate 100 pads. Each batch of this 100 pads will reside in a subfolder of the directory specified through the positional argument. 
As positional argument you should have dir/0000 and dir/0001 each containing 100 pads.
Dans ce programme, on génère des pads, des  préfixes et des suffixes.
on code chaque message donné avec le premier pads disponible, 
qui est le préfixe et  en ajoute pad xor message et en ajoute le suffix le 
On enregistre le texte chiffré dans un fichier.
 et on fait l’inverse Pour décoder, nous parcourons le répertoire contenant les pads pour le préfixe correct.
et on Décode la partie du milieu du message XOR avec le pad qui lui correspond.
