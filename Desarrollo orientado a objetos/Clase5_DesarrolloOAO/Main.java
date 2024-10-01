import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        //Crear una instancia Tienda para poder trabajar con sus metodos
        Tienda tienda = new Tienda();
        Scanner scanner = new Scanner(System.in);
        //Crear una variable para almacenar opciones
        String opcion;
        do{
            System.out.println("\n*** Menú de la tienda ***");
            System.out.println("1.- Agregar producto.");
            System.out.println("2.- Mostrar productos.");
            System.out.println("3.- Actualizar producto.");
            System.out.println("4.- Eliminar producto.");
            System.out.println("5.- Salir del programa.");
            System.out.println("Selecciona una opción: ");
            opcion = scanner.nextLine();
            switch (opcion) {
                case "1":
                    System.out.println("\nAgregando un producto...");
                    tienda.agregarProducto();
                    break;
                case "2":
                    System.out.println("\nMostrando productos...");
                    tienda.mostrarProducto();
                    break;
                case "3":
                    System.out.println("\nActualizando un producto...");
                    tienda.actualizarProducto();
                    break;
                case "4":
                    System.out.println("\nEliminando un producto...");
                    tienda.eliminarProducto();
                case "5":
                    System.out.println("\nSaliendo del programa....");
                    return;
                default:
                    System.out.println("Ingrese una opción valida.");
                    break;
            }
        }while(opcion != "5");
    }
}
