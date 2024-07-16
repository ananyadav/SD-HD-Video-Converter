import cv2
import os

def video_to_jpg(video_path, output_folder, output_txt_path):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    frame_names = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = f"frame_{frame_count:04d}.jpg"
        output_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(output_path, frame)
        frame_names.append(frame_name)

        frame_count += 1

    cap.release()

    with open(output_txt_path, 'w') as f:
        for name in frame_names:
            f.write("%s\n" % name)

def video(video_path, output_path, output_txt_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    frame_names = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = f"frame_{frame_count:04d}.jpg"
        output_path = os.path.join(output_path, frame_name)
        cv2.imwrite(output_path, frame)
        frame_names.append(frame_name)

        frame_count += 1

    cap.release()

    with open(output_txt_path, 'w') as f:
        for name in frame_names:
            f.write("%s\n" % name)

# Example usage
if __name__ == "__main__":
    video_path_sd = "C://Users//ADMIN//SD-HD-Video-Converter//Devi_Stuti_sd.mp4"
    output_folder_sd = "C://Users//ADMIN//SD-HD-Video-Converter//output_sd_frames"
    output_txt_path_sd = "C://Users//ADMIN//SD-HD-Video-Converter//frames_sd_list.txt"

    video_to_jpg(video_path_sd, output_folder_sd, output_txt_path_sd)

    video_path_hd = "C://Users//ADMIN//SD-HD-Video-Converter//Devi_Stuti_hd.mp4"
    output_folder_hd = "C://Users//ADMIN//SD-HD-Video-Converter//output_hd_frames"
    output_txt_path_hd = "C://Users//ADMIN//SD-HD-Video-Converter//frames_hd_list.txt"

    video(video_path_hd, output_folder_hd, output_txt_path_hd)
