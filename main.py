from Hospital import Hospital
from Doctor import Cardiologist, Pediatrician, Neurologist
from Patient import Patient

patients = []

a = 1

while a == 1:
    print("****** SDU HOSPITAL MANAGEMENT SYSTEM *********")
    print("Press '1' for Hospital details")
    print("Press '2' for Doctor details")
    print("Press '3' for Patient Entry")
    print("Press '4' for patient details")
    print("Press '5' to Exit")

    try:
        num = int(input("Enter your number: "))

        #showing hospital details
        if num == 1:
            print("___******____")
            obj = Hospital('SDU', 'Kaskelen', '7:00am', '11:00pm')
            obj.display()

        # Showing doctor that work in hospital
        elif num == 2:
            print(" **There are three types of Doctors here**")
            print("1: Cardiologist")
            print("2: Pediatrician")
            print("3: Neurologist")
            num_doc = int(input("Enter your number for any doctor details: "))

            # Showing details of Cardiologist Doctor
            if num_doc == 1:
                print("_*******_")
                obj = Cardiologist("01", "Dr.Zaki", "Monday - Friday, 8AM - 5PM")
                obj.display()
                obj.working()

            # Showing details of Cardiologist Doctor
            elif num_doc == 2:
                print("_*******_")
                obj = Pediatrician("02", "Dr.Yasser", "Tuesday - Sunday, 9AM - 7PM")
                obj.display()
                obj.working()

            # Showing details of Cardiologist Doctor
            elif num_doc == 3:
                print("_*******_")
                obj = Neurologist("03", "Dr.Kahfi", "Friday - Sunday, 6AM - 9PM")
                obj.display()
                obj.working()

        # Showing doctor that available
        elif num == 3:
            print(" **There are three types of Doctors here**")
            print("1: Cardiologist")
            print("2: Pediatrician")
            print("3: Neurologist")
            doctor_specialist = int(input("Enter your number for any doctor details: "))
            print("____PATIENT ENTRY______")

            # Making appointment for Cardiologist doctor based on schedule
            if doctor_specialist == 1:
                doctor_specialist = "Cardiologist"
                doctor_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
                doctor_time = ("8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM")

                try:
                    name = input("Enter patient name: ")
                    day = input("Enter your Appointment day (e.g., Monday - Friday): ")

                    while day not in doctor_days:
                        print("Doctor not available on that day.")
                        day = input("Enter your Appointment day (e.g., Monday - Friday): ")

                    print("Doctor is available on", day)

                    time = input("Enter your Appointment time (e.g., 8AM - 5PM): ")

                    while time not in doctor_time:
                        print("Doctor not available at that time.")
                        time = input("Enter your Appointment time (e.g., 8AM - 5PM): ")

                    if any(patient.day == day and patient.time == time for patient in patients):
                        print("Sorry, there is already an appointment scheduled at that time.")
                    else:
                        obj = Patient(name, doctor_specialist, day, time)
                        patients.append(obj)
                        print("Patient details entered.")

                except Exception as e:
                    print("Error occurred:", e)

            # Making appointment for Pediatrician doctor based on schedule
            elif doctor_specialist == 2:
                doctor_specialist = "Pediatrician"
                doctor_days = ("Tuesday", "Wednesday", "Thursday", "Friday", "Sunday")
                doctor_time = ("9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM", "7PM")

                try:
                    name = input("Enter patient name: ")
                    day = input("Enter your Appointment day (e.g., Tuesday - Sunday): ")

                    while day not in doctor_days:
                        print("Doctor not available on that day.")
                        day = input("Enter your Appointment day (e.g., Tuesday - Sunday): ")

                    print("Doctor is available on", day)

                    time = input("Enter your Appointment time (e.g., 9AM - 7PM): ")

                    while time not in doctor_time:
                        print("Doctor not available at that time.")
                        time = input("Enter your Appointment time (e.g., 9AM - 7PM): ")

                    if any(patient.day == day and patient.time == time for patient in patients):
                        print("Sorry, there is already an appointment scheduled at that time.")
                    else:
                        obj = Patient(name, doctor_specialist, day, time)
                        patients.append(obj)
                        print("Patient details entered.")

                except Exception as e:
                    print("Error occurred:", e)

            # Making appointment for Neurologist doctor based on schedule
            elif doctor_specialist == 3:
                doctor_specialist = "Neurologist"
                doctor_days = ("Friday", "Saturday", "Sunday")
                doctor_time = ("6AM", "7AM", "8AM", "9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM",
                               "6PM", "7PM", "8PM", "9PM")

                try:
                    name = input("Enter patient name: ")
                    day = input("Enter your Appointment day (e.g., Friday - Sunday): ")

                    while day not in doctor_days:
                        print("Doctor not available on that day.")
                        day = input("Enter your Appointment day (e.g., Friday - Sunday): ")

                    print("Doctor is available on", day)

                    time = input("Enter your Appointment time (e.g., 6AM - 9PM): ")

                    while time not in doctor_time:
                        print("Doctor not available at that time.")
                        time = input("Enter your Appointment time (e.g., 6AM - 9PM): ")

                    if any(patient.day == day and patient.time == time for patient in patients):
                        print("Sorry, there is already an appointment scheduled at that time.")
                    else:
                        obj = Patient(name, doctor_specialist, day, time)
                        patients.append(obj)
                        print("Patient details entered.")


                except Exception as e:
                    print("Error occurred:", e)

        # Showing all the patient details that have been add
        elif num == 4:
            print("____PATIENT DETAILS______")
            for patient in patients:
                print("Patient name:      ", patient.name)
                print("To          :      ", patient.doctor_specialist)
                print("Day         :      ", patient.day)
                print("Time        :      ", patient.time)

        # Exiting main menu
        elif num == 5:
            print("___******____")
            print("Thanks for visiting.")
            a = 0
        else:
            print("Invalid Input. try again")
    except ValueError:
            print("Invalid Input. Please enter a number.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Clear the input buffer
        try:
            input("Press Enter to continue...")
        except:
            pass  # If user sends EOF (Ctrl+D), just continue without clearing buffer
