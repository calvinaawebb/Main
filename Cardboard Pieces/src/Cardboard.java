import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Cardboard {
	public static String place = "Start";
	public static ArrayList<String> places = new ArrayList<String>();
	public static String gamemode = "";
	public static ArrayList<String> pieces = new ArrayList<String>();
	
    public static void main(String[] args) {
    	System.out.println("This is the Cardboard Piece finding simulator");
    	System.out.println("Depending on your gamemode, go on an adventure to find out your morality in a short story, or in a long one.");
    	System.out.println("Type 'S' if you would like the first gamemode and 'L' if you want the second gamemode.");
        Gamemode();
    }
    static void Gamemode() {
    	Scanner inpg = new Scanner(System.in);
    	System.out.print(">");
    	String outg = inpg.nextLine();
    	System.out.println(outg);
    	if (outg == "S") {
    		gamemode = "S";
    	} else {
    		gamemode = "L";
    	}
    	Start();
    }
    static void Start() {
    	System.out.println("Use the 'move' command to move from place to place");
    	System.out.println("Use the 'look' command to look at avaliable places/pieces");
    	System.out.println("In each area there will be a set of pieces");
    	System.out.println("Each piece yeilds a different path, choose your adventure and discover your morality");
    	System.out.println("Use the 'choose' command with one of the piece names to choose that piece");
    	System.out.println("Use the 'status' command to see your morality status");
    	Collections.addAll(pieces, "Lobby Level, No Pieces");
    	Collections.addAll(places, "Red Terminal", "Blue Terminal", "Green Terminal");
    	System.out.println(places);
    	System.out.println(pieces);
    	Boolean terminate = true;
    	while (terminate) {
    		Scanner inp = new Scanner(System.in);
            System.out.print(">");
            String outp = inp.nextLine();
            if (outp.equals("look")) {
            	System.out.println("Places:" + places);
            	System.out.println("Pieces:" + pieces);
            } else if (outp.charAt(0) == 'm') {
            	String[] outpp = outp.split("@", 2);
            	System.out.println(outpp[1]);
            }
    	}   
    }
    static void Red_Terminal() {
    	System.out.println();
    	
    }
    static void Blue_Terminal() {
    	
    }
    static void Green_Terminal() {
    	
    }
}
			