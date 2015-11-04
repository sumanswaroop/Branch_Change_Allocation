package Java;
import java.util.*;
import java.io.*;

// Making a class to represent each and every Branch in Institute
public class Programme{
	private String branch;
	private float alpha;
	private float beta;
	public int seatsOccupied;
	private int initialSeats;
	private int sanctionedSeats;
	public int minSeats;
	public int maxSeats;
	public float cutoff;
	public float blockedCutOff;
	public Boolean blocked;


	// Parametrized constructor for the class Programme
	public Programme(String branch, float alpha, float beta, int initialSeats, int seatsOccupied){
		this.branch = branch;
		this.alpha = alpha;
		this.beta = beta;
		this.initialSeats = initialSeats;
		this.sanctionedSeats = seatsOccupied;
		this.seatsOccupied = seatsOccupied;
		cutoff = 11.0f;
		blocked = false;
		minSeats = Math.round(initialSeats*alpha);
		maxSeats = Math.round(initialSeats*beta);
		blockedCutOff = 0f;
	}

	// Copy Constructor for the class Programme
	public Programme(Programme thisone) {
		branch = thisone.branch ;
		alpha = thisone.alpha ;
		beta = thisone.beta ;
		seatsOccupied = thisone.seatsOccupied ;
		initialSeats = thisone.initialSeats ;
	}

	//Now making the functions to retrive the values of the private variables
	public String getBranch(){
		return this.branch;
	}

	public int getSanctionedSeats(){
		return this.sanctionedSeats;
	}

	public int getInitialSeats(){
		return this.initialSeats;
	}

}
