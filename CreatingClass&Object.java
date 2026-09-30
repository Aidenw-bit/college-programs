class Rectangle
{
	private double width;
	private double height;
	
	public Rectangle(double width, double height)
	{
		this.width = width;
		this.height = height;
	}
	
	public double area()
	{
		return width * height ;
	}
	
	public double perimeter()
	{
		return 2 * (width + height );
	}
}
public class Main
{
	public static void main(String[] args)
	{
		Rectangle r = new Rectangle( 5, 4 );
		System.out.println("The area of this rectangle is " + r.area() + ", and the perimeter is " + r.perimeter() );
	}
}