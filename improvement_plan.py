class ImprovementPlan:
    def __init__(self, assessment_scores):
        self.scores = assessment_scores
        self.recommendations = []
    
    def generate_plan(self):
        """Génère un plan d'amélioration personnalisé"""
        plan = {
            'critical': [],
            'important': [],
            'nice_to_have': []
        }
        
        # Analyse chaque compétence
        for skill, score in self.scores.items():
            if skill == 'stance' and score < 70:
                plan['critical'].append({
                    'skill': 'Stance',
                    'current_score': score,
                    'target_score': 90,
                    'exercises': [
                        {
                            'name': 'Position de combat',
                            'duration': '5 minutes',
                            'description': 'Pratiquez la position pieds écartés à largeur des épaules, corps de face ou légèrement de côté.',
                            'frequency': '5x par semaine'
                        },
                        {
                            'name': 'Déplacements latéraux',
                            'duration': '10 minutes',
                            'description': 'Marchez latéralement en maintenant votre garde, en pivotant sur les orteils.',
                            'frequency': '4x par semaine'
                        }
                    ]
                })
            
            if skill == 'punch_accuracy' and score < 65:
                plan['critical'].append({
                    'skill': 'Précision des coups',
                    'current_score': score,
                    'target_score': 85,
                    'exercises': [
                        {
                            'name': 'Travail de cible',
                            'duration': '15 minutes',
                            'description': 'Frappez des sacs de frappe avec des zones cibles marquées.',
                            'frequency': '5x par semaine'
                        },
                        {
                            'name': 'Combinaisons répétitives',
                            'duration': '10 minutes',
                            'description': 'Pratiquez les mêmes combinaisons jusqu\'à la maîtrise.',
                            'frequency': '4x par semaine'
                        }
                    ]
                })
            
            if skill == 'defense' and score < 60:
                plan['important'].append({
                    'skill': 'Défense',
                    'current_score': score,
                    'target_score': 80,
                    'exercises': [
                        {
                            'name': 'Slip (esquive)',
                            'duration': '10 minutes',
                            'description': 'Pratiquez les mouvements de tête pour esquiver les coups.',
                            'frequency': '4x par semaine'
                        },
                        {
                            'name': 'Blocage et parade',
                            'duration': '15 minutes',
                            'description': 'Travaillez avec un partenaire pour bloquer les coups entrants.',
                            'frequency': '3x par semaine'
                        }
                    ]
                })
            
            if skill == 'speed' and score < 70:
                plan['important'].append({
                    'skill': 'Vitesse',
                    'current_score': score,
                    'target_score': 85,
                    'exercises': [
                        {
                            'name': 'Exercices de vitesse des pieds',
                            'duration': '10 minutes',
                            'description': 'Sauts à la corde et exercices d\'agilité.',
                            'frequency': '5x par semaine'
                        },
                        {
                            'name': 'Combinaisons rapides',
                            'duration': '10 minutes',
                            'description': 'Lancez les coups aussi vite que possible tout en gardant le contrôle.',
                            'frequency': '4x par semaine'
                        }
                    ]
                })
            
            if skill == 'footwork' and score < 65:
                plan['important'].append({
                    'skill': 'Techniques des pieds',
                    'current_score': score,
                    'target_score': 85,
                    'exercises': [
                        {
                            'name': 'Exercices d\'agilité',
                            'duration': '15 minutes',
                            'description': 'Cones, echelle de vitesse, mouvements circulaires.',
                            'frequency': '4x par semaine'
                        },
                        {
                            'name': 'Pivot et rotation',
                            'duration': '10 minutes',
                            'description': 'Pratiquez les pivots corrects pour les coups.',
                            'frequency': '4x par semaine'
                        }
                    ]
                })
            
            if skill == 'endurance' and score < 70:
                plan['nice_to_have'].append({
                    'skill': 'Endurance',
                    'current_score': score,
                    'target_score': 85,
                    'exercises': [
                        {
                            'name': 'Cardio régulier',
                            'duration': '20-30 minutes',
                            'description': 'Course, vélo ou saut à la corde.',
                            'frequency': '4x par semaine'
                        },
                        {
                            'name': 'Assauts prolongés',
                            'duration': '20 minutes',
                            'description': 'Pratiquez le combat à rythme soutenu.',
                            'frequency': '2x par semaine'
                        }
                    ]
                })
        
        return plan
    
    def get_timeline(self):
        """Estime la durée pour atteindre les objectifs"""
        return {
            'critical_improvements': '4-6 semaines',
            'important_improvements': '6-8 semaines',
            'full_development': '12-16 semaines'
        }
