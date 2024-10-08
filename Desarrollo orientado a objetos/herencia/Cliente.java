import java.util.ArrayList;
public class Cliente {
    private String id,nombre;
    private ArrayList<Reparacion> listareparaciones;

    //Constructor
    public Cliente(String rut, String nombrePersona){
        this.id = rut;
        this.nombre = nombrePersona;
        this.listareparaciones = new ArrayList<>();
    }
    public Cliente(){
    }

    //set
    public void setId(String id) {
        this.id = id;
    }
    public void setListareparaciones(ArrayList<Reparacion> listareparaciones) {
        this.listareparaciones = listareparaciones;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    //get
    public String getId() {
        return id;
    }
    public ArrayList<Reparacion> getListareparaciones() {
        return listareparaciones;
    }
    public String getNombre() {
        return nombre;
    }

    //Métodos especiales

    //Aregar reparaciones
    public void agregarReparacion(Reparacion reparacion){
        listareparaciones.add(reparacion);
    }
    //Mostrarinfo
    public void mostrarInformacion(){
        System.out.println("");
        System.out.println("Cliente: " + nombre);
        System.out.println("Id cliente: " + id);
        System.out.println("Reparaciones: ");
        if(listareparaciones.isEmpty()){
            System.out.println("No existen reparaciones");
        }else{
            for(Reparacion reparacion : listareparaciones){
                System.out.println("");
                System.out.println("Reparaciòn " + ":");
                reparacion.mostrarInformacion();
            }
        }
        System.out.println("");
    }
    //To-string
    @Override
    public String toString() {
        return "Id Cliente: " + id + "\nNombre del cliente: " + nombre;
    }
}
