import mediapipe as mp
import cv2
import numpy as np

class PoseDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
    
    def detect_pose(self, frame):
        """Détecte la pose du boxeur dans une frame"""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(frame_rgb)
        return results
    
    def get_landmarks(self, results):
        """Extrait les coordonnées des points clés"""
        if results.pose_landmarks:
            landmarks = {}
            for idx, lm in enumerate(results.pose_landmarks.landmark):
                landmarks[idx] = {
                    'x': lm.x,
                    'y': lm.y,
                    'z': lm.z,
                    'visibility': lm.visibility
                }
            return landmarks
        return None
    
    def draw_pose(self, frame, results):
        """Dessine les points de pose sur la frame"""
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )
        return frame
