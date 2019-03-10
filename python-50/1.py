import glob, os
os.chdir(f"E:\\face_recognization\\ChikonEye_a-third-eye-app-which-protects-your-work-from-peepers\\dataSet")
for file in glob.glob("*.jpg"):
    print(file)