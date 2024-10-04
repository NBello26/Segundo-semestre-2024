import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String opcion = "";
        GymDuoc gym = new GymDuoc();
        Scanner scanner = new Scanner(System.in);
        do{
            System.out.println("");
            System.out.println("*** Bienvenido al GymDUOC ***");
            System.out.println("1.- Ingresar alumno");
            System.out.println("2.- Mostrar alumnos");
            System.out.println("3.- Actualizar alumno");
            System.out.println("4.- Eliminar alumno");
            System.out.println("5.- Salir");
            System.out.println("Ingrese la opción que desea: ");
            opcion = scanner.nextLine();
            switch (opcion) {
                case "1":
                    System.out.println("");
                    System.out.println("Agregando alumno...");
                    gym.agregarAlumno();
                    break;
                case "2":
                    System.out.println("");
                    System.out.println("Mostrando alumnos...");
                    gym.mostrarAlumnos();
                    break;
                case "3":
                    System.out.println("");
                    System.out.println("Actualizar alumno");
                case "5":
                    System.out.println("");
                    System.out.println("Saliendo del sistema...");
                    return;
                default:
                    System.out.println("Ingresar una opción valida.");
                    break;
            }
        } while (opcion != "5");
    }
}
