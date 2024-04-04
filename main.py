import re


def timeStampRemover(srt : str):

    #timestampPattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})")
    timestampPattern = re.compile(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}')
    return re.sub(timestampPattern, " ", srt)


def srt2txt(srt_path, txt_path):
    """
    A file type or address is used here to turn a srt file into a txt file.
    """
    with open(srt_path, "r") as srt_file:
        with open(txt_path, "w") as txt_file:
            stampRemoved = timeStampRemover(srt_file.read())
            txt_file.write(stampRemoved)

def main():
    srt2txt("./Bake Faster with Blender 2.80 [rrUWC6vKQaQ].en.srt", "./Bake Faster with Blender 2.80 [rrUWC6vKQaQ].en.txt")

    

if __name__ == "__main__":
    main()