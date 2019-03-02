//Tia Hannes - Hanne123 - 5286175
// Thomas Rooney - Roone194 - 5364798

import java.util.Scanner;
import java.awt.*;

public class Main{

  /*
  Main method which prompts the user for input, and then calls upon the method to draw the
  corresponding fractal. Assumes that java.awt.*, and java.util.Scanner are imported.
   */

  public static void main(String[] args){

    Canvas canvas = new Canvas(1000, 1000);
    Scanner s = new Scanner(System.in);
    System.out.println("Enter one of the following:\n'triangle' to draw a triangle \n'rectangle' to draw a rectangle \n'circle' to draw a circle: ");
    String next = s.nextLine();
    Color col = Color.BLUE;
    double area;

//Conditionals based on the user input that indicate what fractal to draw based on the user input.

    if (next.equals("rectangle")) {

      Rectangle userRectangle = new Rectangle(400, 300, 256, 256);
      userRectangle.setColor(col);
      canvas.drawShape(userRectangle);
      canvas.repaint();
      area = userRectangle.calculateArea();
      System.out.println(rectangleFractal(canvas, userRectangle, area));

    }

    else if (next.equals("triangle")) {

      Triangle userTriangle = new Triangle(400, 600, 256, 256);
      userTriangle.setColor(col);
      canvas.drawShape(userTriangle);
      canvas.repaint();
      area = userTriangle.calculateArea();
      System.out.println(triangleFractal(canvas, userTriangle, area));
    }

    else if (next.equals("circle")) {

      Circle userCircle = new Circle(500, 500, 128);
      userCircle.setColor(col);
      canvas.drawShape(userCircle);
      canvas.repaint();
      area = userCircle.calculateArea();
      System.out.println(circleFractal(canvas, userCircle, area));
    }

    s.close();

  } //main method

  /*

  Recursive Method to draw rectangle fractal. Parameters it takes in: a Canvas object, Rectangle object,
  and the area of the corresponding rectangle object. Output: draws a rectangle fractal and returns
  the area of all of the individuals rectangles drew added together. Assumes that java.awt.* is imported.

  */

  public static double rectangleFractal(Canvas canvas, Rectangle rectangle, double area){

    if (rectangle.getWidth() <= 2){
      return area;
    } //base case

    else {
    //code to create fractal rectangle in bottom left corner
    double width = rectangle.getWidth() / 2;
    double height = rectangle.getHeight() / 2;
    double xpos1 = rectangle.getXPos() - width;
    double ypos1 = rectangle.getYPos() + (2 * height);

    Color col;
    if (rectangle.getColor() == Color.BLUE){
      col = Color.RED;
    }
    else if (rectangle.getColor() == Color.RED) {
      col = Color.GREEN;
    }
    else {
      col = Color.BLUE;
    }

    Rectangle rectangle1 = new Rectangle(xpos1, ypos1, width, height);
    rectangle1.setColor(col);
    canvas.drawShape(rectangle1);
    canvas.repaint();

    //code to draw fractal rectangle in bottom right corner
    double xpos2 = xpos1 + (3 * width);
    Rectangle rectangle2 = new Rectangle(xpos2, ypos1, width, height);
    rectangle2.setColor(col);
    canvas.drawShape(rectangle2);
    canvas.repaint();

    //code to draw fractal rectangle on top left corner
    double ypos3 = ypos1 - (height * 3);
    Rectangle rectangle3 = new Rectangle(xpos1, ypos3, width, height);
    rectangle3.setColor(col);
    canvas.drawShape(rectangle3);
    canvas.repaint();

    //code to draw fractal rectangle on top right corner
    Rectangle rectangle4 = new Rectangle(xpos2, ypos3, width, height);
    rectangle4.setColor(col);
    canvas.drawShape(rectangle4);
    canvas.repaint();

    rectangleFractal(canvas, rectangle1, (rectangle1.calculateArea() + area));
    rectangleFractal(canvas, rectangle4, (rectangle4.calculateArea() + area));
    rectangleFractal(canvas, rectangle3, (rectangle3.calculateArea() + area));
    rectangleFractal(canvas, rectangle2, (rectangle2.calculateArea() + area));

    } //else statement

      return area;
    } //rectangleFractal method

/*

Recursive Method to draw triangle fractal. Parameters it takes in: a Canvas object, a Triangle object,
and the area of the corresponding Triangle object. Output: draws triangle fractals and returns
the area of all of the individuals triangles drew added together. Assumes that java.awt.* is imported.

*/

  public static double triangleFractal(Canvas canvas, Triangle triangle, double area){

    if (triangle.getWidth() <= 2){
      return area;
    } //base case

    else {
    //code to create fractal triangle in bottom left corner
    double width = triangle.getWidth() / 2 ;
    double height = triangle.getHeight() / 2;
    double xpos1 = triangle.getXPos() - width;
    double ypos1 = triangle.getYPos();
    Color col;
    if (triangle.getColor() == Color.BLUE){
      col = Color.RED;
    }
    else if (triangle.getColor() == Color.RED) {
      col = Color.GREEN;
    }
    else {
      col = Color.BLUE;
    }
    Triangle triangle1 = new Triangle(xpos1, ypos1, width, height);
    triangle1.setColor(col);
    canvas.drawShape(triangle1);
    canvas.repaint();

    //code to draw fractal triangle in bottom right corner
    double xpos2 = xpos1 + (3 * width);
    Triangle triangle2 = new Triangle(xpos2, ypos1, width, height);
    triangle2.setColor(col);
    canvas.drawShape(triangle2);
    canvas.repaint();

    //code to draw fractal on top of triangle
    double xpos3 = xpos1 + (width + (width/2));
    double ypos3 = ypos1 - (height * 2);
    Triangle triangle3 = new Triangle(xpos3, ypos3, width, height);
    triangle3.setColor(col);
    canvas.drawShape(triangle3);
    canvas.repaint();

    triangleFractal(canvas, triangle3, (triangle3.calculateArea() + area));
    triangleFractal(canvas, triangle1, (triangle1.calculateArea() + area));
    triangleFractal(canvas, triangle2, (triangle2.calculateArea() + area));

  } //else statement

    return area;

  } //triangleFractal method

/*

Recursive Method to draw circle fractal. Parameters it takes in: a Canvas object, Circle object,
and the area of the corresponding Circle object. Output: draws circle fractals and returns
the area of all of the individuals circles drew added together. Assumes that java.awt.* is imported.

*/

public static double circleFractal(Canvas canvas, Circle circle, double area){

  if (circle.getRadius() <= 2){
    return area;
  } //base case

  else {
  //code to create fractal circle on left side of center circle
    double radius = circle.getRadius() / 2 ;
    double xpos1 = circle.getXPos() - (3 * radius);
    double ypos = circle.getYPos();
    Color col;
    if (circle.getColor() == Color.BLUE){
      col = Color.RED;
    }
    else if (circle.getColor() == Color.RED) {
      col = Color.GREEN;
    }
    else {
      col = Color.BLUE;
    }
  Circle circle1 = new Circle(xpos1, ypos, radius);
  circle1.setColor(col);
  canvas.drawShape(circle1);
  canvas.repaint();

  //code to draw fractal circle on right side of center of circle

  double xpos2 = xpos1 + (6 * radius);
  Circle circle2 = new Circle(xpos2, ypos, radius);
  circle2.setColor(col);
  canvas.drawShape(circle2);
  canvas.repaint();

  double ypos2 = ypos + (3 * radius);
  double xpos3 = xpos1 + (3 * radius);
  Circle circle3 = new Circle(xpos3, ypos2, radius);
  circle3.setColor(col);
  canvas.drawShape(circle3);
  canvas.repaint();

  double ypos3 = ypos - (3 * radius);
  Circle circle4 = new Circle(xpos3, ypos3, radius);
  circle4.setColor(col);
  canvas.drawShape(circle4);
  canvas.repaint();

  circleFractal(canvas, circle1, (circle1.calculateArea() + area));
  circleFractal(canvas, circle2, (circle2.calculateArea() + area));
  circleFractal(canvas, circle3, (circle3.calculateArea() + area));
  circleFractal(canvas, circle4, (circle4.calculateArea() + area));

    } //else statement

    return area;

  }//circleFractal method

} //class
