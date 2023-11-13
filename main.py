from unidecode import unidecode
import music_tag
import os

working_dir = "./" #will be set via command line argument

list_of_files = os.listdir(working_dir)
list_of_changes = []
keys_to_convert = ['tracktitle', 'artist', 'album', 'albumartist', 'composer']

for i, file in enumerate(list_of_files):
    file_no_unicode = unidecode(file)
    
    if file != file_no_unicode:
        print(file, file_no_unicode)
        os.rename(file, file_no_unicode)
        file = file_no_unicode
        list_of_changes.append(f"{i}  {file} ---> {file_no_unicode}")
    
    file_type = file.split(".")[-1]
    
    f = music_tag.load_file(file)

    for key in keys_to_convert:
        current_meta = str(f[key])
        meta_no_unicode = unidecode(str(current_meta))
        
        if current_meta != meta_no_unicode:
            f[key] = meta_no_unicode
            list_of_changes.append(f"{i}  {file}>{key} | {current_meta} ---> {meta_no_unicode}")
            f.save()

            
for change in list_of_changes:
    print(change)