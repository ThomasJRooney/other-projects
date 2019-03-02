//Tia Hannes - Hanne123 - 5286175
// Thomas Rooney - Roone194 - 5364798

import java.awt.*;

public class Triangle {

  double x;
  double y;
  double w;
  double h;
  Color col;

//Constructor, takes in an x position, y position, width, and height of a Triangle object, all of type double.

  public Triangle(double xpos, double ypos, double width, double height){

    x = xpos;
    y = ypos;
    w = width;
    h = height;

  } //constructor

//Method to calculate the perimeter of a Triangle object. Takes in no parameters and returns the perimeter of a Triangle object of type double.

  public double calculatePerimeter(){

    double perimeter = w + (2 * (Math.pow(((Math.pow((w/2),2)) + h),0.5)));
    return perimeter;

  }

//Method to calculate the area of a Triangle object. Takes in no parameters and returns the area of a Triangle object of type double.

  public double calculateArea() {

    double area = (w * h) / 2;
    return area;

  }

//Method to set the color of a Triangle object. Takes in a color of type Color.

  public void setColor(Color color){

    col = color;

  }

//Method to set the x and y position of a Triangle object. Takes in 2 parameters, an x and a y position, both of type double.

  public void setPos(double xpos, double ypos){

    x = xpos;
    y = ypos;

  }

//Mehthod to get the height of a Triangle object. Takes in no parameters and returns a height of type Double.

  public void setHeight(double height){

    h = height;

  }

//Mehthod to get the width of a Triangle object. Takes in no parameters and returns a width of type Double.

  public void setWidth(double width){

    w = width;

  }

//Mehthod to get the color of a Triangle object. Takes in no parameters and returns a color of type Color.

  public Color getColor(){

    return col;

  }

//Mehthod to get the x position of a Triangle object. Takes in no parameters and returns an x position of type double.

  public double getXPos(){

    return x;

  }

//Mehthod to get the y position of a Triangle object. Takes in no parameters and returns a y position of type double.

  public double getYPos(){

    return y;

  }

//Mehthod to get the height of a Triangle object. Takes in no parameters and returns a height of type double.

  public double getHeight(){

    return h;

  }

//Mehthod to get the width of a Triangle object. Takes in no parameters and returns a width of type double.

  public double getWidth(){

    return w;

  }

} //class
