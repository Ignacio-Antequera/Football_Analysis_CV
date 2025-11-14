from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read video frames
    video_frames = read_video("input_videos/Take_N1.mp4")
    
    # Initialize tracker with the first frame
    tracker = Tracker("models/best.pt")
    
    tracks = tracker.get_object_tracks(video_frames)
    
    # Save video frames
    save_video(video_frames, "output_videos/Take_N1_output.avi")
    
if __name__ == "__main__":
    main()