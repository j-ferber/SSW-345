import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Where do you want to order pizza from? Enter in this format without <>: MyPizzaApp <franchise> <pizzaKind>");
        String input = sc.nextLine();
        String[] splitInput = input.split(" ");
        if (splitInput[1].equals("NYPizzaStore")) {
            PizzaStore nyPizzaStore = new NYPizzaStore();
            Pizza pizza = nyPizzaStore.orderPizza(splitInput[2]);
            System.out.println(pizza.toString());
        } else if (splitInput[1].equals("ChicagoPizzaStore")) {
            PizzaStore chicagoPizzaStore = new ChicagoPizzaStore();
            Pizza pizza = chicagoPizzaStore.orderPizza(splitInput[2]);
            System.out.println(pizza.toString());
        } else {
            System.out.println("Unknown Pizza Store");
        }
    }
}
