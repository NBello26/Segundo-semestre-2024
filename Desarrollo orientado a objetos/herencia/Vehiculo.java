//Super class
public class Vehiculo {
    //Atributos
    private String id, marca;
    private double precio;

    //Contructor
    public Vehiculo(String idVehiculo, String marcaVehiculo, double precioVehiculo){
        this.id = idVehiculo;
        this.marca = marcaVehiculo;
        this.precio = precioVehiculo;
    }
    //Constructor vacío
    public Vehiculo(){
    }

    //Set
    public void setId(String id) {
        this.id = id;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }
    public void setPrecio(double precio) {
        this.precio = precio;
    }
    
    //get
    public String getId() {
        return id;
    }
    public String getMarca() {
        return marca;
    }
    public double getPrecio() {
        return precio;
    }

    //métodos especiales

    //Mostrar información
    public void mostrarInformacion(){
        System.out.println("Patente Vehículo: " + this.id);
        System.out.println("Marca Vehículo: " + this.marca);
        System.out.println("Precio Vehículo: " + this.precio);
    }

    //Calcular reparación
    public double calcularReparacion(double descuento){
        System.out.println("Calculando reparación...");
        return precio - (precio*descuento);
    }
    
    //to-string
    @Override
    public String toString() {
        return "Id Vehículo: " + this.id + "\nMarca: " + this.marca + "\nPrecio: " + precio; 
    }
}