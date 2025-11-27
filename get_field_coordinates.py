import cv2 as cv
import numpy as np

points = []
current_frame = 0
frame = None
original_frame = None

def mouse_callback(event, x, y, flags, param):
    global points, frame
    
    if event == cv.EVENT_LBUTTONDOWN:
        points.append([x, y])
        cv.circle(frame, (x, y), 5, (0, 255, 0), -1)
        cv.putText(frame, f"{len(points)}: ({x},{y})", (x+10, y-10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv.imshow('Select Field Corners', frame)
        print(f"Point {len(points)}: [{x}, {y}]")
        
        if len(points) == 4:
            print(f"\npixel_vertices = np.array({points})")

def browse_and_select(video_path):
    global points, current_frame, frame, original_frame
    
    cap = cv.VideoCapture(video_path)
    total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv.CAP_PROP_FPS)
    
    print(f"Total frames: {total_frames}, FPS: {fps}")
    print("\nControls:")
    print("  Right Arrow: Next frame")
    print("  Left Arrow: Previous frame")
    print("  Space: Jump 30 frames forward")
    print("  Backspace: Jump 30 frames backward")
    print("  Click: Select point (need 4 points)")
    print("  'r': Reset points")
    print("  'q': Quit")
    print("\nClick on 4 field corners in this order:")
    print("1. Bottom-left corner")
    print("2. Top-left corner")
    print("3. Top-right corner")
    print("4. Bottom-right corner")
    
    cap.set(cv.CAP_PROP_POS_FRAMES, current_frame)
    ret, original_frame = cap.read()
    frame = original_frame.copy()
    
    cv.namedWindow('Select Field Corners')
    cv.setMouseCallback('Select Field Corners', mouse_callback)
    
    while True:
        cv.imshow('Select Field Corners', frame)
        cv.setWindowTitle('Select Field Corners', f'Frame {current_frame}/{total_frames}')
        
        key = cv.waitKey(0) & 0xFF
        
        if key == ord('q') or len(points) == 4:
            break
        elif key == ord('r'):
            points = []
            frame = original_frame.copy()
            print("\nPoints reset. Start clicking again.")
        elif key == 83:  # Right arrow
            current_frame = min(current_frame + 1, total_frames - 1)
            cap.set(cv.CAP_PROP_POS_FRAMES, current_frame)
            ret, original_frame = cap.read()
            frame = original_frame.copy()
            points = []
            print(f"\nFrame {current_frame}")
        elif key == 81:  # Left arrow
            current_frame = max(current_frame - 1, 0)
            cap.set(cv.CAP_PROP_POS_FRAMES, current_frame)
            ret, original_frame = cap.read()
            frame = original_frame.copy()
            points = []
            print(f"\nFrame {current_frame}")
        elif key == 32:  # Space
            current_frame = min(current_frame + 30, total_frames - 1)
            cap.set(cv.CAP_PROP_POS_FRAMES, current_frame)
            ret, original_frame = cap.read()
            frame = original_frame.copy()
            points = []
            print(f"\nJumped to frame {current_frame}")
        elif key == 8:  # Backspace
            current_frame = max(current_frame - 30, 0)
            cap.set(cv.CAP_PROP_POS_FRAMES, current_frame)
            ret, original_frame = cap.read()
            frame = original_frame.copy()
            points = []
            print(f"\nJumped to frame {current_frame}")
    
    cap.release()
    cv.destroyAllWindows()
    return points

if __name__ == "__main__":
    # Change this to your video file
    video_path = 'input_videos/Take_N4.mp4'
    
    points = browse_and_select(video_path)
    
    if points and len(points) == 4:
        print("\n" + "="*60)
        print("Copy this into your view_transformer.py:")
        print(f"self.pixel_vertices = np.array({points})")
        print("="*60)
