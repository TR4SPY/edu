import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.IOException;

public class MyConnectFour {
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_RESET = "\u001B[0m";

    public void MyConnectFour() {
        playGame();

    }

    private void playGame() {

        System.out.println(ANSI_YELLOW + "Welcome to Connect 4");
        System.out.println("There are 2 players red and yellow");
        System.out.println("Player 1 is Red, Player 2 is Yellow");
        System.out.println("To play the game type in the number of the column you want to drop you counter in");
        System.out.println("A player wins by connecting 4 counters in a row - vertically, horizontally or diagonally");
        System.out.println("" + ANSI_RESET);

        Board board = new Board(6, 7);
        View view = new CommandLineView();
        view.display(board.toString());
        System.out.print("Human Player's turn: ");  
      
        //  Add players to the game
        ArrayList < Player > players = new ArrayList < > ();
        players.add(new Human('R'));
        players.add(new ComputerPlayer('Y'));
        //  To add another Computer player uncomment the code below: 
        //  players.add(new ComputerPlayer('B'));
        int currentPlayer = 0;

        boolean win = false;
        while (!win) {
            int position = players.get(currentPlayer).getMove();
            //  In case a number that is outside the range 1 to 7 is type in the terminal the game breaks, else the game continues
            if (position == 0 || position > 7) {
                System.out.println("not a valid number start again");
                break;
            } else {
                board.placeCounter(players.get(currentPlayer).getToken(), position);
                System.out.print("\033[H\033[2J");  //  Clear the console view
              view.display(board.toString());
              System.out.print("Human Player's turn: ");
                board.checkCount(players.get(currentPlayer).getToken());
                if (board.checkCount(players.get(currentPlayer).getToken()) == true) {
                    win = true;
                  System.out.print("\033[H\033[2J");  //  Clear the console view
                    System.out.println(players.get(currentPlayer).getToken() + " is winner !!!");
                } else {
                    currentPlayer = (currentPlayer + 1) % players.size();
                }
            }
        }

    }

}
