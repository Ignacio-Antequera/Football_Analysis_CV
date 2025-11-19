from utils import read_video, save_video
from trackers import Tracker
import cv2 as cv

def main():
    # Read video frames
    video_frames, fps = read_video("input_videos/Take_N1.mp4")
    
    # Initialize tracker with the first frame
    tracker = Tracker("models/best.pt", frame_rate=fps)
    
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub = True,
                                       stub_path = "stubs/track_stubs.pkl")
    
    # Save cropped image of a player
    for track_id, player in tracks["players"][0].items():
        bbox = player['bbox']
        frame = video_frames[0]
        
        # Crop the player from the frame
        cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
        
        # Save the cropped image
        cv.imwrite(f"output_videos/croppped_image.jpg", cropped_image)
        break
    
    # Draw annotations on video frames
    
    ## Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    
    # Save video frames
    save_video(output_video_frames, "output_videos/Take_N1_output.avi", fps=fps)
    
if __name__ == "__main__":
    main()