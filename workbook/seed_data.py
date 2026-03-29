from workbook.models import Review, ReviewQuestion

def seed():

    r1 = Review.objects.create(title="Project Review-I", semester=1, description="Problem Statement, Motivation, objectives and Literature Review")

    questions = [
        "Does the statement gives clear identification about what your project will accomplish?",
        "Is the statement short and concise? ",
        "Can a person who is not familiar with the project understand scope of the project by reading the project problem statement?",
        "The project’s objectives of study (what product, process, resource etc.) are being addressed?",
        "Is similar type of methodology / model used for existing work ?",
        "Is the studied literature sufficient to decide scope of the project?",
        "Are the objectives set will help to achieve goal of the project?",
        "Does Research gap identified will lead to find motivation of project?",
        "Does your project contribute to our society by any means and will lead to find motivation?",
        "Are the objectives clearly and unambiguously listed?",
    ]

    for q in questions:
        ReviewQuestion.objects.create(review=r1, question_text=q)

    print("Data inserted successfully!")





    r2 = Review.objects.create(title="Project Review-II", semester=1, description="Feasibility and Scope")

    questions = [
        "Is the project’s view point is understood?",			
        "Is the project goal statement is in alignment with the sponsoring organization’s business goal and mission?",
        "Who is the project’s end user?",
        "What is the projected cost of producing a product?",
        "Is project achievable in specified (Time, Cost Budget)?",
        "Are the requirements within the scope of the project?",
        "Is the scope properly defined?",
        "Does the problem statement clearly define scope of the project?",
        "Do the project requirements fit into available software and hardware?",
        "Whether the milestones are stated completely and project timeline is given?",
        "Whether risks like technical risks, Operational risks, schedule risks, business risks are identified correctly or not?",
        "Whether Risk prioritization is done properly or not and any back up plan is there or not?",
    ]

    for q in questions:
        ReviewQuestion.objects.create(review=r2, question_text=q)

    print("Data inserted successfully!")





    r3 = Review.objects.create(title="Project Review-III", semester=1, description="Requirement Analysis & Design")

    questions = [
        "Is information domain analysis complete, consistent and accurate?",
        "Is problem statement categorized in identified area and targeted towards specific area there in?",
        "Are requirement consistent with schedule, resources and budget?",
        "Are all requirements traceable to system level?",
        "What is needed to make the product?",
        "Is there a demand for the produce?",
        "Whether all requirements are captured and documented in line with scope?",
        "Whether all type of analysis classes are identified ?",
        "Are requirement reflected in the system architecture?",
        "Does the design address all the issues form the requirement?",
        "Is effective modularity achieved and modules are functionally independent?",
        "Are structural diagrams (class, Object, etc.) are well defined?",
        "Are all class associations clearly defined and understood? (Is it clear which classes provide which services? )",
        "Are the classes in the class diagram clear? (What they represent in the architecture design document?)",
        "Are the multiplicities in the use case diagram depicted in the class diagram?",
        "Are all objects used in sequence diagram?",
        "Are the symbols used in all diagrams corresponding to UML standards?",
        "Are behavioral diagrams (use case, sequence, activity, etc.) well defined and understood?",
        "Does each case have clearly defined actors and input/output?",
        "Does the sequence diagram matches with class diagram?",
        "Whether State charts are capturing system’s dynamic behavior correctly or not?",
        "Related to procedural thinking whether DFDs and CFDs along with transaction and transformation flow are done correctly or not?",
    ]

    for q in questions:
        ReviewQuestion.objects.create(review=r3, question_text=q)

    print("Data inserted successfully!")








    r4 = Review.objects.create(title="Project Review-I", semester=2, description="Modeling (Model Refinement and Algorithm development)")

    questions = [
        "Which software Development Process model is used? (Water fall, Incremental, RAD) How?(? at this level?)",
        "Do you clearly identify data objects, their attributes and relationships? (All constraints fro SRS are captured or not?)",
        "Have you clearly matched the objects with respective classes and their responsibilities?",
        "Have you analyzed the requirements and represented them into respective models ?",
        "Can you differentiate between different system states and depict them in the form of state transition diagram?",
        "Does the mathematical model clearly imply design of the project?",
        "Does the mathematical model clearly states goal of project?",
        "Does the interface between the modules properly identified ?",
        "Does any functional dependencies are identified and described?",
        "Which architectural model does your system supports?",
        "Whether Deployment diagram is inline with selected architecture?",
        "Whether all components are designed properly and represented in component diagram?",
        "Whether NP-completeness of algorithms is checked or not?",
    ]

    for q in questions:
        ReviewQuestion.objects.create(review=r4, question_text=q)

    print("Data inserted successfully!")









    r5 = Review.objects.create(title="Project Review-II", semester=2, description="Coding / Implementation")

    questions = [
        "Does the code completely and correctly implement the design?",
        "Does the code comply with the coding standard?",
        "Is the code well structured, consistent in style, and consistently formatted?",
        "Are all functions in the design coded?",
        "Does the code make use of object oriented concepts?",
        "Does the code support granularity?",
        "Does the language used for coding is correctly chosen as per the projectneed?",
        "If any off the shelf components areused, Have you understood the functionalities of using it?",
        "Are all comments consistent with the code?",
        "Whether code optimization is done properly or not? (By using language features)",
    ]

    for q in questions:
        ReviewQuestion.objects.create(review=r5, question_text=q)

    print("Data inserted successfully!")











    r6 = Review.objects.create(title="Project Review-III", semester=2, description="Validation and Testing")

    questions = [
        "Have you done alpha testing?",
        "Have you done beta testing?",
        "Have you validated the requirements, design and code as per standard?",
        "Have you performed GUI testing of project? How?",
        "Does your system comply with basic usability norms?",
        "Have you tested the code using standard datasets available in your area of project?",
        "Have you tested the code in real time environment?",
        "After integration of all components whether total performance of system is checked or not?",
        "Whether repository of all components along with versions is documented or not?",
    ]

    for q in questions:
        ReviewQuestion.objects.create(review=r6, question_text=q)

    print("Data inserted successfully!")







    r7 = Review.objects.create(title="Project Review-IV", semester=2, description="Report Writing")

    questions = [
        "Is the report written as per the prescribed format?",
        "Is the report timely prepared?",
        "Is the report properly organized, spelled, grammatically correct?",
        "Is the report plagiarism free?",
        "Is the report precise and written to the point?a",
        "Is the report contains complete results and comparative graphs?",
        "Are all figures and tables properly numbered and labeled?",
        "Are all figures and tables properly cited?",
        "Weather references are properly cited?",
    ]

    for q in questions:
        ReviewQuestion.objects.create(review=r7, question_text=q)

    print("Data inserted successfully!")
