import java.util.ArrayList;
import java.util.Scanner;

public class Tienda {
    //Atributos
    private ArrayList<Producto> ListaProductos;
    private Scanner scanner;
    
    //Constructor
    public Tienda(){
        this.ListaProductos = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    //Método para agregar productos C
    public void agregarProducto(){
        //id,nombre,precio

        System.out.println("Ingresa el ID del producto: ");
        int id = scanner.nextInt();
        scanner.nextLine();//Eliminar el buffer

        System.out.println("Ingresa el nombre del producto: ");
        String nombre = scanner.nextLine();

        System.out.println("Ingresa el precio del producto: ");
        double precio = scanner.nextDouble();

        //Crear un nuevo producto y añadirlo a la lista
        Producto producto = new Producto(id, nombre, precio);
        ListaProductos.add(producto);
    }
    //Método para listar o mostrar productos R 
    public void mostrarProducto(){
        if (ListaProductos.isEmpty()){
            System.out.println("No hay productos agregados.");
        }else{
            //Recorremos la lista y almacenamos cada producto en la variable productoIteracion, para luego mostrarla en pantalla
            for (Producto productoIteracion : ListaProductos){
                System.out.println(productoIteracion);
            }
        }
    }
    //Método para actualizar productos U
    public void actualizarProducto(){
        //Solicito el id del producto que quiere actualizar
        System.out.println("Ingresa la ID del producto a actualizar");
        int id = scanner.nextInt();
        scanner.nextLine();

        //Recorro la lista buscando el id coincidente
        for (Producto producto : ListaProductos){
            if (producto.getIdProducto() == id) {
                System.out.println("Ingresa un nuevo nombre: ");
                String newnombre = scanner.nextLine();
                System.out.println("Ingrese el nuevo precio: ");
                double newprecio = scanner.nextDouble();
                scanner.nextLine();

                //Actualizo los nuevos datos
                producto.setNombreProducto(newnombre);
                producto.setPrecioProducto(newprecio);
                System.out.println("El producto " + producto.getNombreProducto() + " ha sido agregado correctamente.");
                return;
            }System.out.println("El producto con esa id no se encuentra agregado.");
            
        }
    } 
    //Método para eliminar productos D
    public void eliminarProducto (){
        System.out.println("Ingresa la ID del producto a actualizar");
        int id = scanner.nextInt();
        scanner.nextLine();
        //variable
        Producto productoAEliminar = null;
        for (Producto producto : ListaProductos){
            if(producto.getIdProducto() == id){
                productoAEliminar = producto;
                break; //Una vez encontrado el producto no es necesario seguir iterando en el for 
            }
        }
        //Elimino el producto
        if (productoAEliminar != null){
            ListaProductos.remove(productoAEliminar);
            System.out.println("El producto " + productoAEliminar.getNombreProducto() + " fue eliminado correctamente.");
        }else{
            System.out.println("El producto no fue encontrado.");
        }
    }
}
