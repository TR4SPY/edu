import java.util.Random;

public class ComputerPlayer extends Player {

    private Random randN;

    public ComputerPlayer(char token) {
        super(token);
        randN = new Random();
    }

    public int getMove() {
        return (randN.nextInt(6) + 1);
    }
}
