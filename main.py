import re
import os

def timeStampRemover(srt : str):

    #timestampPattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})")
    timestampPattern = re.compile(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}')
    stampRemoved = re.sub(timestampPattern, " ", srt)
    stampRemoved = stampRemoved.splitlines()
    pruned = ""
    for i, line in enumerate(stampRemoved):
        print(line)
        for j in range(i+1, i + min(10, len(stampRemoved)-1 -i)):
            if line == stampRemoved[j] :
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
            final = timeStampRemover(srt_file.read())
            txt_file.write(final)


def ProcessFolder(path_to_folder):
    for file in os.listdir(path_to_folder):
        if file.endswith(".srt"):
            srt2txt(path_to_folder + file, path_to_folder + file[:-4] + ".txt")

def main():
    #srt2txt("./Bake Faster with Blender 2.80 [rrUWC6vKQaQ].en.srt", "./Bake Faster with Blender 2.80 [rrUWC6vKQaQ].en.txt")
    ProcessFolder("./")

    

if __name__ == "__main__":
    main()