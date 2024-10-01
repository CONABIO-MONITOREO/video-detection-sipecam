import cv2
import os

from pathlib import Path
from dotenv import load_dotenv

from megadetector.detection.run_detector_batch import \
    load_and_run_detector_batch
from megadetector.utils import path_utils

import shutil



load_dotenv()

data_directory = os.getenv('DATA_DIRECTORY')
frames_directory = os.getenv('FRAMES_DIRECTORY')
model_filename = os.getenv('MEGADETECTOR_MODEL')
with_animal_directory = os.getenv('WITH_ANIMAL_DIRECTORY')
without_animal_directory = os.getenv('WITHOUT_ANIMAL_DIRECTORY')

folder_path = Path(data_directory)

extensions = ['*.mp4', '*.avi', '*.mov', '*.mkv']

for extension in extensions:
    
    files = folder_path.rglob(extension)
    
    for file in files:
        
        if not os.path.exists(frames_directory):
            os.makedirs(frames_directory)

        cap = cv2.VideoCapture(str(file))
        has_animal = False
        fps = cap.get(cv2.CAP_PROP_FPS)
        frames_interval = int(fps * 0.5)
        frame_count = 0
        saved_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % frames_interval == 0:
                frame_filename = os.path.join(frames_directory, f'frame_{saved_count:04d}.jpg')
                cv2.imwrite(frame_filename, frame)
                saved_count += 1
        cap.release()

        image_file_names = path_utils.find_images(frames_directory, recursive=True)
        results = load_and_run_detector_batch(model_filename, image_file_names)
        
        for result in results:
            for detection in result['detections']:
                if detection['category'] and detection['conf'] > 0.45:
                    print(str(file))
                    has_animal = True
                    break
            if has_animal:
                break

        if has_animal:
            shutil.copy(str(file), with_animal_directory)
        else:
            #shutil.copy(str(file), without_animal_directory)
            pass
        
        if os.path.exists(frames_directory):
            shutil.rmtree(frames_directory)
        
