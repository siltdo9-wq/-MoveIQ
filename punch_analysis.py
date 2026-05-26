import numpy as np
from scipy import signal

class PunchAnalyzer:
    def __init__(self):
        self.punch_threshold = 0.5
        self.speed_threshold = 30  # pixels per frame
        
    def calculate_punch_speed(self, landmarks_sequence):
        """Calcule la vitesse des coups"""
        punches = []
        
        # Points clés des poings (MediaPipe)
        left_wrist = 15
        right_wrist = 16
        left_shoulder = 11
        right_shoulder = 12
        
        for i in range(1, len(landmarks_sequence)):
            prev = landmarks_sequence[i-1]
            curr = landmarks_sequence[i]
            
            if prev and curr:
                # Vitesse du poing droit
                right_speed = self._calculate_distance(
                    prev[right_wrist], 
                    curr[right_wrist]
                )
                
                # Vitesse du poing gauche
                left_speed = self._calculate_distance(
                    prev[left_wrist], 
                    curr[left_wrist]
                )
                
                if right_speed > self.speed_threshold:
                    punches.append({
                        'type': 'right',
                        'speed': right_speed,
                        'frame': i,
                        'power': self._estimate_power(right_speed)
                    })
                
                if left_speed > self.speed_threshold:
                    punches.append({
                        'type': 'left',
                        'speed': left_speed,
                        'frame': i,
                        'power': self._estimate_power(left_speed)
                    })
        
        return pun
