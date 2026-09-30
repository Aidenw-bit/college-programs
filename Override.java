class Person
{
    private String name;
    
    Person(String name)
    {
        this.name = name;
    }
    
    public String getname()
    {
        return this.name;
    }
    
    public void displayInfo()
    {
        System.out.println("Name: " + this.name);
    }
}
class Student extends Person
{
    private String major;
    
    Student(String name, String major)
    {
        super(name);
        this.major = major;
    }
    
    public String getmajor()
    {
        return this.major;
    }
    
    @Override
    public void displayInfo()
    {
        System.out.println("Name: " + getname() + ", Major: " + this.major);
    }
}
class GraduateStudent extends Student
{
    private String researchTopic;
    
    GraduateStudent(String name, String major, String researchTopic)
    {
        super(name, major);
        this.researchTopic = researchTopic;
    }
    
    public String getresearchTopic()
    {
        return this.researchTopic;
    }
    
    @Override
    public void displayInfo()
    {
        System.out.println("Name: " + getname() + ", Major: " + getmajor() + ", Research Topic: " + this.researchTopic);
    }
}
public class Main
{
    public static void main(String[] args)
    {
        Person[] array = new Person[3];
        
        array[0] = new Person("Aiden");
        array[1] = new Student("Alex", "CSCI");
        array[2] = new GraduateStudent("Sean", "CSCI", "Polymorphic hierarchy");
        
        
        for (Person a : array)
        {
            a.displayInfo();
        }
        
        Person a = new Student("aiden", "CSCI");
        if (a instanceof Student)
        {
            Student s = (Student) a;
            System.out.println( s.getmajor() );
        }
        
    }
}