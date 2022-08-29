TICKET TOOL

    Ticket Tool es una página web que consiste en la creación de tickets por parte de usuarios de Ticket Tool, para que sean resueltos por un equipo de IT. Dichos tickets deben consistir en problemas tecnológicos que pueda presentar el usuario para el que requiere asistencia técnica. Este servicio puede ser utilizado por empresas que contratan Ticket Tool como solución para gestionar incidentes tecnológicos.

CÓMO INICIAR EL PROYECTO

    Para inicializar la página, se deben seguir los siguientes pasos:
    1) Descargar el proyecto en GitHub.
    2) Abrir un entorno para poder trabajar el proyecto.
    3) Ubicarse en la carpeta del proyecto en la que se encuentra el archivo manage.py.
    4) Ejecutar el comando "python .\manage.py runserver"
    5) Hacer ctrl + click en el URL de la terminal 

CLASES

    El proyecto consiste de tres clases:
    1) Ticket: incidentes tecnológicos creados por usuarios que buscan asistencia técnica. Sus atributos son la fecha de creación, descripción, categoría y estado.
    2) User: aquellos que tienen la posibilidad de crear tickets a través de la página para reportar problemas tecnológicos. Sus atributos son nombre, apellido, email y número de legajo.
    3) Staff: miembros del equipo de IT que trabajan en la solución de los tickets creados por los usuarios. Sus atributos son nombre, apellido, email y puesto de trabajo.

VISUALES

    Al inicio de la página web se puede acceder a través del URL "/ticket/homepage/" o bien haceindo click en el botón "Ticket Tool" en la esquina superior izquierda de la pantalla. Al comienzo habrá una sección con dos botones, uno para crear y otro para buscar tickets cargados en la página. Debajo, hay tres secciones que contienen las distintas clases del proyecto, con un botón cada una que te permite visualizar listados de las bases de datos de cada una. Debajo, también se pueden ver testimonios de usuarios que utilizaron la página para la resolución de tickets. Al final, hay un formulario para ponerse en contacto con los desarrolladores de la página web.

    Para acceder a la sección de usuarios, se puede hacer click en el botón mencionado de la página de inicio o ingresando el URL "/ticket/users/". Allí se podrá ver un listado de los usuarios cargados a la base de datos. Además, hay un botón que permite crear nuevos usuarios al completar un formulario con los atributos de la clase User mencionada anteriormente y luego haciendo click en el botón que dice "Submit" (el URL correspondiente es "/ticket/createuser/").

    Por otro lado, el URL para acceder a la sección de tickets es "/ticket/tickets/" en el cual se puede ver un listado de todos los tickets creados junto a sus atributos correspondientes. Además, hay un botón que permite crear un ticket nuevo (su URL es "/ticket/createticket/") y otro que permite buscar entre los tickets ya creados ("/ticket/ticketsearch/"); en ambos casos se deben completar los formularios y luego hacer click en el botón correspondiente. El link para acceder a los resultados de la búsqueda es "/ticket/ticketsearch_results/".

    Por último, el URL para acceder a la sección del equipo de IT es "/ticket/staff/" y allí se puede visualizar un listado de los miembros del staff. Además, hay un botón que permite agregar nuevos miembros a la base de datos (su URL es "/ticket/createstaff/"), debiendo completar el formulario correspondiente y luego hacer click en submit.






