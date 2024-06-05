import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Human extends Player {

    private BufferedReader input;

    public Human(char token) {
        super(token);
        input = new BufferedReader(new InputStreamReader(System.in));
    }

    public int getMove() {
        try {
            return Integer.parseInt(input.readLine());
        } catch (Exception e) {
            return -1;
        }

    }

}
