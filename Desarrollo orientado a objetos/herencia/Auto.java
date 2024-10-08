//Sub class of Vehículo
public class Auto extends Vehiculo{
    //Cantidad de puertas, tiene o no aire acondicionado
    //Atributos
    private int cantidadPuertas;
    private boolean aireAcondicionado;

    //Constructor
    //Recibe los atributos de la super clase mas los propios
    public Auto(String idAuto, String marcaAuto, double precioAuto, int puertasAuto, boolean aireAcondicionadoAuto){
        //Con el super hereda los atributos de la superclase
        super(idAuto, marcaAuto, precioAuto);
        this.cantidadPuertas = puertasAuto;
        this.aireAcondicionado = aireAcondicionadoAuto;
    }
    public Auto(){
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
    public void setAireAcondicionado(boolean aireAcondicionado) {
        this.aireAcondicionado = aireAcondicionado;
    }
    public void setCantidadPuertas(int cantidadPuertas) {
        this.cantidadPuertas = cantidadPuertas;
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
    public int getCantidadPuertas() {
        return cantidadPuertas;
    }
    public boolean aireAcondicionado(){
        return aireAcondicionado;
    }

    //Métodos especiales

    //Mostrar info sobreescribir
    @Override
    public void mostrarInformacion(){
        /* 
         * El super.mostrarInformacion() hace lo siguiente:
         * System.out.println("Patente Vehículo: " + this.id);
         * System.out.println("Marca Vehículo: " + this.marca);
         * System.out.println("Precio Vehículo: " + this.precio);
        */
        
        super.mostrarInformacion();

        System.out.println("Cantidad de puertas: " + cantidadPuertas);
        System.out.println("Tiene aire acondicionado: " + (aireAcondicionado ? "Tiene aire" : "No tiene aire"));
    }

    //to-string
    @Override
    public String toString() {
        return super.toString() + "\nCantidad de puertas: " + cantidadPuertas + "\n¿Tiene aire acondicionado?: " + (aireAcondicionado ? "Tiene aire" : "No tiene aire");
    }
}
