public class ConstructorTest {
    // declare instance fields here!
    
    
    // constructor method
    public ConstructorTest() {
    System.out.println("I am inside the constructor method.");
    }
    
    @Override
    public String toString(){
        return "Test";
    }
    // main method
    public static void main(String[] args) {
    System.out.println("This code is inside the main method.");

    ConstructorTest tesuto = new ConstructorTest();

    System.out.println(tesuto);
    }
}