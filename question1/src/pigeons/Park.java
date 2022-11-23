package pigeons;
import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicInteger;

import javax.swing.JPanel;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.Color;
import java.awt.Graphics;

/**
 * Classe permettant de gérer un parc d'oiseaux
 * 
 * Ce parc permet de gerer un parc contenant des oiseaux, vous pouvez nourrir
 * ces oiseaux en cliquant sur votre interface, vos oiseaux seront effrayer de
 * manière aléatoire. Ce park peut
 * etre affiché à l'aide d'une <code>JFrame</code>.
 * 
 * @author Valentin THEDON
 * @author Nathan AMSELLEM
 * 
 * @version %I%, %G%
 * @since 1.0
 */
public class Park extends JPanel implements MouseListener {

  /**
   * Oiseaux présent dans le parc
   */
  private ArrayList<Bird> birds;
  /**
   * Nourritures présente dans le parc
   */
  private ArrayList<Food> foods;

  /**
   * Probabilité d'effrayer les oiseaux, decroit à chaque actualisation du parc
   */
  private int frightenProbaility = 20000;

  /**
   * Nombre de thread travaillant en ecriture sur l'objet
   */
  private AtomicInteger numWriter = new AtomicInteger();

  /**
   * Constructeur de l'objet representant un parc
   * 
   * @param width  longueur du parc
   * @param height hauteur du parc
   */
  public Park(int width, int height) {
    super();
    super.setSize(width, height);

    this.addMouseListener(this);

    this.birds = new ArrayList<Bird>();
    this.foods = new ArrayList<Food>();
  }

  /**
   * Obtenir les oiseaux du parc
   * 
   * @return la liste contenant les oiseaux du parcs
   */
  public ArrayList<Bird> getBirds() {
    return birds;
  }

  /**
   * Obtenir la nourriture du parc
   * 
   * Cette méthode est executé avec un verrou ce qui permet aux oiseaux de
   * recuperer la propriété en étant sur que la variable n'est pas en cours de
   * modification
   * 
   * @return la liste contenant les nourritures du parc
   */
  public synchronized ArrayList<Food> getFoods() {

    try {
      while (numWriter.get() != 0) {
        wait();
      }
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    return foods;
  }

  /**
   * Ajouter une nourriture dans le parc
   * 
   * Cette méthode est executé avec un verrou ce qui permet de modifier la
   * propriété, tout en bloquant les lectures eventuelles de la propriété.
   * L'ecriture est prioritaire sur la lecture.
   * 
   * @param toAdd nourriture a ajouter au parc
   */
  public synchronized void addFood(Food toAdd) {
    numWriter.incrementAndGet();
    this.foods.add(toAdd);
    numWriter.decrementAndGet();
    notifyAll();
  }

  /**
   * Ajouter un oiseau dans le parc
   * 
   * @param toAdd Oiseau à ajouter au parc
   */
  public void addBird(Bird toAdd) {
    this.birds.add(toAdd);
    Thread t = new Thread(toAdd);
    t.start();
  }

  /**
   * Supprimer des nourriture présente sur le parc
   * 
   * Cette méthode est executé avec un verrou ce qui permet de modifier la
   * propriété, tout en bloquant les lectures eventuelles de la propriété.
   * L'ecriture est prioritaire sur la lecture.
   * 
   * @param foods liste de nourriture à supprimer du parc
   */
  public synchronized void removeFoods(ArrayList<Food> foods) {
    numWriter.incrementAndGet();
    this.foods.removeAll(foods);
    numWriter.decrementAndGet();
    notifyAll();

  }

  /**
   * Supprimer une nourriture du parc
   * 
   * Cette méthode est executé avec un verrou ce qui permet de modifier la
   * propriété, tout en bloquant les lectures eventuelles de la propriété.
   * L'ecriture est prioritaire sur la lecture.
   * 
   * @param food nourriture à ajouter
   */
  public synchronized void removeFood(Food food) {
    numWriter.incrementAndGet();
    this.foods.remove(food);
    numWriter.decrementAndGet();
    notifyAll();

  }

  @Override
  public void paintComponent(Graphics g) {
    refreshPark();
    g.setColor(Color.WHITE);
    g.fillRect(0, 0, this.getWidth(), this.getHeight());
    for (Bird b : birds) {
      if (b.isAlive()) {
        g.setColor(Bird.COLOR);
        g.fillRect(b.getPosition().getX(), b.getPosition().getY(), 15, 15);
      }
    }

    synchronized (foods) {
      try {
        while (numWriter.get() != 0) {
          wait();
        }
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      for (Food f : foods) {
        g.setColor(f.getColor());
        g.fillOval(f.getPosition().getX(), f.getPosition().getY(), 5, 5);
      }
    }
  }

  @Override
  public void mouseClicked(MouseEvent e) {
    Food f = new Food(e.getX(), e.getY());
    this.addFood(f);
    for (Bird b : birds) {
      synchronized (b) {
        b.notify();
      }
    }
  }

  @Override
  public void mousePressed(MouseEvent e) {
    // TODO Auto-generated method stub

  }

  @Override
  public void mouseReleased(MouseEvent e) {
    // TODO Auto-generated method stub

  }

  @Override
  public void mouseEntered(MouseEvent e) {
    // TODO Auto-generated method stub

  }

  @Override
  public void mouseExited(MouseEvent e) {
    // TODO Auto-generated method stub

  }

  /**
   * @param index index de liste de l'oiseau à supprimer
   */
  public void removeBird(int index) {
    this.birds.remove(index);
  }

  /**
   * Rafraichir le parc, supprime les nourriture périmés depuis un certain temps,
   * réduit le temps de fraicheurs des nourritures et essaye d'effrayer les
   * oiseaux du park
   */
  private void refreshPark() {
    ArrayList<Food> foodToRemove = new ArrayList<Food>();
    for (Food f : foods) {
      f.reduceFreshTimeLeft(1);
      if (f.getFreshTimeLeft() <= -5000) {
        foodToRemove.add(f);
      }
    }
    this.removeFoods(foodToRemove);

    if (Math.floor(Math.random() * (--frightenProbaility)) == 0) {
      for (Bird b : birds) {
        b.frighten();
        this.frightenProbaility = 20000;
      }
    }

  }

  public boolean isBusy(){
    return (numWriter.get() > 0);
  }
}
