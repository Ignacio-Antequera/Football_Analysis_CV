# ⚽ Football Analysis with Computer Vision

> "I stopped looking at the footage as a player and started looking at it as a Computer Vision engineer."

## 📖 About the Project

🥉🌍 **BRONZE MEDALIST - FISU University World Cup** 🌍🥉

Last September, I had the honor and privilege of participating in the **FISU University World Cup** in **Dalian, China 🇨🇳**, representing the **University of Granada**. It was a unique experience where we managed to bring home the **bronze medal**. 🥉⚽️

Defending and representing my university, city, and country on an international stage was incredible. Sharing this experience with my younger brother, Bruno, made it even more unforgettable. 🫂⚽️

As an **AI researcher**, I was also fascinated by the investment in technology surrounding the event. 🤖💻

When I returned home and watched the broadcast recordings of our games, my perspective shifted. I stopped looking at the footage just as a player and started looking at it as a Computer Vision engineer. I realized I had the perfect dataset right in front of me.

I decided to challenge myself: **could I build an AI system capable of analyzing the very match I just played in?**

This project became the perfect intersection of my two biggest passions: **Football** and **Artificial Intelligence**.

---

## 🚀 Key Features & Pipeline

Here is how I turned raw broadcast footage into actionable sports analytics:

### 1. Detection & Tracking 🕵️‍♂️
I didn't want to just use a standard model. I fine-tuned **YOLO** to detect players, referees, and the ball specifically for this footage, ensuring the tracking was robust even in a crowded scene.

### 2. Team Identification 👕
To automate the analysis, the system needs to know who is who. I implemented **K-means clustering** to segment pixel colors within bounding boxes, automatically assigning players to teams based on their jerseys.

### 3. The "Moving Camera" Problem 🎥
Broadcast cameras are constantly panning and zooming. I utilized **Optical Flow** to calculate camera movement between frames, allowing me to stabilize the view and track true player movement.

### 4. From Pixels to Meters 📏
This was the most critical step. By applying **Perspective Transformation**, I mapped the distorted 3D camera view to a 2D bird's-eye perspective. This allowed me to measure player speed and distance covered in actual meters, not just pixels.

### 5. The Analytics 📊
Finally, I built the logic to calculate **ball acquisition percentages** and generate physical performance metrics for the players.

---

## 🛠️ Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Ignacio-Antequera/Football_Analysis_CV.git
    cd Football_Analysis_CV
    ```

2.  **Install dependencies**
    Ensure you have Python installed. It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download Models**
    Ensure the YOLO models are placed in the `models/` directory.
    - `models/best.pt` (Fine-tuned model)
    - `models/yolov8x.pt` (Base model)

---

## 🏃‍♂️ Usage

1.  **Prepare Input Video**
    Place your input video in the `input_videos/` directory. The default expected file is `input_videos/Take_N4.mp4`.

2.  **Run the Analysis**
    Execute the main script to start the processing pipeline:
    ```bash
    python main.py
    ```

3.  **View Results**
    The processed video with annotations and metrics will be saved in the `output_videos/` directory (e.g., `output_videos/Take_N4_output_video.avi`).

---

## 📂 Project Structure

- `main.py`: The entry point of the application.
- `trackers/`: Modules for object tracking (players, ball, referees).
- `team_assigner/`: Logic for assigning teams based on jersey colors.
- `player_ball_assigner/`: Determines which player has possession of the ball.
- `camera_movement_estimator/`: Estimates and compensates for camera movement.
- `view_transformer/`: Handles perspective transformation (pixels to meters).
- `speed_and_distance_estimator/`: Calculates physical metrics.
- `utils/`: Helper functions for video reading/saving.

---

## 🧠 Technologies Used

- **Python** 🐍
- **YOLO (You Only Look Once)** for Object Detection
- **OpenCV** for Image Processing
- **NumPy** for Numerical Operations
- **K-Means Clustering** for Color Segmentation
- **Optical Flow** for Camera Stabilization

---

## 📬 Contact

Feel free to reach out if you have any questions or want to discuss AI in Sports!

