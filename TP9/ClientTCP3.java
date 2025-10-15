// ClientTCP3.java
import java.net.*;
import java.io.*;

public class ClientTCP3 
	{
	public static void main(String[] args) 
		{
		try 
			{
			Socket socket = new Socket("localhost", 2016);
			DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
			dOut.writeUTF(args[0]);
			System.out.println("Message envoyé: " + args[0]);
			DataInputStream dIn = new DataInputStream(socket.getInputStream());
			String response = dIn.readUTF();
			System.out.println("Réponse du serveur: " + response);
			socket.close();
			}
		 catch (IOException e) 
		{
		System.err.println("Erreur client: " + e.getMessage());
		}
	}
}

