package Java;
import java.io.*;
import java.util.*;

public class AnotherList{
	
	private ArrayList<Applicant> cpiList;	
	// Constructor
	public AnotherList(){
		cpiList = new ArrayList<Applicant>();
	}


	//Functions for accessing data members
	public ArrayList<Applicant> getcpiList(){
		return cpiList;
	}

	//Function for adding Applicant
	public void addApplicant(Applicant appli){
		cpiList.add(appli);
	}

	public int size(){
		return cpiList.size();
	}
	
	public void sortList(){
		Collections.sort(cpiList, new Comparator<Applicant>() {
	        @Override
	        public int compare(Applicant appli1, Applicant appli2)
	        {
	        	if(appli1.getCPI() < appli2.getCPI())
	        		return 1;
	        	else
	        		return -1;
	        }
    	});
	}
}
