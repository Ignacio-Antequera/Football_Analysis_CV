from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read video frames
    video_frames = read_video("input_videos/Take_N1.mp4")
    
    # Initialize tracker with the first frame
    tracker = Tracker("models/best.pt")
    
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub = True,
                                       stub_path = "stubs/track_stubs.pkl")
    
    # Draw annotations on video frames
    
    ## Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    
    # Save video frames
    save_video(output_video_frames, "output_videos/Take_N1_output.avi")
    
if __name__ == "__main__":
    main()