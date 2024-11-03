"""
 Write a Python program that declares a
 class describing your favorite animal.
 Have the data members of the class
 represent the following physical
 parameters of the animal: length of the
 arms (float), length of the legs (float),
 number of eyes (int), does it have a tail?
 (bool), is it furry? (bool). Write an
 initialization function that sets the
 values of the data members when an
 instance of the class is created.
 Write a member function of the class
 to print out and describe the data
 members representing the physical
 characteristics of the animal.
"""

class belted_galloway:
    
    def __init__(self, arm_length, leg_length,
                eye_count, has_tail, is_furry):
        self.arm_length = arm_length       
        self.leg_length = leg_length       
        self.eye_count = eye_count         
        self.has_tail = has_tail           
        self.is_furry = is_furry           
        
    def describe(self):
        print("Belted Galloway Cow Characteristics:")
        print(f"Length of Arms: {self.arm_length} feet")
        print(f"Length of Legs: {self.leg_length} feet")
        print(f"Number of Eyes: {self.eye_count}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")
   
        
cow = belted_galloway(arm_length=1.2, leg_length=1.5, eye_count=2, has_tail=True, is_furry=True)
cow.describe()