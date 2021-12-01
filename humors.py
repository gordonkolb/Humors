class Humors:
    def __init__(self):
        self.BlackBileSymptoms = {"Moody", "Anxious", "Rigid"}
        self.PhlegmSymptoms = {"Passive", "Careful", "Thoughtful"}
        self.BloodSymptoms = {"Sociable", "Outgoing", "Talkative"}
        self.YellowBileSymptoms = {"Touchy", "Restless", "Aggressive"}
        
        self.symptoms = []    # creates a new empty list for each dog

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

    def print_symptoms(self):
        for x in self.symptoms:
            print(x)
