"""
Asistencia = 75% o superior
Parcial 1 -> Construcción de MER (Modelo Entidad - Relación) (11 y 12 de Septiembre) (30%)
Parcial 2 -> Construcción de MER Normalizado, Modelo Relacional e informes interactivos con formulario en Oracle APEX (23 Y 24 de Octubre) (40%)
Parcial 3 -> Consultas SQL y creación de Dashboard (4 y 5 de Diciembre) (30%) 
"""

"""
Base de datos: Una base de datos es una herramienta para recopilar y organizar información.
Servidores: Conjunto de computadoras capaces de atender las peticiones de un cliente y devolverle una respuesta en concordancia.
Dato: Representación simbólica de un atributo o variable cuantitativa o cualitativa.
Información: Conjunto organizado de datos relevantes para uno o más sujetos que extraen de él un conocimiento.
SGBD (Sistema Gestor de Base de Datos): Permite la comunicación con la Base de Datos (Algunos ejemplos serian MySQL, PostgreSQL, ORACLE, SQLServer, etc).
Permite:
Definición:
- Creación de objetos (CREATE).
- Modificación de estructura (ALTER).
- Eliminación de objetos (DROP) o eliminación de todos los registros de la tabla (TRUNCATE).
Manipulación:
- Visualizar datos (SELECT).
- Registrar datos (INSERT).
- Actualizar datos (UPDATE) o eliminar registros de una tabla (DELETE).
Control de datos:
- GRANT que entrega permisos a los usuarios sobre los objetos de la base de datos.
- REVOKE que quita esos permisos.
Control de Transacciones:
- COMMIT que permite confirmar cambios
- ROLLBACK que permite deshacer tareas realizadas.

Abstracción de datos: Técnica que consiste en representar las características esenciales de una estructura de datos. 
Entidad: Una cosa, objeto o concepto del mundo real con existencia independiente, es decir, se diferencia únicamente de otro objeto o cosa, incluso 
siendo del mismo tipo, o una misma entidad.
    Entidad fuerte: La entidad posee atributos claves propios que permitan identificar en forma única cada Instancia de la Entidad.
                    La Entidad existe en el modelo sin depender de la existencia de otra.
    Entidad debil: Cada Instancia de la Entidad depende de la existencia de una Instancia de otra Entidad que es Fuerte (acá no surgen una Relación con Identificación).
            Por existencia: Cuando en una relación débil no depende por identificación, siempre será débil por existencia, ya que no puede existir la débil si no existe la fuerte.
                            Ejemplo: Artista - Discográfica
            Por identificación: Esto sucede cuando la entidad débil no es capaz de identificar un registro con sus propios atributos 
                                y necesita complementarlo con la clave principal de la entidades fuerte.
                                Ejemplo: Libro - Copia

Tarea: Definir atributos para la entidad "Cliente" y seleccionar que tipo de atributo es (Numerico, VARCHAR2, DATE)
"""