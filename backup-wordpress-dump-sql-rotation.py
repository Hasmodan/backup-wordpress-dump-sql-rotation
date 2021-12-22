#!/usr/bin/python3

import shutil
import zipfile
from datetime import datetime
import os
import time
import pipes

#Information BDD
DB_HOST = 'Votre NOM d'hôte '
DB_USER = 'NOM utilisateur '
DB_USER_PASSWORD = 'Le MDP de votre BDD '
DB_NAME = 'Nom de votre BDD '
BACKUP_PATH = '/Chemin/de/sauvegarde/de votre/ fichier/'

TODAYBACKUPPATH = BACKUP_PATH

# Vérifie que le fichier existe sinon on le crée.
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

# Code pour DUMP soit une seul BDD ou bien un ensemble de BDD .
print("Recherche de fichier du nom de la BDD.")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print("BDD trouvé...")
    print("Démarrage de la sauvegarde de toutes les BDD lister dans le répertoire " + DB_NAME)
else:
    print("BDD trouvé...")
    print("Démarrage sauvegarde BDD " + DB_NAME)
    multi = 0

# Démarrage du DUMP de la BDD .
if multi:
    in_file = open(DB_NAME, "r")
    flength = len(in_file.readlines())
    in_file.close()
    p = 1
    dbfile = open(DB_NAME, "r")

    while p <= flength:
        db = dbfile.readline()  # lecture de la database par le nom du fichier
        db = db[:-1]  # supression des lignes supplémentaire
        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(
            TODAYBACKUPPATH) + "/" + db + ".sql"
        os.system(dumpcmd)
        gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        os.system(gzipcmd)
        p = p + 1
    dbfile.close()
else:
    db = DB_NAME
    dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(
        TODAYBACKUPPATH) + "/" + db + ".sql"
    os.system(dumpcmd)
    gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
    os.system(gzipcmd)

time.sleep(2)

shutil.move('ici j'ai fais le choix de changer l'emplacement de mon archive pour quel soit dans un autre folder que j'ai nommé backup ')

print("le backup SQL est sauvegarder sur le BUREAU dossier BACKUP! Bien joué le SysAdmin Good Job =D ") # petit message à titre informatif 

time.sleep(2)

shutil.make_archive("emplacement ou je souhaite faire mon archive avec nom du fichier du nom "BACKUPWP", 'zip', "/var/www/html/wordpress/") 

filename = f"BackupFINAL-{datetime.now():%d-%m-%Y}.zip"
os.chdir('indiquer le chemin pour avoir l'archive là ou vous le voulez')
## Open the zip file for appending
zip_file = zipfile.ZipFile(filename , mode='a')

## Ajouter le chemin des fichiers ZIP
zip_file.write('/,,,/,,,/,,,/,,,/wordpress.sql.gz') 
zip_file.write('/,,,/,,,/,,,/BACKUP/BACKUPWP.zip')



if os.path.exists("/home/username/Bureau/"):
  os.remove("/,,,/,,,/,,,/BACKUP/wordpress.sql.gz")
  os.remove("/,,,/,,,/,,,/BACKUP/BACKUPWP.zip")
else:
  print("Les fichiers n'existent pas")


#Rotation des fichiers avec liste 

current_time = time.time()
joursuppr = 1
directory = '/indiquer/votre/chemin/ici'

for dirpath,_,filenames in os.walk(directory):
    for f in filenames:
        fileWithPath = os.path.abspath(os.path.join(dirpath, f))
        creation_time = os.path.getmtime(fileWithPath)
        #GETMTIME debug format date sur linux
        print(datetime.fromtimestamp(creation_time).strftime("%d-%m-%Y"))
        print("FICHIER DISPO:",fileWithPath)
        if (current_time - creation_time) // (24 * 3600) >= joursuppr:
            os.unlink(fileWithPath)
            print('{} SUPPRIME'.format(fileWithPath))
            print("\n")
        else:
            print('{} PAS SUPPRIME'.format(fileWithPath))