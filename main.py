import re
import os

def time_stamp_remover(srt : str):

    #time_stamp_pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})")
    time_stamp_pattern = re.compile(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}')
    stamp_removed = re.sub(time_stamp_pattern, " ", srt)
    stamp_removed = stamp_removed.splitlines()
    pruned = ""
    for i, line in enumerate(stamp_removed):
        print(line)
        for j in range(i+1, i + min(10, len(stamp_removed)-1 -i)):
            if line == stamp_removed[j] :
                print(line)
                line = "\n"
        pruned = pruned + line
    final = "" 
    pruned = pruned.splitlines()
    for line in pruned:
        if line =="\n" or line =="" or line == " ":
            pass
        else:
            final += line + "\n"
        
    return final 


def srt2txt(srt_path, txt_path):
    """
    A file type or address is used here to turn a srt file into a txt file.
    """
    with open(srt_path, "r") as srt_file:
        with open(txt_path, "w") as txt_file:
            final = time_stamp_remover(srt_file.read())
            txt_file.write(final)


def process_folder(path_to_folder, path_to_destination=None):
    
    if path_to_destination is None:
        path_to_destination = path_to_folder
    if not os.path.exists(path_to_destination):
        os.makedirs(path_to_destination)
    for file in os.listdir(path_to_folder):
        if file.endswith(".srt"):
            srt2txt(os.path.join(path_to_folder , file), os.path.join(path_to_destination , file[:-4] + ".txt"))

def main():
    #srt2txt("./Bake Faster with Blender 2.80 [rrUWC6vKQaQ].en.srt", "./Bake Faster with Blender 2.80 [rrUWC6vKQaQ].en.txt")
    process_folder("./",'./Processed')

    

if __name__ == "__main__":
    main()