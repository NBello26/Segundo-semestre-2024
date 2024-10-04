import java.util.ArrayList;
import java.util.Scanner;

public class GymDuoc {
    //Atributos
    private ArrayList<Alumno> ListaAlumno;
    private Scanner scanner;
    
    //Constructor
    public GymDuoc(){
        this.ListaAlumno = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    //metodos

    public void agregarAlumno(){
        //pedimos los datos.
        String flag = "False";
        int id;
        do{
            System.out.println("Ingrese la ID del alumno: ");
            id = scanner.nextInt();
            scanner.nextLine();
            if(id > 0){
                System.out.println("Ingreso de id correctamente");
                flag = "true";
            }else{
                System.out.println("Ingrese un id mayor a 0");
            }
        }while (flag.equals("False"));
        System.out.println("Ingresar el nombre completo del alumno: ");
        String nombre = scanner.nextLine();
        System.out.println("Ingrese la edad: ");
        int edad = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Ingrese el tipo de membresía que tiene: ");
        String membresia = scanner.nextLine();
        Alumno alumno = new Alumno(id,nombre,edad,membresia);
        ListaAlumno.add(alumno);
        System.out.println("Alumno " + nombre + " a sido agregado exitosamente");
    }
    public void mostrarAlumnos(){
        if (ListaAlumno.isEmpty()){
            System.out.println("No hay Alumnos agregados.");
        }else{
            //Recorremos la lista y almacenamos cada Alumno en la variable AlumnoIteracion, para luego mostrarla en pantalla
            for (Alumno AlumnoIteracion : ListaAlumno){
                System.out.println(AlumnoIteracion);
            }
        }
    }
    public void actualizarAlumno(){
        System.out.println("Ingrese la ID del alumno que desea actualizar: ");
        int id = scanner.nextInt();
        scanner.nextLine();
        if (ListaAlumno.isEmpty()){
            System.out.println("No hay Alumnos agregados.");
        }else{
            //Recorremos la lista y almacenamos cada Alumno en la variable AlumnoIteracion, para luego mostrarla en pantalla
            for (Alumno AlumnoIteracion : ListaAlumno){
                if (AlumnoIteracion.getId() == id){
                    System.out.println("Ingresar el nombre completo del alumno: ");
                    String nombre = scanner.nextLine();
                    System.out.println("Ingrese la edad: ");
                    int edad = scanner.nextInt();
                    scanner.nextLine();
                    System.out.println("Ingrese el tipo de membresía que tiene: ");
                    String membresia = scanner.nextLine();
                    AlumnoIteracion.setNombre(nombre);
                    AlumnoIteracion.setEdad(edad);
                    AlumnoIteracion.setMembresia(membresia);
                    System.out.println("Alumno " + nombre + " a sido actualizado exitosamente");
                    return;
                }
            }
        }
    }
}
