
class Observer_progress():
    progress_phrase = {10 : "Setupping Target and Filters",
                       20 : "Setupping Scanner",
                       30 : "Scanner Start, scanning single ports. Wait...",
                       70 : "Scanner Completed...",
                       90 : "Parsing results...",
                       100 : "Completed"
                       }

    def __init__(self):
        self.percent = 0

    def update(self, percent):
        self.percent = percent