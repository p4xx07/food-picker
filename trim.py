import os

def trimVideoToGif(inputPath, start, end):
    command = f"sudo ffmpeg -ss {start} -t {end} -i {inputPath} -vf \"fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse\" -loop 0 output.gif"
    print(command)
    os.system(command)



