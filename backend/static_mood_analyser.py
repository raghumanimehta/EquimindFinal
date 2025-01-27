
# Analyse mood based for the given time period
# def analyse_mood(moods: Mood[], start_date: datetime, end_date: datetime) -> Mood:

class StaticMoodAnalyser:
    def __init__(self, moods: Mood[], start_date: datetime, end_date: datetime):
        self.moods = moods.filter(lambda mood: mood.timestamp >= start_date and mood.timestamp <= end_date)
        self.start_date = start_date
        self.end_date = end_date

    # def analyse(self) -> Mood:
    #     return Mood()

    # def correlate_mood_with_stress(self) -> bool:
    #     if (self)

    def get_average_mood_Level(self) -> MoodLevel:
        return sum(mood.level for mood in self.moods) / len(self.moods)
    
    def get_average_sleep_quality(self) -> SleepQuality:
        return sum(mood.sleep_quality for mood in self.moods) / len(self.moods)
    
    def get_average_stress_level(self) -> StressLevel:
        return sum(mood.stress_level for mood in self.moods) / len(self.moods)
    
    def get_average_sleep_hours(self) -> float:
        return sum(mood.sleep_hours for mood in self.moods) / len(self.moods)

    

        
        