
public class Alumno {
    private int id;
    private String nombre;
    private int edad;
    private String membresia;

    //Constructor
    public Alumno (int id, String nombre, int edad, String membresia){
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
        this.membresia = membresia;
    }

    public Alumno (){
    }
    //set
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public void setId(int id) {
        this.id = id;
    }
    public void setMembresia(String membresia) {
        this.membresia = membresia;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    //get
    public int getEdad() {
        return edad;
    }
    public int getId() {
        return id;
    }
    public String getMembresia() {
        return membresia;
    }
    public String getNombre() {
        return nombre;
    }
    //especiales

    //to string
    @Override
    public String toString() {
        return "id: " + this.id + "\n" + "nombre: " + this.nombre + "\n" + "edad: " + this.edad + "\n" + "Tipo de membresía: " + this.membresia;
    }
}