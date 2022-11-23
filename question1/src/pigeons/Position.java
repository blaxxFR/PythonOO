package pigeons;

/**
 * Classe representant un position
 * 
 * @author Valentin THEDON
 * @author Nathan AMSELLEM
 * 
 * @version %I%, %G%
 * @since 1.0
 */
public class Position {

  /**
   * Coordonnée sur l'axe des abscisses
   */
  private int x;
  /**
   * Coodonnée sur l'axe des ordonées
   */
  private int y;

  /**
   * Constructeur de l'objet representant une position
   * 
   * @param x position sur l'abscisse
   * @param y position sur l'ordonée
   */
  public Position(int x, int y) {
    this.x = x;
    this.y = y;
  }

  /**
   * Constructeur de l'objet representant une position
   * 
   * Position fixé à l'origine (0 ; 0)
   */
  public Position() {
    this(0, 0);
  }

  /**
   * Calculer la distance entre 2 positions
   * 
   * @param position postion distante
   * @return distance entre les 2 points
   */
  public int distance(Position position) {
    return (int) Math.sqrt(Math.pow(Math.abs(this.x - position.x), 2) + Math.pow(Math.abs(this.y - position.y), 2));
  }

  /**
   * Déplacer la position
   * 
   * @param x nouvelle position sur l'axe des abscisses
   * @param y nouvelle position sur l'axe des abscisses
   */
  public void moveTo(int x, int y) {
    this.x = x;
    this.y = y;
  }

  /**
   * Déplacer la position
   * 
   * @param toMove nouvelle position
   */
  public void moveTo(Position toMove) {
    this.moveTo(toMove.getX(), toMove.getY());
  }

  /**
   * Obtenir la position sur l'axe des abscisses
   * 
   * @return coordonnée sur l'abscisses
   */
  public int getX() {
    return this.x;
  }

  /**
   * Définir une coordonée d'abscisse
   * 
   * @param x nouvelle coordonnée d'abscisse
   */
  public void setX(int x) {
    this.x = x;
  }

  /**
   * Obtenir la position sur l'axe des ordonées
   * 
   * @return coordonnée sur l'ordonnée
   */
  public int getY() {
    return this.y;
  }

  /**
   * Définir une coordonée d'ordonée
   * 
   * @param y nouvelle coordonnée d'ordonée
   */
  public void setY(int y) {
    this.y = y;
  }

}
