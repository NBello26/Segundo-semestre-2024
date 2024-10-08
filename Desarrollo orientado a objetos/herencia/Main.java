public class Main {
    public static void main(String[] args) {
        //crear auto
        Auto auto = new Auto("1234", "Susuki", 10, 4, true);
        //Crear moto
        Motocicleta moto = new Motocicleta("1235", "Yamaha", 20, false);
        //Crear un cliente
        Cliente cliente1 = new Cliente("12.345.456-7", "Nicolàs");
        //Creo una reparacion y agrego vehiculo
        Reparacion reparacion = new Reparacion();
        reparacion.agregarVehiculo(auto);
        //agrego reparacion a cliente
        cliente1.agregarReparacion(reparacion);
        //Muestro informacion
        cliente1.mostrarInformacion();
        /*
        Reparacion reparacion2 = new Reparacion();
        reparacion2.agregarVehiculo(moto);
        cliente1.agregarReparacion(reparacion2);
        cliente1.mostrarInformacion();
         */
        reparacion.agregarVehiculo(moto);
        cliente1.mostrarInformacion();
    }
}
