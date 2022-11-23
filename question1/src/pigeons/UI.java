package pigeons;
import javax.swing.JFrame;

/**
 * Classe d'interface utilisateur de l'application
 * 
 * @author Valentin THEDON
 * @author Nathan AMSELLEM
 * 
 * @version %I%, %G%
 * @since 1.0
 */
public class UI extends JFrame {

  /**
   * Parc de l'application
   */
  private Park park;

  /**
   * Constructeur de l'interface graphique
   * 
   * La taille de l'interface sera la même que celle du parc
   * 
   * @param park le parc attaché à cette interface
   */
  public UI(Park park) {
    super();
    this.park = park;
    this.setSize(park.getSize());

    this.setVisible(true);
    this.setLocationRelativeTo(null);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setTitle("Pigeons");

    this.setContentPane(park);
  }

  /**
   * Obtenir le park associé à l'intefrace graphique
   * 
   * @return parc de l'application
   */
  public Park getPark() {
    return park;
  }

  /**
   * Définir un parc pour l'interface graphique
   * 
   * @param park parc de l'application
   */
  public void setPark(Park park) {
    this.park = park;
  }

  /**
   * Dessiner l'interface
   */
  public void draw() {
    this.park.repaint();
  }

}
