package pigeons;
public class App {
    /**
     * Fonction Main permettant de lancer l'application
     * 
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        Park park = new Park(500, 500);

        new Bird(12, 123, park);
        new Bird(102, 235, park);
        new Bird(321, 421, park);
        new Bird(126, 231, park);
        new Bird(411, 34, park);
        new Bird(245, 333, park);

        UI ui = new UI(park);

        while (true) {
            ui.draw();
            Thread.sleep(1);
        }
    }
}
