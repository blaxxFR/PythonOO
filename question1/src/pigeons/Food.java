package pigeons;

import java.awt.Color;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Classe permettant de gérer une nourriture
 * 
 * @author Valentin THEDON
 * @author Nathan AMSELLEM
 * 
 * @version %I%, %G%
 * @since 1.0
 */
public class Food {

  /**
   * Position de la nourriture
   */
  private Position position;
  /**
   * Consommabilité de la nourriture
   */
  private boolean isFresh;
  /**
   * Temps restant de fraicheur de la nourriture
   */
  private long freshTimeLeft = 2000;
  /**
   * Nombre de thread travaillant en ecriture sur l'objet
   */
  private AtomicInteger numWriter = new AtomicInteger();

  /**
   * Couleur de la nourriture
   * - Rouge si non consommable
   * - Jaune si consommable
   */
  public Color color;

  /**
   * Constructeur de l'objet representant une nourriture
   * 
   * @param position Position de la nourriture
   */
  public Food(Position position) {
    this.position = position;

    this.isFresh = true;
    this.color = Color.YELLOW;
  }

  /**
   * Constructeur de l'objet representant une nourriture
   * 
   * @param x position sur l'axe des abscisses de la nourriture
   * @param y postiion sur l'axe des ordonnées de la nourriture
   */
  public Food(int x, int y) {
    this(new Position(x, y));
  }

  /**
   * Obtenir la position de la nourriture
   * 
   * @return position de la nourriture
   */
  public Position getPosition() {
    return position;
  }

  /**
   * Reduit le temps de fraicheur de la nourriture.
   * Si le temps restants de fraicheur, la nourriture est consideré comme non
   * consommable et la variable {@link Food#isFresh} vaut desormais
   * <code>true</code>. Par ailleurs la couleur d'une nourriture devient rouge
   * 
   * @param toReduce Temps à retirer du temps restant de fraicheur
   */
  public synchronized void reduceFreshTimeLeft(long toReduce) {
    this.numWriter.incrementAndGet();
    this.freshTimeLeft -= toReduce;
    if (this.freshTimeLeft < 0) {
      this.isFresh = false;
      this.color = Color.RED;
    }
    this.numWriter.decrementAndGet();
    notifyAll();
  }

  /**
   * Obtenir la couleur associé une nourriture
   * 
   * @return La couleur associé à la nouritture, jaune si consommable, rouge sinon
   */
  public Color getColor() {
    return color;
  }

  /**
   * Obtenir le temps de fraicheur restant à une nourriture
   * 
   * Cette méthode est executé avec un verrou ce qui permet aux oiseaux de
   * recuperer la propriété en étant sur que la variable n'est pas en cours de
   * modification
   * 
   * @return Temps de fraicheur restant à la nourriture
   */
  public synchronized long getFreshTimeLeft() {
    while (numWriter.get() != 0)
      try {
        wait();
      } catch (InterruptedException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
    return freshTimeLeft;
  }

  /**
   * Obtenir la consommabité de la nourriture
   * 
   * Cette fonction est executé avec un verrou ce qui permet aux oiseaux de
   * recuperer la propriété en étant sur que la variable n'est pas en cours de
   * modification
   * 
   * @return boolean
   * 
   */
  public synchronized boolean isFresh() {
    while (numWriter.get() != 0)
      try {
        wait();
      } catch (InterruptedException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
    return isFresh;
  }
}
