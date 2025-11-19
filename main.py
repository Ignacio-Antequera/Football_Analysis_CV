from utils import read_video, save_video
from trackers import Tracker
import cv2 as cv
from team_assigner import TeamAssigner

def main():
    # Read video frames
    video_frames, fps = read_video("input_videos/Take_N1.mp4")
    
    # Initialize tracker with the first frame
    tracker = Tracker("models/best.pt", frame_rate=fps)
    
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub = True,
                                       stub_path = "stubs/track_stubs.pkl")
    
    # Assign teams to players
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks)
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track["bbox"], player_id)
            tracks['players'][frame_num][player_id]["team"] = team
            tracks['players'][frame_num][player_id]["team_color"] = team_assigner.team_colors[team]
            
    
    # Draw annotations on video frames
    
    ## Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks['players'][0])
    
    # Save video frames
    save_video(output_video_frames, "output_videos/Take_N1_output.avi", fps=fps)
    
if __name__ == "__main__":
    main()