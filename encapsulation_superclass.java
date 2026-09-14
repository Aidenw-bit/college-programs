class Person
{
    private String name;
    private String email;
    
    Person(String name, String email)
    {
        this.name = name;
        this.email = email;
    }
    
    public String getname()
    {
        return this.name;
    }
    
    public String getemail()
    {
        return this.email;
    }
}

class Student extends Person
{
    private String major;
    
    Student(String name, String email, String major)
    {
        super(name, email);
        this.major = major;
    }
    
    public String getmajor()
    {
        return this.major;
    }
}

class Instructor extends Person
{
    private int office;
    
    Instructor(String name, String email, int office)
    {
        super(name, email);
        this.office = office;
    }
    
    public int getoffice()
    {
        return this.office;
    }
}


public class Main
{
    public static void main(String[] args)
    {
        Student Aiden = new Student("Aiden", "aweldon3@mcneese.edu", "CSCI");
        Instructor Dr_Nizam = new Instructor("Dr_Nizam", "nizam2@mcneese.edu", 123);
        
        System.out.println("Student name: " + Aiden.getname() + "    Student email: " + Aiden.getemail() + "    Student major: "+ Aiden.getmajor() );
        System.out.println("Instructor name: " + Dr_Nizam.getname() + "    Instructor email: " + Dr_Nizam.getemail() + "    Instructor office: " + Dr_Nizam.getoffice() );
    }
}