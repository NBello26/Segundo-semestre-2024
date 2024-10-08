import java.util.ArrayList;
public class Reparacion {
    //Atributos
    private ArrayList<Vehiculo> listaVehiculos;
    private double total;

    //Constructor
    public Reparacion(){
        this.listaVehiculos = new ArrayList<>();
        this.total = 0;
    }

    //set
    public void setListaVehiculos(ArrayList<Vehiculo> listaVehiculos) {
        this.listaVehiculos = listaVehiculos;
    }
    public void setTotal(double total) {
        this.total = total;
    }

    //get
    public ArrayList<Vehiculo> getListaVehiculos() {
        return listaVehiculos;
    }
    public double getTotal() {
        return total;
    }

    //Metodos especiales

    //Calcular total de reparación
    public double calcularTotal(){
        return total;
    }
    //Agregar vehículo a la reparación
    public void agregarVehiculo(Vehiculo vehiculo){
        listaVehiculos.add(vehiculo);
        total += vehiculo.calcularReparacion(0.1);
    }
    //Mostar info
    public void mostrarInformacion(){
        int contador = 1;
        if(listaVehiculos.isEmpty()){
            System.out.println("No existen vehiculos");
        }else{
            for(Vehiculo vehiculo : listaVehiculos){
                System.out.println("");
                System.out.println(contador + ".- Vehículo en reparación: ");
                vehiculo.mostrarInformacion();
                contador ++;
            }
            System.out.println("");
            System.out.println("El total de la reparaciòn es: " + total);
        }
    }
}
