package com.company;

import java.util.Random;
import java.util.Scanner;
public class GuessNumber {
    public static void main(String[] args) {
        Random Random_number = new Random();
        int rightNum
                = Random_number.nextInt(20);
        int turns = 0;
        Scanner scan = new Scanner(System.in);
        System.out.println("Guess a number between 1 to 20, You will have 6 turns!");
        System.out.println("Here we go!");

        int guess;
        int i = 0;
        boolean win = false;
        while (win == false) {
            guess = scan.nextInt();
            turns++;

            if (guess == rightNum
            ) {
                win = true;
            } else if (i > 8) {
                System.out.println("Akinator says BZZzz! That's all folks the right answer was: " + rightNum
                );
                return;
            } else if (guess < rightNum
            ) {
                i++;
                System.out.println("Akinator says Too Low! " + (6 - i));


            } else if (guess > rightNum
            ) {
                i++;
                System.out.println("Akinator says Too high! Turns left: " + (6 - i));

            }


        }
        System.out.println("Akinator praises you as theWinner!");
        System.out.println("Then number was " + rightNum
        );
        System.out.println("You used " + turns + " turns to guess the right number");
        System.out.println("Akinator says you want to play again, too bad!");
    }
}
