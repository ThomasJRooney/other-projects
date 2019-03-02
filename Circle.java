//Tia Hannes - Hanne123 - 5286175
// Thomas Rooney - Roone194 - 5364798

import java.awt.*;
import java.lang.Math.*;

public class Circle {

  double x;
  double y;
  double radius;
  Color col;

//Constructor, takes in an x and y position both doubles, and a radius which is also a double

  public Circle(double xpos, double ypos, double rad){

    x = xpos;
    y = ypos;
    radius = rad;

  } //constructor

//Method to calculate the perimeter of a Circle object. Takes no parameters and returns the perimeter of a circle object of type double.

  public double calculatePerimeter(){

    double perimeter = 2 * Math.PI * radius;
    return perimeter;

  }

//Method to calculate the area of a Circle object. Takes no parameters and returns the area of the Circle object of type double.

  public double calculateArea(){

    double area = Math.PI * radius * radius;
    return area;

  }

//Method to set the color of a Circle object. Takes in a color of type Color.

  public void setColor(Color color){

    col = color;

  }

//Method to set the x and y position of a Circle object. Takes in 2 parameters, an x position and a y position, both of type double.

  public void setPos(double xpos, double ypos){

    x = xpos;
    y = ypos;

  }

//Method to set the radius of a Circle object.

  public void setRadius(double rad){

    radius = rad;

  }

//Method to get the color of a Circle object. Returns the color which is a Color.

  public Color getColor(){

    return col;

  }

//Method to get the x position of a Circle object. Returns the x position which is a double.

  public double getXPos(){

    return x;

  }

//Method to get the y position of a Circle object. Returns the y position which is a double.

  public double getYPos(){

    return y;

  }

//Method to get the radius of a Circle object. Returns the radius of a circle object which is a double.

  public double getRadius(){

    return radius;

  }

} //class
