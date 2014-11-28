
class CalEvent:
    def __init__(self):
        self.start_date = None
        self.start_time = None
        self.end_date = None
        self.end_time = None
        self.title = None
        self.desc = None
        self.link = None

    def __repr__(self):
        return 'event(' + repr(self.title) + ', ' + repr(self.desc) + ', ' + repr(self.link) + ')'
