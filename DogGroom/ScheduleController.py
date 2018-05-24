import re
from .models import *
from .const import *
from datetime import *

class ScheduleController:

    def __init__(self):
        self.defaultslots = daytime_slots
        
    def add15(self, timestr):
        
        hour = int(timestr[:2])
        minute = int(timestr[3:])
        t = datetime(1, 1, 1, hour, minute, 0, 0)
        t += timedelta(minutes = 15)
        return re.search(r'\d{2}:\d{2}' , str(t)).group()

    def augment_used_slot(self, used_slots, aug_n):
        augment = []
        for e in used_slots:
            more_used_slots = [e]
            for i in range(1, aug_n):
                more_used_slots.append(self.add15(more_used_slots[-1]))
            augment = augment + more_used_slots
        return sorted(list(set(augment)))

    def get_availableslot(self, thedate):
        result = []

        appts = Appointment.objects.filter(date = thedate)   
        used_slots = [appt.starttime for appt in appts]
        if used_slots == []:
            newslots = self.defaultslots
        else:
            augment_used_slots = self.augment_used_slot(used_slots, 6)
            newslots = [slot for slot in self.defaultslots if slot not in augment_used_slots]
        
        
        for start in range(len(newslots)):
            end = start + 6
            if end >= len(newslots):
                break
            else:
                tmpslots = newslots[start : end]
                if self.is_continuousslots(tmpslots, 6):
                    result.append(newslots[start])
        return result

    def is_continuousslots(self, slots, continuity):
        base = slots[0]
        idealslots = [base]
        for i in range(1, continuity):
            idealslots.append(self.add15(idealslots[-1]))
        
        if slots == idealslots:
            return True
        else:
            return False
