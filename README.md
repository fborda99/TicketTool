TICKET TOOL

    Ticket Tool is a web page that consists of the creation of tickets by employees, to be resolved by an IT team. Said tickets must consist of technological problems that the user may present for which technical assistance is required. This service can be used by companies that contract Ticket Tool as a solution to manage technological incidents.

    The project was developed by Thomas Bransburg and Florencia Borda. In general terms, Thomas developed the AppEmployees and Florencia the AppIT_Team. Then, together they created the AppTickets and AppMessages.

    Note: In order to visualize the testing documentation (Unit_Test_TicketTool.xlsx) in Visual Studio Code you will need to install the Excel Viewer Extension.

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
