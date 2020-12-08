import ffmpeg
import sys

input = ffmpeg.input(sys.argv[1])
output = ffmpeg.output(input, 'out.mp4', vcodec='libx264', vf='pad=w=iw+50:h=ih:x=25:y=0:color=white')

output.run()
