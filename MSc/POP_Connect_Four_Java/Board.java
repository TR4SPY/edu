public class Board {
    private char[][] board;
    boolean hasWon = false;

    //  Constructor
    public Board(int row, int col) {
        board = new char[row][col + 1];
    }

    //  Return a string that could later be printed in the terminal representing the board
    public String toString() {
        String toReturn = "";
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length - 1; j++) {
                char a = board[i][j];
                if (a != 0) {
                    toReturn += ("| " + a + " ");
                } else {
                    toReturn += ("|   ");
                }
            }
            toReturn += ("|");
            toReturn += "\n";

        }
        toReturn += ("  1   2   3   4   5   6   7");
        return toReturn;
    }

    //  Place counter in the board, the parameters are the colour/token of the player and the position the player wants to move
    public boolean placeCounter(char player, int position) {
        boolean placed = false;
        for (int i = board.length - 1; i >= 0; i--) {
            if (!placed) {
                if (board[i][position - 1] == 0) {
                    board[i][position - 1] = player;
                    placed = true;
                } else {
                    // Skip
                }
            }
        }
        return placed;
    }

    //  Check counter, it return a boolean, true if one of them won, or false if nobody is winning
    //  Parameter colour, is the token/colour of the player
    public boolean checkCount(char colour) {
        int count = 0;
    //  ConnectN test variable
        int n = 4;

        //  Diagonals check if there are 4 equal tokens together w
        for (int i = 0; i < board.length; i++) {
            count = 0;
            for (int j = i, k = 0; j < board.length && k < board[0].length; j++, k++) {
                if (board[j][k] == colour) {
                    count = count + 1;
                    if (count >= n) {
                        hasWon = true;
                    }
                } else {
                    count = 0;
                }
            }
        }

        for (int i = 1; i < board[0].length; i++) {
            count = 0;
            for (int j = 0, k = i; j < board.length && k < board[0].length; j++, k++) {
                if (board[j][k] == colour) {
                    count = count + 1;
                    if (count >= n) {
                        hasWon = true;
                    }
                } else {
                    count = 0;
                }
            }
        }

        for (int i = 0; i < board[0].length; i++) {
            count = 0;
            for (int j = board.length - 1, k = i; j >= 0 && k < board[0].length; j--, k++) {
                if (board[j][k] == colour) {
                    count = count + 1;
                    if (count >= n) {
                        hasWon = true;
                    }
                } else {
                    count = 0;
                }
            }
        }

        for (int i = board.length - 2; i >= 0; i--) {
            count = 0;
            for (int j = i, k = 0; j >= 0 && k < board[0].length; j--, k++) {
                if (board[j][k] == colour) {
                    count = count + 1;
                    if (count >= n) {
                        hasWon = true;
                    }
                } else {
                    count = 0;
                }
            }
        }

        //  Horizontal check if there are 4 equal tokens next to each other
        count = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == colour) {
                    count = count + 1;
                    if (count >= n) {
                        hasWon = true;
                    }
                } else {
                    count = 0;;
                }
            }
        }

        //  Vertical check if there are 4 equal tokens next to each other
        count = 0;
        for (int i = 0; i < board[0].length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[j][i] == colour) {
                    count = count + 1;
                    if (count >= n) {
                        hasWon = true;
                    }
                } else {
                    count = 0;;
                }
            }

        }

        return hasWon;

    }

}
