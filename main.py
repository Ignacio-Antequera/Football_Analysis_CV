from utils import read_video, save_video
from trackers import Tracker
import cv2 as cv
from team_assigner import TeamAssigner
import os

def process_video(video_path, output_path, stub_path):
    """Process a single video file"""
    print(f"\n{'='*60}")
    print(f"Processing: {os.path.basename(video_path)}")
    print(f"{'='*60}")
    
    # Read video frames
    video_frames, fps = read_video(video_path)
    print(f"Loaded {len(video_frames)} frames at {fps} FPS")
    
    # Initialize tracker
    tracker = Tracker("models/best.pt")
    
    # Get object tracks
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=False,
                                       stub_path=stub_path)
    print("Object tracking complete")
    
    # Interpolate ball tracks
    tracks['ball'] = tracker.interpolate_ball_positions(tracks['ball'])
    print("Ball position interpolation complete")
    
    # Assign teams to players
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track["bbox"], player_id)
            tracks['players'][frame_num][player_id]["team"] = team
            tracks['players'][frame_num][player_id]["team_color"] = team_assigner.team_colors[team]
    print("Team assignment complete")
    
    # Draw annotations on video frames
    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    print("Annotations drawn")
    
    # Save video frames
    save_video(output_video_frames, output_path, fps=fps)
    print(f"Video saved to: {output_path}")

def main():
    # Define input and output directories
    input_dir = "input_videos"
    output_dir = "output_videos"
    stub_dir = "stubs"
    
    # Create output directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(stub_dir, exist_ok=True)
    
    # Get all video files in input directory
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
    video_files = [f for f in os.listdir(input_dir) 
                   if f.lower().endswith(video_extensions)]
    
    if not video_files:
        print(f"No video files found in {input_dir}")
        return
    
    print(f"Found {len(video_files)} video(s) to process:")
    for i, video in enumerate(video_files, 1):
        print(f"  {i}. {video}")
    
    # Process each video
    for video_file in video_files:
        video_path = os.path.join(input_dir, video_file)
        
        # Create output filename (keep same name, change to .avi)
        video_name = os.path.splitext(video_file)[0]
        output_path = os.path.join(output_dir, f"{video_name}.avi")
        stub_path = os.path.join(stub_dir, f"{video_name}_track_stubs.pkl")
        
        try:
            process_video(video_path, output_path, stub_path)
        except Exception as e:
            print(f"ERROR processing {video_file}: {str(e)}")
            continue
    
    print(f"\n{'='*60}")
    print("All videos processed!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()