public class Motocicleta extends Vehiculo{

    //Atributos
    private boolean tieneMaletero;

    //Constructor
    public Motocicleta(String idMoto, String marcaMoto, double precioMoto, boolean tieneMaleteroMoto){
        super(idMoto, marcaMoto, precioMoto);
        this.tieneMaletero = tieneMaleteroMoto;
    }
    public Motocicleta(){
        super();
    }

    //set
    @Override
    public void setId(String id) {
        // TODO Auto-generated method stub
        super.setId(id);
    }
    @Override
    public void setMarca(String marca) {
        // TODO Auto-generated method stub
        super.setMarca(marca);
    }
    @Override
    public void setPrecio(double precio) {
        // TODO Auto-generated method stub
        super.setPrecio(precio);
    }
    public void setTieneMaletero(boolean tieneMaletero) {
        this.tieneMaletero = tieneMaletero;
    }

    //get
    @Override
    public String getId() {
        // TODO Auto-generated method stub
        return super.getId();
    }
    @Override
    public String getMarca() {
        // TODO Auto-generated method stub
        return super.getMarca();
    }
    @Override
    public double getPrecio() {
        // TODO Auto-generated method stub
        return super.getPrecio();
    }
    public boolean getTieneMaletero(){
        return tieneMaletero;
    }

    //Metodo especiales
    //Mostrar información
    @Override
    public void mostrarInformacion(){
        super.mostrarInformacion();
        System.out.println("¿Tiene maletero?: " + (tieneMaletero ? "Tiene maletero" : "No tiene maletero"));
    }

    //To-string
    @Override
    public String toString() {
        return super.toString() + "\n¿Tiene maletero?: " + (tieneMaletero ? "Tiene maletero" : "No tiene maletero");
    }
}
