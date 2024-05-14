import pandas as pd

df = pd.read_csv('df/leif_df.csv')
metrics = [
    # General
    'date',  # The date of the recorded data
    
    # Physical Health
    'blood_pressure',  # Blood pressure levels
    'heart_rate',   # Heart rate
    'heart_rate_variability',  # Heart Rate Variability (HRV)
    'stand_hours',  # Number of hours spent standing
    'sitting_hours',  # Number of hours spent sitting
    'steps',  # Number of steps taken
    'stairs',  # Number of stairs climbed
    'cardio',  # Duration of cardio excerise
    'strength_training',  # Duration of strength training
    'flexibility_training',  # Duration of flexibility training
    'balance_training',  # Duration of balance training
    'body_weight',  # Body weight
    'blood_glucose',  # Blood glucose levels
    'blood_oxygen',  # Blood oxygen levels
    'calories',  # Calories consumed and burned
    'hydration',  # Water intake
    'macronutrient_intake',  # Intake of proteins, fats, and carbohydrates
    'micronutrient_intake',  # Intake of vitamins and minerals
    'body_composition',  # Body fat percentage, muscle mass, etc.
    'resting_metabolic_rate',  # Basal metabolic rate
    'gut_microbiome_analysis',  # Health of gut microbiome
    'genetic_markers',  # Analysis of genetic predispositions
    'biomechanical_metrics',  # Biomechanical data like stride length, joint angles
    'epigenetic_markers',  # Track changes that may indicate aging or disease onset
    'ecg',  # Periodic electrocardiogram readings to monitor heart health
    'spirometry',  # Measure lung function
    'oxygen_saturation',  # Continuous SpO2 monitoring
    'lipid_profile',  # Regular cholesterol and triglyceride checks
    'hormone_levels',  # Including insulin, cortisol, thyroid hormones, etc.
    'dexascan_results',  # Results from DEXA scans for fat, muscle, and bone density
    'posture_analysis',  # Analysis of posture and ergonomic habits
    
    # Mental Health
    'mood',  # General mood
    'stress',  # Stress levels
    'positivity',  # Positive emotions and thoughts
    'negativity',  # Negative emotions and thoughts
    'anxiety',  # Anxiety levels
    'logical_fallacies',  # Frequency of logical fallacies in thoughts and speech
    'meditation_duration',  # Duration of meditation or mindfulness practice
    'journaling_frequency',  # Frequency of journaling
    'journaling_sentiment',  # Sentiment analysis of journaling entries
    'social_interactions_quality',  # Quality of social interactions
    'immune_function',  # Regular blood tests for white blood cell counts and other markers
    'vaccination_status',  # Ensuring up-to-date with necessary vaccines
    
    # Cognitive Function
    'focus',  # Ability to concentrate and stay focused
    'cognitive_performance',  # Cognitive performance (e.g., memory, problem-solving)
    'cognitive_load',  # Estimation of mental workload
    'thought_patterns',  # Analysis of positive vs. negative thought patterns
    'problem_solving',  # Problem-solving abilities
    
    # Sleep
    'sleep_duration',  # Total duration of sleep
    'sleep_stages_rem',  # Duration of REM sleep
    'sleep_stages_deep',  # Duration of deep sleep
    'sleep_stages_light',  # Duration of light sleep
    'sleep_quality',  # Overall quality of sleep
    
    # Environmental Factors
    'air_quality',  # Quality of the air
    'uv_index',  # UV index levels
    'temperature',  # Ambient temperature
    'humidity',  # Humidity levels
    'noise_levels',  # Ambient noise levels
    'light_exposure',  # Exposure to natural and artificial light
    'air_pollution_levels',  # Levels of air pollution (e.g., PM2.5, PM10)
    'toxin_exposure_levels',  # Biomarkers for environmental toxins
    
    # Behavioral Patterns
    'screen_time',  # Time spent using screens (e.g., phone, computer)
    'work_hours',  # Number of work hours
    'productivity_levels',  # Productivity levels
    'leisure_activities',  # Frequency and type of leisure activities
    
    # Reproductive Health (if applicable)
    'menstrual_cycle_tracking',  # Tracking of menstrual cycle
    'sexual_health_metrics',  # Sexual health metrics
    'reproductive_hormone_levels',  # Monitoring reproductive hormones
    'prostate_health',  # Regular screenings if applicable
    
    # Healthcare Interactions
    'medication_adherence',  # Adherence to medication schedules
    'doctor_visits',  # Frequency of doctor visits
    'health_checkups',  # Regular health checkups and screenings
    
    # Personal Development
    'education_activities',  # Educational pursuits and activities
    'personal_goals_progress',  # Progress towards personal goals
    'task_management',  # Efficiency in managing tasks
    'goal_setting',  # Setting and achieving goals
    'time_management',  # Efficiency in managing time
    
    # Communication and Interaction Metrics
    'conversation_length',  # Duration of conversations
    'speaking_time',  # Amount of time spent speaking vs. listening
    'speech_rate',  # Words per minute
    'emotional_tone',  # Sentiment analysis
]
