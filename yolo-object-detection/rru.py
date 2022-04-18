import os
import subprocess

# Run detections on all files in the inputVideos directory
for fileName in os.listdir("videos/"):
    lastDotIndex = fileName.rfind(".")
    print(fileName[:lastDotIndex])
    print(" yolo_video.py --input videos/" + fileName + " --output outputVideos/" + \
          fileName[:lastDotIndex] + ".avi --yolo yolo-coco --use-gpu 1")
    cmd = "yolo_video.py --input videos/" + fileName + " --output output/" + \
          fileName[:lastDotIndex] + ".avi --yolo yolo-coco "
    print("Running command:\n" + cmd)
    subprocess.run(cmd, shell=True)
