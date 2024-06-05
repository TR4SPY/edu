public class CommandLineView implements View {
    public static final String ANSI_CYAN = "\u001B[36m";
    public static final String ANSI_RESET = "\u001B[0m";
    public void display(String s) {

        System.out.println(ANSI_CYAN + s + ANSI_RESET);
    }

}
