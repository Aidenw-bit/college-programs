 class BankAccount
{
	//this is the fields, it tells us what an object of this class will need
	private double Balance;
	private String Owner;
	
	
	//this is the constructor, it makes the objects
	public BankAccount(double Balance, String Owner)
	{
		this.Balance = Balance;
		this.Owner =  Owner;
	}
	
	
	//these are our getter methods, they let other classes read our private objects they dont need parameters because they are in the class where they get the data
	public double getBalance()
	{
		return this.Balance;
	}
	
	public String getOwner()
	{
		return this.Owner;
	}
	
	
	//these are our methods in them we have ways to verify if the amount being taken out or added is valid, we dont want to take or add negative money nor do we want to be able to take more money then we have
	
	public void deposit(double amount)
	{
		if ( amount > 0 )
		{
			this.Balance += amount;
		}
	}
	
	public void withdrawl(double amount)
	{
		if ( amount > 0)
		{
			if ( amount <= Balance )
			{
				this.Balance -= amount;
			}
		}
	}
	
	public void transfer(double amount, BankAccount targetAccount)
	{
	    if ( amount > 0)
	    {
	        if (amount <= Balance)
	        {
	            this.withdrawl(amount);
	            targetAccount.deposit(amount);
	        }
	        
	        
	    }
	}
}


public class Main
{
	public static void main(String[] args)
	{
		BankAccount myAccount = new BankAccount(100.00, "Aiden");
		BankAccount otherAccount = new BankAccount(50.00, "Marcus");
		
		myAccount.deposit(50.00);
		
		myAccount.withdrawl(200.00);
		
	    myAccount.transfer(50.00, otherAccount);
		
		System.out.println(myAccount.getOwner() + "'s bank account has " + myAccount.getBalance() + " dollars");
		System.out.println(otherAccount.getOwner() + "'s bank account has " + otherAccount.getBalance() + " dollars");
	}
}
