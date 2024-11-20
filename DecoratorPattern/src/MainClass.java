public class MainClass
{
    public MainClass()
    {
        Pizza pizza = new MargheritaPizza();
        pizza = new MushroomDecorator(pizza);
        pizza = new PepperoniDecorator(pizza);
        
        // prints "Margherita Pizza, mushrooms, pepperoni"
        System.out.println(pizza.getDescription());
        // prints "9.74"
        System.out.println(pizza.getCost()); 
    }
    
    public static void main(String[] args)
    {
        new MainClass();
    }
}
