// ServeurTCP3.java
import java.net.*;
import java.io.*;

public class ServeurTCP3 
	{
	public static void main(String[] args) 
		{
		try 
			{
			ServerSocket socketserver = new ServerSocket(2016);
			System.out.println("Serveur en attente");
			while(true) 
				{
				Socket socket = socketserver.accept();
				System.out.println("Connexion d'un client");
				DataInputStream dIn = new DataInputStream(socket.getInputStream());
				String msg = dIn.readUTF();
				System.out.println("Message reçu: " + msg);
				String rev = new StringBuilder(msg).reverse().toString();
				System.out.println("Message inversé: " + rev);
				DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
				dOut.writeUTF(rev);
				socket.close();
				}
			} 
		catch (IOException e) 
		{
		System.err.println("Erreur serveur: " + e.getMessage());
		}
	}
}

