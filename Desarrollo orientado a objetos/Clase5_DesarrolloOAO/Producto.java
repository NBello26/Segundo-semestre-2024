//Definir la clase producto

public class Producto {
    //Definir atributos
    private int idProducto;
    private String nombreProducto;
    private double precioProducto;

    //Métodos

    //Constructor
    public Producto (int producto, String nombre, double precio){
        this.idProducto = producto;
        this.nombreProducto = nombre;
        this.precioProducto = precio;
    }
    //Constructor vacío
    public Producto (){
    }

    //Setters
    public void setIdProducto(int idProducto) {
        this.idProducto = idProducto;
    }
    public void setNombreProducto(String nombreProducto) {
        this.nombreProducto = nombreProducto;
    }
    public void setPrecioProducto(double precioProducto) {
        this.precioProducto = precioProducto;
    }

    //Getters
    public int getIdProducto() {
        return idProducto;
    }
    public String getNombreProducto() {
        return nombreProducto;
    }
    public double getPrecioProducto() {
        return precioProducto;
    }

    //Métodos especiales


    //To string
    @Override
    public String toString() {
        return "Id producto: " + idProducto + "\nNombre producto: " + nombreProducto + "\nPrecio: " + precioProducto;
    }
}