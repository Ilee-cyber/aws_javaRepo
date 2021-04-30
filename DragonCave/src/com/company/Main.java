package com.company;
import java.util.Scanner;
import org.graalvm.compiler.nodes.NodeView.Default;
public class Dragons {

    public static void main(String[] args) {
        Scanner thefool = new Scanner(System.in);
        System.out.print(
                "You are in a land full of dragons. In front of you,\n" +
                        "\n you see two caves. In one cave, the dragon is friendly\n" +
                        "\n and will share his treasure with you. The other dragon\n" +
                        "\n is greedy and hungry and will eat you on sight.\n" +
                        "\nWhich cave will you go into? (1 or 2)"

        );
        int caveNum = thefool.nextInt();
        switch(caveNum){
            case 1: System.out.println("You approach the cave...\n" +
                    "\nIt is dark and spooky...\n" +
                    "\n A large dragon jumps o ut in front of you! He opens his jaws and...\n" +
                    "\n Gobbles you down in one bite!");
                System.out.println("Process finished with exit code 0");
                break;
            case 2: System.out.println("You approach the cave...\n" +
                    "\n" +
                    "It is dark and spooky...\n" +
                    "\n" +
                    "A large dragon jumps out in front of you! He opens his jaws and...\n" +
                    "\n" +
                    "Gobbles you down in one bite!");
                System.out.println("Process finished with exit code 0");
                break;
            default:
                System.out.println("Find the one with riches or find the one with woe");
                System.out.println("Process finished with exit code 0");
                break; // a more realistic approach to what happens with dragons
        }
	// write your code here
    }
}
