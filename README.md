TICKET TOOL

    Ticket Tool is a web page that consists of the creation of tickets by employees, to be resolved by an IT team. Said tickets must consist of technological problems that the user may present for which technical assistance is required. This service can be used by companies that contract Ticket Tool as a solution to manage technological incidents.

    The project was developed by Thomas Bransburg and Florencia Borda. In general terms, Thomas developed the AppEmployees and Florencia the AppIT_Team. Then, together they created the AppTickets, AppMessages and the all the necessary docuementation.
    
UNIT TEST

    In order to visualize the testing documentation (Unit_Test_TicketTool.xlsx) in Visual Studio Code you will need to install the Excel Viewer Extension.

DEMO VIDEO

    Link to a video demonstrating how the website works: https://drive.google.com/file/d/1z4Ib_ZFwKIoKyEQ6ISE2UQCIBbyHDKDo/view?usp=sharing

HOW TO START THE PROJECT

    To initialize the page, the following steps must be followed:
        1) Download the project on GitHub.
        2) Open an environment to be able to work on the project.
        3) Go to the project folder where the manage.py file is located.
        4) Run the command "python .\manage.py runserver"
        5) ctrl + click on the URL of the terminal.

CLASSES

    1) Ticket: technological incidents created by users seeking technical assistance. Its attributes are the creation date, description, category and status.

    2) Employee: those who have the possibility of creating tickets through the page to report technological problems. Its attributes are name, lastname, email and workid. It's related to an Avatar class.
    
    3) IT_Member: Members of the IT team who work on the solution of the tickets created by the users. Its attributes are name, lastname, email and job title. It's related to an Avatar class.

    4) Message: communications between the employees and the IT Team. Its attributes are the message, sender and date.
    
USERS VS DATABASE REGISTER

    Before running the project, it is important to understand the differences between the users and the registers from the database. 
    
    On one side, you need to login the website using and user (which is related to the model User). The difference between the IT and Employee Users is the is_staff attribute: it is True for the IT Users and False for the Employee Users. This information is stored in the auth_user table from db.sqlite3.
    
    On the other side, once the user has logged in the website, there are List Views (one for AppIT_Team and other one for AppEmployees) that show the list of registers of the corresponding database. Therefore, it is not directly related to the Users mentioned in the previous paragraph. There are bottons to add, update and remove the registers from the database (which modifies the AppEmployees_employees and AppIT_Team_it_member tables from db.sqlite3, but those changes would not impact in  the auth_user table from db.sqlite3).

VIEWS
    
    If you log in as an Employee User, you will be able to visualize the views mentioned in the AppEmployees. There, the user can visualize the Employees List with a ListView and also DetailView; and can update or delete registers from the list. In addition, the user can see, search, update and create tickets, as well as they can see, search and send messages. Finally, the user can visualize its profile, being able to update the email, password and upload an avatar.
    
    If you log in as an IT User, you will be able to visualize the views mentioned in the AppIT_Team. There, the user can visualize the IT Team Members List with a ListView and also DetailView; and can update or delete registers from the list. In addition, the user can see, search and update tickets, as well as they can see, search and send messages. Finally, the user can visualize its profile, being able to update the email, password and upload an avatar.
   
 HOW TO CREATE AN IT USER
    
    1. Open the Python Shell.
    2. Locate at the same level as the "manage.py" file. This can be verified by writting the command "ls".
    3. Run the command "python .\manage.py createsupueruser".
    4. Input a username, email (optional) and password.
    5. Superuser will be successfully created. Once the superuser is created, you can log in as an IT User.
    
