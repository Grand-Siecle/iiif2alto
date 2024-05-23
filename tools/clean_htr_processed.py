import os, re

"""Pour supprimer les fichiers XML déjà traités pour reprendre la suite du process sans recommencer la totalité
Seulement en cas de problème pour la partie OCR
Lit un fichier de logs, retrouve les fichiers xml dans les erreurs, fait une liste des fichiers existants puis supprime ceux qui ne sont pas la liste des erreurs
"""

with open('errors.txt', 'r') as f:
	log = f.read()

pattern = r'([^:\s]+\.xml)'

# Trouver tous les noms de fichiers XML dans le log
matches = re.findall(pattern, log)

xml_files = [match.split('/')[-1] for match in matches]

# Afficher la liste des noms de fichiers XML
xml_files_from_log = set(xml_files) 
xml_directory = './images/'
all_xml_files = set(f for f in os.listdir('./images/') if f.endswith('.xml'))

files_to_delete = all_xml_files - xml_files_from_log

print(len(files_to_delete))
for xml_file in files_to_delete:
    os.remove(os.path.join(xml_directory, xml_file))
