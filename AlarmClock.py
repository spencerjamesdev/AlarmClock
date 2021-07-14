class Alarm_clock_class:
    
    def __Init__(self):
        self.current_time = "5:00 pm"
        self.on_or_off = bool
        self.alarm_time = "7:00 am"

    def change_current_time(self):
        self.current_time = input("Enter the current time:")
        print("Current time: ", self.current_time)

    def toggle_alarm(self):
        user_input = input("Turn on alarm? Type 'yes' or 'no':")
        if(user_input == "yes"):
            self.on_or_off = True
        elif(user_input == "no"):
            self.on_or_off = False

    def set_alarm_time(self):
        self.alarm_time = input("Enter the time you would like to set your alarm to:")
        print("Alarm time: ", self.alarm_time)