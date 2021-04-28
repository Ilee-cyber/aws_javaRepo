package com.company;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class hangman{

    // Java Keywords
    public static final String[] WORDS = {
            "BREAK", "CASE", "CHAR", "CLASS","FALSE",
            "FLOAT", "FOR", "IF", "PRIVATE", "PUBLIC", "RETURN",
            "SWITCH","TRUE", "WHILE"
    };
    public static final Random RANDOM = new Random();
    // Max errors before user lose
    public static final int maxTry = 6;
    // Word to find
    private String wordToFind;
    // Word found stored in a char array to show user
    private char[] wordFound;
    private int try1;
    // letters already entered by user
    private ArrayList < String > letters = new ArrayList < > ();

    // Method returning randomly next word to find
    private String nextWordToFind() {
        return WORDS[RANDOM.nextInt(WORDS.length)];
    }

    // Method for starting a new game
    public void newGame() {
        try1 = 0;
        letters.clear();
        wordToFind = nextWordToFind();

        // word found initialization
        wordFound = new char[wordToFind.length()];

        for (int i = 0; i < wordFound.length; i++) {
            wordFound[i] = '_';
        }
    }

    // Method returning true if word is found
    public boolean wordFound() {
        return wordToFind.contentEquals(new String(wordFound));
    }

    // Method updating the word found after user entered a character
    private void enter(String c) {
        // we update only if c has not already been entered
        if (!letters.contains(c)) {
            if (wordToFind.contains(c)) {
                int index = wordToFind.indexOf(c);

                while (index >= 0) {
                    wordFound[index] = c.charAt(0);
                    index = wordToFind.indexOf(c, index + 1);
                }
            } else {
                // c not in the word => error
                try1++;
            }

            // c is now a letter entered
            letters.add(c);
        }
    }

    // Method returning the result of word, aka what the question ask?
    private String wordFoundList() {
        StringBuilder Bobthebuilder = new StringBuilder();

        for (int i = 0; i < wordFound.length; i++) {
            Bobthebuilder.append(wordFound[i]);

            if (i < wordFound.length - 1) {
                Bobthebuilder.append(" ");
            }
        }

        return Bobthebuilder.toString();
    }

    // Play method for our Hangman Game
    public void play() {
        try (Scanner input = new Scanner(System.in)) {
            // we play while try1 is lower than max errors or user has found the word
            while (try1 < maxTry) {
                System.out.println("\nEnter a letter : ");
                // get next input from user
                String str = input.next();

                // we keep just first letter
                if (str.length() > 1) {
                    str = str.substring(0, 1);
                }

                // update word found
                enter(str);

                // display current state
                System.out.println("\n" + wordFoundList());

                // check if word is found
                if (wordFound()) {
                    System.out.println("\nYou win!");
                    break;
                } else {
                    // we display nb tries remaining for the user
                    System.out.println("\n=> Nb tries remaining : " + (maxTry - try1));
                }
            }

            if (try1 == maxTry) {
                // user lost
                System.out.println("\n K.O");
                System.out.println("=> Word to find was : " + wordToFind);
            }
        }
    }

    public static void main(String[] args) {
        hangman hangmanGame = new hangman();
        hangmanGame.newGame();
        hangmanGame.play();
    }

}