package Java;
import java.io.*;
import java.util.*;

public class MainList{
	private Map<String, Applicant> allApplicant;
	private ArrayList<String> doneList;
	private Map<String, Programme> allProgram;
	private AnotherList everyone;
	private AnotherList rejected;

	int  tempseats,tempoccu;
	float tempcpi;
	String tempName, tempcurrbranch, temppref, tempCategory;
	float tempbeta=1.1f, tempalpha=0.75f;
	String tempCode, tempRoll, garbage;
	Boolean yeah;

	public MainList(){
		allApplicant = new HashMap<String, Applicant>();
		doneList = new ArrayList<String>();
		allProgram = new HashMap<String, Programme>();
		everyone = new AnotherList();
		rejected = new AnotherList();
	}

	public void print(){
		try{
			PrintWriter writer = new PrintWriter("output.csv", "UTF-8");
			writer.println("RollNumber, Name, Current Branch, Destination Branch");
			for (int i=0;i<doneList.size();i++)
			{
				try{
					if(allApplicant.get(doneList.get(i)).getWaiting()){
						writer.println(doneList.get(i)+","+allApplicant.get(doneList.get(i)).getName() + ","+ allApplicant.get(doneList.get(i)).init +","+ allApplicant.get(doneList.get(i)).getCurrProgramme().getBranch());
					}
					else
					{
						writer.println(doneList.get(i)+","+allApplicant.get(doneList.get(i)).getName() +","+ allApplicant.get(doneList.get(i)).getCurrProgramme().getBranch());
					}
				}catch(NullPointerException e){}
			}
			writer.close();
		}catch(IOException e){
			System.exit(1);
		}

		try{
			PrintWriter writer = new PrintWriter("stats.csv","UTF-8");
			writer.println("Program,Cutoff,Sanctioned Strength,Original Strength,Final Strength");
			for (Map.Entry<String , Programme>  entry : allProgram.entrySet())
			{
				if (entry.getValue().getBranch().equals("Branch Unchanged")||entry.getValue().getBranch().equals("Ineligible"))
				{
					continue;
				}
				if (entry.getValue().cutoff == 11.0f)
					writer.println(entry.getValue().getBranch()+",NA,"+entry.getValue().getInitialSeats()+","+entry.getValue().getSanctionedSeats()+","+entry.getValue().seatsOccupied);
				else
					writer.println(entry.getValue().getBranch()+","+entry.getValue().cutoff+","+entry.getValue().getInitialSeats()+","+entry.getValue().getSanctionedSeats()+","+entry.getValue().seatsOccupied);
	  		}
	  		writer.close();
		}catch(IOException e){
			System.exit(1);
		}
	}

	public Applicant getApplicant(Applicant app){
		return allApplicant.get(app.getRollNo());
	}

	public void mainthing(){
		try{

			String csvFile = "programs.csv";
			BufferedReader br = null;
			String line = "";
			String csvSplitBy = ",";
			br = new BufferedReader(new FileReader(csvFile));
			while ((line = br.readLine()) != null) {
				String[] country = line.split(csvSplitBy);
				tempCode = country[0];
				tempseats = Integer.parseInt(country[1]);
				tempoccu = Integer.parseInt(country[2]);
				allProgram.put(tempCode, new Programme(tempCode, tempalpha, tempbeta, tempseats, tempoccu));
			}
			allProgram.put("Ineligible",new Programme("Ineligible", tempalpha, tempbeta, 10, 10));
			allProgram.put("Branch Unchanged",new Programme("Branch Unchanged", tempalpha, tempbeta, 10, 10));
		}catch (FileNotFoundException e) {
		} catch (IOException e) {
		} 
		try{
			String csvFile = "input.csv";
			BufferedReader br = null;
			String line = "";
			String csvSplitBy = ",";
			br = new BufferedReader(new FileReader(csvFile));
			while ((line = br.readLine()) != null) {
				String[] country = line.split(csvSplitBy);
				tempRoll = country[0];
				tempName = country[1];
				tempcurrbranch = country[2];
				tempcpi = Float.valueOf(country[3]);
				tempCategory = country[4];
				temppref = "";
				for (int i=5;i<country.length;i++)
				{
					temppref += country[i] + "-";
				}
				Programme tempp = allProgram.get(tempcurrbranch);
				Applicant newguy = new Applicant(tempRoll, tempName, tempCategory, tempp);
				if (tempCategory.equals("GE")||tempCategory.equals("OBC"))
				{
					if (tempcpi>=8.0f)
						newguy.eligible = true;
					else
						newguy.eligible = false;
				}
				else if (tempCategory.equals("ST")||tempCategory.equals("SC"))
				{
					if (tempcpi>=7.0f)
						newguy.eligible = true;
					else
						newguy.eligible = false;
				}
				doneList.add(tempRoll);
				String[] choices = temppref.split("-");
				for(int i=0;i<choices.length;i++){
					newguy.createPreferenceList1(allProgram.get(choices[i]));
				}
				allApplicant.put(tempRoll, newguy);
				allApplicant.get(tempRoll).addCPI(tempcpi);
				everyone.addApplicant(newguy);
			}
		}catch (FileNotFoundException e) {
		} catch (IOException e) {
		} 
		
		everyone.sortList();
		
		int count=0;
		Boolean check=true,complete;
		while(check)
		{
			check = false;
			for (ListIterator<Applicant> currentPointer = everyone.getcpiList().listIterator(); currentPointer.hasNext(); )
			{
				Applicant current = currentPointer.next();
				complete = false;
				getApplicant(current).setHither(0);
				if (getApplicant(current).eligible)
				{
					while(!complete && getApplicant(current).getHither()!=-1 )
					{
						if (getApplicant(current).getCurrProgramme().getBranch().equals(getApplicant(current).getChoice().getBranch()))
						{
							break;
						}
						if (getApplicant(current).getCPI()>=getApplicant(current).getChoice().cutoff || ((getApplicant(current).getCPI()>=9.0f  || getApplicant(current).getCurrProgramme().seatsOccupied >= getApplicant(current).getCurrProgramme().minSeats) && getApplicant(current).getChoice().seatsOccupied < getApplicant(current).getChoice().maxSeats && !getApplicant(current).getChoice().blocked))
						{
							getApplicant(current).setWaitListedForBool(true);
							complete = true;
							check = true;
							getApplicant(current).getChoice().seatsOccupied++;
							getApplicant(current).getCurrProgramme().seatsOccupied--;
							getApplicant(current).getChoice().cutoff = Math.min(getApplicant(current).getCPI(), getApplicant(current).getChoice().cutoff);
							getApplicant(current).setWaitingFor(getApplicant(current).getChoice());
						}
						else
						{
							getApplicant(current).nextAppliedProgramme();
						}
					}
					getApplicant(current).setHither(0);
					while (getApplicant(current).getHither()!=-1)
					{
						if (getApplicant(current).getChoice().getBranch().equals(getApplicant(current).getCurrProgramme().getBranch()))
						{
							break;
						}
						getApplicant(current).getChoice().blocked = true;
						getApplicant(current).getChoice().blockedCutOff = getApplicant(current).getCPI();
						getApplicant(current).nextAppliedProgramme();
					}
				}
				else
				{
					getApplicant(current).setWaitListedForBool(true);
					getApplicant(current).setWaitingFor(allProgram.get("Ineligible"));
					continue;
				}
			}
			for (Map.Entry<String , Programme>  entry : allProgram.entrySet())
			{
				entry.getValue().blocked = false;
				entry.getValue().blockedCutOff = 0.0f;
	  		}

		}
		for (ListIterator<Applicant> currentPointer = everyone.getcpiList().listIterator(); currentPointer.hasNext(); )
		{
			Applicant current = currentPointer.next();
			if (getApplicant(current).init.equals(getApplicant(current).getCurrProgramme().getBranch()))
			{
				getApplicant(current).setWaitListedForBool(true);
				getApplicant(current).setWaitingFor(allProgram.get("Branch Unchanged"));
			}
		}
		print();
	}
}
