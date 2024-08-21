"""
Contexto:

Cómo desarrollador informático se espera que puedas generar soluciones a las distintas problemáticas de tus futuros clientes.
En muchas ocasiones, estos clientes son altamente exigentes y la gran mayoría de ellos espera un servicio de gran calidad.
Estos servicios pueden ser muy variados y van desde la creación de sitios web, aplicaciones web, correos electrónicos, la gestión
de redes sociales y una gran cantidad de otras soluciones que, con el paso del tiempo, cada vez van a ser más necesarias.
Se espera que en forma constante tu empresa de desarrollo de soluciones informáticas pueda estar con los más altos estándares
de calidad. La calidad es el factor decisivo entre una empresa y otra, y sobre todo, el servicio al cliente y el post venta.
Para asegurar que estos atributos se logren, se ha pedido que puedas desarrollar un sistema que identifique las solicitudes, las
registre, valide las fechas de plazo, gestione los clientes y otros asuntos más.

Lo primero es validar la identidad del usuario ingresando sus credenciales para así acceder al sistema.
A continuación, se despliega la página de inicio visualizando así las tareas.
El sistema permite crear nuevas tareas y asignarle prioridad. Además, también se puede cambiar la configuración editando así
perfiles, usuarios y también las tareas.
Puedes ver un ejemplo de este tipo de softwares en tareas.bilbaolabs.cl. Debes ingresar con las siguientes credenciales de
acceso.

Usuario: administrador | Contraseña: 123456
Debes completar la siguiente tabla para ingresar, cuáles son las entidades que tú logras reconocer y luego clasificarlas en
entidades fuertes y entidades débiles. Las 2 primeras son un ejemplo. Si encuentras mas entidades, puedes agregar mas filas a
la tabla.
"""

"""
O = obligatorio
A = opcional
# = clave primaria
U = Unico
Entidad:
    - Clientes (Fuerte)
        Atributos:
            - rut (Varchar) (O) (#) (U)
            - nombre_completo (Varchar) (O)
            - fecha_de_registro (DATE) (A)
            - correo (Varchar) (O) (U)
            - fecha_de_nacimiento (DATE) (A)
            - tipo_de_servicio (Varchar) (O)
            - genero (Varchar) (A)
            - número_de_telefono (Varchar) (O) (U)
            - dirección (Varchar) (A)
            - codigo_postal (Numerico) (A)
            - estado_del_trabajo (Varchar) (O) 
    - Servicio (Debil)
        Atributos:
            - prioridad (Varchar) (O) 
            - tipo_de_servicio (Varchar) (O)
            - fecha_de_inicio (DATE) (O)
            - fecha_de_entrega (DATE) (O)
            - iD (Numerico) (O) (U) (#)
            - solicitante (Varchar) (O) 
            - encargado (Varchar) (O)
    - Venta (Debil)
        Atributos:
            - metodo_de_pago (Varchar) (O)
            - fecha_de_pago (DATE) (O)
            - número_de_boleta (Numerico) (O) (#) (U)
            - encargado_de_la_venta (Varchar) (O)
            - tipo_de_servicio (Varchar) (O)
            - comprador (Varchar) (O)
    - Usuario (Fuerte)
        Atributos:
            - nombre_de_usuario (Varchar) (O) (U)
            - contraseña (Varchar) (O)
            - iD (Numerico) (O) (U) (#)
            - nombre_completo (Varchar) (O)
            - fecha_de_naciemiento (DATE) (O)
            - sexo (Varchar) (A)
            - correo (Varchar) (O) (U)
            - número_de_teléfono (Varchar) (O)
            - dirección (Varchar) (O)
            - codigo_postal (Numerico) (A)
            - rut (Varchar) (O) (U)
            - cargo (Varchar) (O)
    - Perfil (Debil)
        Atributos:
            - iD (Numerico) (O) (U) (#)
            - foto (A)
            - descripción (Varchar) (A)
            - nombre_completo (Varchar) (O)
            - fecha_de_nacimiento (DATE) (O)  
            - sexo (Varchar) (A)
            - correo (Varchar) (O) (U)
            - número_de_teléfono (Varchar) (O) (U)
            - dirección (Varchar) (A)
            - cargo (Varchar) (O)
"""