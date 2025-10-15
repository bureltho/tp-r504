// ServeurTCP2.java
import java.net.*;
import java.io.*;

public class ServeurTCP2 
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
				System.out.println("Message: " + dIn.readUTF());
				socket.close();
				}
			} 
		catch (IOException e) 
		{
		System.err.println("Erreur serveur: " + e.getMessage());
		}
	}
}

