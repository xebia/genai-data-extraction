accident_descriptions = [
"""
A 30-year-old man was injured in a car accident. He was driving his car when another car hit him from the side. He was taken to the hospital with a broken leg. The man works as a lawyer.
""",

"""
I was walking down the street when I saw a woman fall off her bike. She was taken to the hospital with a broken arm. She was wearing a helmet, so she didn't hit her head. The accident happened on a busy street, so there were many witnesses. To make a living she works as a surgeon.
""",

"""
An earthquake hit the city, causing a building to collapse. In an office a 58-year-old employee was injured by falling debris. He got cut woundson his shoulder. His occupation is a teacher.
""",

"""
A 10-year-old boy was playing in a park when he fell from a swing. He landed awkwardly on his wrist, resulting in a fracture. He was transported to the local children's hospital for treatment. The boy is a student at the nearby elementary school.
""",

"""
A construction worker, aged 45, was injured on a building site. He was operating a forklift when it tipped over, pinning his foot. He sustained severe crush injuries and was airlifted to a regional trauma centre. He is employed as a heavy machinery operator.
""",

"""
A car accident left a 30-year-old man with a broken leg. He was hit from the side by another vehicle while driving. The man, a lawyer, was taken to the hospital.
""",

"""
While walking down a busy street, a woman fell off her bike. She suffered a broken arm. Thankfully, she was wearing a helmet. The woman, a surgeon, was taken to the hospital by ambulance.
""",

"""
Falling debris injured a 58-year-old employee during a building collapse caused by an earthquake. He sustained cut wounds on his shoulder. The man works as a teacher.
""",

"""
A fractured wrist was the result of a fall from a swing for a 10-year-old boy. He landed awkwardly while playing in a park and was transported to the local children's hospital. He is a student at the nearby elementary school.
""",

"""
Severe crush injuries to his foot required a 45-year-old construction worker to be airlifted to a regional trauma centre. The incident occurred when a forklift he was operating tipped over. He is employed as a heavy machinery operator.
""",

"""
Please find below the our accident report for the incident that occurred on 15th March 2024:

Slipping on ice while walking her dog led to a hip fracture for a 65-year-old woman. She was admitted to the hospital for surgery. She is a retired librarian.

Can we please get a settlement?
""",

"""
Burns to his hands and face resulted from a chemical spill during a laboratory experiment, injuring a 22-year-old student. He was treated in the emergency room and released.
""",

"""
Chest injuries were sustained by a 50-year-old truck driver in a multi-vehicle collision on the highway, caused by heavy fog. He was hospitalized.
""",

"""
A knee injury was suffered by a 16-year-old girl during a high school basketball game, landing awkwardly after a jump shot. She was taken to the hospital for an MRI.
""",

"""
Head trauma occurred when a 70-year-old man fell down a flight of stairs at his home. He was taken to the intensive care unit. He is a retired accountant.
""",

"""
Severe burns to his arms resulted from a pot of boiling water spilling on a 35-year-old chef working in a restaurant kitchen. He was treated at a burn center.
""",

"""
A fractured ankle was the outcome of a fall while trekking in a mountainous area for a 28-year-old hiker. She was rescued by a search and rescue team. She is a freelance graphic designer.
""",

"""
Electrocution while working on a power line caused severe burns to a 40-year-old electrician. He was hospitalized and is employed by a local utility company.
""",

"""
Puncture wounds to his leg were inflicted by a dog bite on a 12-year-old boy playing in his backyard. He was taken to the hospital for treatment and rabies shots.
""",

"""
Multiple fractures were sustained when a tractor overturned, injuring a 55-year-old farmer. He was airlifted to a regional hospital.
""",

"""
A back injury occurred when a stack of boxes fell on a 25-year-old warehouse worker. He was taken to the hospital for evaluation and works as a forklift operator.
""",

"""
A shoulder dislocation was suffered by a 19-year-old lifeguard while attempting a rescue in the ocean. He was treated at the beach first aid station.
""",

"""
A broken arm was the result of a fall from a ladder for a 60-year-old carpenter working on a home renovation project. He was taken to the hospital.
""",

"""
A concussion was sustained when a 32-year-old cyclist was hit by a car on a rural road. He was hospitalized and works as a software engineer.
""",

"""
Minor injuries were experienced by a 48-year-old pilot during a small plane crash during a training flight. He was rescued.
""",
]

import datetime
import random

def generate_eml(accident_description, index):
    """Generates an EML-formatted email from an accident description."""

    # Create some variety in sender and dates
    senders = {
        0: ("John Doe", "john.doe@example.com"),
        1: ("Jane Smith", "jane.smith@workmail.net"),
        2: ("Robert Jones", "robert.jones@company.org"),
        3: ("Emily Brown", "emily.brown@mail.com"),
        4: ("Michael Davis", "michael.davis@service.net"),
        5: ("Jessica Wilson", "jessica.wilson@pro.com"),
        6: ("David Garcia", "david.garcia@example.net"),
        7: ("Linda Rodriguez", "linda.rodriguez@workmail.com"),
        8: ("Christopher Williams", "chris.williams@company.net"),
        9: ("Angela Martinez", "angela.martinez@mail.org"),
    }
    sender_index = index % len(senders) # Cycle through senders
    sender_name, sender_email = senders[sender_index]

    # Date -  Stagger dates, go back in time from a recent date.
    base_date = datetime.datetime(2024, 3, 15, 10, 30, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-8))) # PST
    date = base_date - datetime.timedelta(days=index*2, hours=random.randint(0,23), minutes=random.randint(0, 59), seconds=random.randint(0,59))
    date_str = date.strftime("%a, %d %b %Y %H:%M:%S %z")

    # Subjects
    subjects = [
        "Insurance Claim for Accident",
        "Accident Report and Claim",
        "Urgent: Accident Claim Submission",
        "Claim for Injuries Sustained",
        "Request for Accident Settlement",
        "Formal Accident Claim",
        "Settlement Request",
        "Accident Injury Claim"
    ]
    subject = subjects[index % len(subjects)]
     # Add a bit more randomness
      # Adjust percentage of emails that go to claims department
    if random.random() < 0.8:
        recipient = "claims@superinsurance.com"
    else:
        recipient = "requests@superinsurance.com"

    # randomly pick 'Dear Insurance Corp', 'Dear reader', 'Hello' or 'Hi'
    greetings = ["Dear Insurance Corp", "Dear reader", "Hello", "Hi"]
    greeting = random.choice(greetings
    )


    eml_content = f"""From: {sender_name} <{sender_email}>
Date: {date_str}
Subject: {subject}
To: {recipient}
Content-Type: text/plain; charset="UTF-8"

{greeting},


{accident_description}

Sincerely,
{sender_name}
"""
    return eml_content


# Create and print EML files

eml_files = []
for i, desc in enumerate(accident_descriptions):
    eml = generate_eml(desc, i)
    eml_files.append(eml)
    print(eml)
    print("-" * 20)  # Separator between emails

# You can save these to .eml files:
for i, eml in enumerate(eml_files):
    with open(f"accident_report_{i+1}.eml", "w") as f:
        f.write(eml)