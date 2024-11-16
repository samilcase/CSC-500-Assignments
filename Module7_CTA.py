room_numbers = {
    "CSC101":3004,
    "CSC102":4501,
    "CSC103":6755,
    "NET110":1244,
    "COM241":1411
}

instructors = {
    "CSC101":'Haynes',
    "CSC102":'Alvardo',
    "CSC103":'Rich',
    "NET110":'Burke',
    "COM241":'Lee'
}

meeting_times = {
    "CSC101":'8:00 a.m.',
    "CSC102":'9:00 a.m.',
    "CSC103":'10:00 a.m.',
    "NET110":'11:00 a.m.',
    "COM241":'1:00 p.m.'
}


user_input = input("Enter a course number ('q' to quit): ")

while user_input != 'q':
    try:
        print('Room Number: ',room_numbers[user_input])
        print('Instructor: ',instructors[user_input])
        print('Meeting Time: ',meeting_times[user_input])
        user_input = input("\nEnter a course number ('q' to quit): ")
    except:
        print('Class not found.')
        user_input = input("\nEnter a course number ('q' to quit): ")
