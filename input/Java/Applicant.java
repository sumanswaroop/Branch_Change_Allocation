package Java;
import java.io.*;
import java.util.*;

/* First of all we start with a class for students who are applying for branch change,
	the class contains the information about the student and also his preference list.
	*/
public class Applicant{

	// Personal and Academic Related Information
	private float CPI;
	private String name;
	private String rollNo;
	private String category;
	public String init;
	public boolean eligible;
	// Programme Related Information
	private int hither;
	private boolean waiting;
	private Programme currBranch;
	private Programme waitingForThis;
	private ArrayList<Programme> preferenceList;
	private ArrayList<Programme> hahaha;

	// Parametrized Construtor of class Applicant
	public Applicant(String rollNo, String name, String category, Programme currBranch){
		this.rollNo = rollNo;
		this.name = name;
		this.category = category;
		this.currBranch = currBranch;
		this.hither = 0;
		this.waiting = false;
		preferenceList = new ArrayList<Programme>();
		init = currBranch.getBranch();
	}

	// Copy Constructor the class Applicant
	public Applicant(Applicant thisOne){
		rollNo = thisOne.rollNo;
		name = thisOne.name;
		category = thisOne.category;
		currBranch = thisOne.currBranch;
		CPI = thisOne.CPI;
		preferenceList = new ArrayList<Programme>(thisOne.preferenceList);   
		hither = thisOne.hither;
		waiting = thisOne.waiting;
	}

	// Functions To Return the values of the variables
	public String getRollNo(){
		return this.rollNo;
	}

	public boolean getWaiting(){
		return waiting;
	}

	public String getName(){
		return this.name;
	}

	public float getCPI(){
		return this.CPI;
	}

	public String getCategory(){
		return this.category;
	}

	public int getHither(){
		return this.hither;
	}

	public Programme getCurrProgramme(){
		return this.currBranch;
	}

	public Programme getChoice(){
		return this.preferenceList.get(hither);
	}

	// Now making functions to set variables
	public void setHither(int thisOne){
		hither = thisOne;
	}

	public void setWaitingFor(Programme thisOne){
		currBranch = thisOne;
	}

	public Programme giveWaitingFor(){
		return waitingForThis;
	}

	public void setWaitListedForBool(boolean thisOne){
		waiting = thisOne;
	}

	public void createPreferenceList1(Programme choice){
		this.preferenceList.add(choice);
	
	}
	// Suppose the Applicant was not alloted his last seat, then we move on the next choice
	public int nextAppliedProgramme(){
		hither += 1;
		if (hither < preferenceList.size() );
		else if ( hither == preferenceList.size())
		{
			// Remove Applicant,  ||  Sorry Rahega
			hither = -1;
			return -1;
		}
		return 0;
	}
	public void addCPI(float cpi)
	{
		CPI = cpi;
	}
}




