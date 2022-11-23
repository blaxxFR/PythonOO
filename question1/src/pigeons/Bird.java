package pigeons;
import java.awt.Color;

/**
 * Classe permettant de gérer un oiseau
 * 
 * Implemente l'interface Runnable, ce qui permet d'executer les actions d'un
 * oiseau dans un thread.
 * 
 * @author Valentin THEDON
 * @author Nathan AMSELLEM
 * 
 * @version %I%, %G%
 * @since 1.0
 */

public class Bird implements Runnable {

  /**
   * Positiion de l'oiseau
   */
  private Position position;

  /**
   * Parc de rattachement de l'oiseau
   */
  private Park park;
  private boolean isAlive = true;

  /**
   * Couleur d'un oiseau
   */
  public static Color COLOR = Color.BLACK;
  /**
   * Temps de raffraichissement d'un oiseau (en ms)
   */
  public static int REFRESH_TIME = 20;
  /**
   * Vitesse d'un oiseau
   */
  public static int VELOCITY = 10;

  /**
   * Constructeur de l'objet oiseau
   * 
   * @param position position de l'oiseau
   * @param park parc de rattachement de l'oiseau
   */
  public Bird(Position position, Park park) {
    this.position = position;
    this.park = park;
    this.park.addBird(this);
  }

  /**
   * Constructeur de l'objet oiseau
   * 
   * @param x position sur l'axe des abscisses de l'oiseau
   * @param y position sur l'axe des ordonnées de l'oiseau
   * @param park parc de rattachement de l'oiseau
   */
  public Bird(int x, int y, Park park) {
    this(new Position(x, y), park);
  }

  /**
   * Detecte la nourriture la plus proche de l'oiseau
   * 
   * @return Food L'objet representant la nourriture la plus proche
   */
  public Food findNearestFood() {
    Food nearestFood = null;
    int minDistance = Integer.MAX_VALUE;
    int i = 0;
    while(i < park.getFoods().size()){
      Food f = park.getFoods().get(i);
      if (this.position.distance(f.getPosition()) < minDistance && f.isFresh()) {
        nearestFood = f;
        minDistance = this.position.distance(f.getPosition());
      }
      i++;
    }
    return nearestFood;
  }

  @Override
  public void run() {
    while (isAlive) {
      Food nearestFood = findNearestFood();
      if (nearestFood != null) {
        this.moveTo(nearestFood);
        Food onFood = this.getOnFood();
        if (onFood != null && onFood.isFresh()) {
          this.park.removeFood(onFood);
        }
      }
      try {
        Thread.sleep(REFRESH_TIME);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }

  /**
   * Deplace un oiseau vers une position
   * 
   * @param toMove La position vers laquelle nous devous nous deplacer
   */
  public void moveTo(Position toMove) {
    if (this.position.distance(toMove) <= ((VELOCITY * REFRESH_TIME * 0.01))) {
      this.position.moveTo(toMove.getX(), toMove.getY());
    } else {
      float x = this.position.getX()
          + ((VELOCITY * REFRESH_TIME * 0.01f)
              * ((toMove.getX() - this.position.getX()) / (float) this.position.distance(toMove)));
      float y = this.position.getY()
          + (((VELOCITY * REFRESH_TIME * 0.01f))
              * ((toMove.getY() - this.position.getY()) / (float) this.position.distance(toMove)));
      this.position.moveTo(Math.round(x), Math.round(y));
    }
  }

  /**
   * Deplacer l'oiseau vers une nourriture
   * 
   * @param food La nourriture vers laquelle l'oiseau doit se diriger
   */
  public void moveTo(Food food) {
    this.moveTo(food.getPosition());
  }

  /**
   * Effraie l'oiseau, a pour but de le déplacer à une position aléatoire
   */
  public void frighten() {
    this.position.moveTo(Math.round((float) Math.random() * park.getWidth()),
        Math.round((float) Math.random() * park.getHeight()));
    ;
  }

  /**
   * @return Food Renvoie la nourriture sur laquelle nous nous situons, ou null si nous sommes sur aucune nourriture
   */
  public Food getOnFood() {
    for (Food f : park.getFoods()) {
      if (this.position.distance(f.getPosition()) == 0)
        return f;
    }
    return null;
  }

  /**
   * Obtenir le parc dans lequel l'oiseau evolue
   * 
   * @return  Le parc dans lequel l'oiseau évolue
   */
  public Park getPark() {
    return park;
  }

  /**
   * Définir un parc dans lequel l'oiseau evoluera
   * 
   * @param park Le parc dans lequel l'oiseu évoluera
   */
  public void setPark(Park park) {
    this.park = park;
  }

  /**
   * 
   * @return boolean vrai si l'oiseau est en vie, faux sinon.
   */
  public boolean isAlive() {
    return this.isAlive;
  }

  /**
   * Obtenir la position de l'oiseau
   * 
   * @return Position la position actuelle de l'oiseau
   */
  public Position getPosition() {
    return this.position;
  }
}
