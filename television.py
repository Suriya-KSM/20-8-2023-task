# creating television class
class televison:
    
    #constructor for the class
    def __init__(self, channel, brand, volume, tv_is_on):

        self.channel=channel
        self.brand=brand
        self.volume=volume
        self.tv_is_on=tv_is_on

    #Power on function
    def power_on(self):
        if self.tv_is_on==True:
            print("\n",self.brand, ' at Channel ', self.channel,' Volume ', self.volume)
    
    #Power off function
    def power_off(self):
        print("TV has been turned OFF.")
        quit()

    #current channel function
    def get_channel(self):
        print("\nCurrent Channel ", self.channel)
        return self.channel
    
    #Changing channel function
    def set_channel(self):
        if self.tv_is_on==True:
            channel=int(input("\nEnter the channel number you want to switch to "))
            if channel <= 50 and channel > 0:
                self.channel=channel
                print('\n',self.brand, ' at Channel ', self.channel,' Volume ', self.volume)
            else:
                print ("\nEntered Channel not found Redirecting to channel", self.channel)
        elif self.tv_is_on==False:
            print("TV has been turned OFF.")

    #Increase volume function
    def increase_volume(self):
        if self.tv_is_on==True:
            if self.volume>=0 and self.volume<100:
                self.volume+=5
                print('\n',self.brand, ' at Channel ', self.channel,' Volume ', self.volume)
            else:
                print("Maximum volume has been reached", self.volume)
        elif self.tv_is_on==False:
            print("TV has been turned OFF.")

    #Decrease volume function
    def decrease_volume(self):
        if self.tv_is_on==True:
            if self.volume>0 and self.volume<=100:
                self.volume-=5
                print('\n',self.brand, ' at Channel ', self.channel,' Volume ', self.volume)
            else:
                print("Minimum volume has been reached ", self.volume)
        elif self.tv_is_on==False:
            print("TV has been turned OFF.")


#Getting input from the user to turn on tv
Turn_on = int(input("Press 1 to turn ON:"))

#creating Object for the class
tv=televison(1,"Samsung",int(50),True)

#creating buttons and assingning relevant function to it
if Turn_on==1:
    tv.power_on()
    while Turn_on !=0:
        choice=int(input("""\n1-Turn off TV \n2-Change channel \n3-raise volume \n4-lower volume \nPress any button: """))
        if choice==1:
            tv.power_off()
        elif choice==2:
            tv.get_channel()
            tv.set_channel()
        elif choice==3:
            tv.increase_volume()
        elif choice==4:
            tv.decrease_volume()
        else:
            print("Press valid Number")
else:
   print("You have to turn on TV first")
