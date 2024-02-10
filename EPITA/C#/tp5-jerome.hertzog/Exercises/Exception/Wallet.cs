using System;

namespace Exception
{
    public class Wallet
    {
        // Exception to be thrown when you are out of balance
        class YouAreBrokeException : System.Exception
        {
        }

        // Exception to be thrown when you have deposited too much cash into your wallet
        class IllegalGamblingException : System.Exception
        {
        }

        // Random variable used in RandomTransaction
        private Random random = new Random();

        // Current wallet balance, is 0 initially
        private int balance = 0;

        // Maximum wallet balance
        private int maxBalance;

        // Wallet Constructor taking maximum wallet balance as argument
        // maxBalance must be a positive integer
        public Wallet(int maxBalance)
        {
            if (maxBalance < 0)
            {
                throw new ArgumentOutOfRangeException();
            }
            this.maxBalance = maxBalance;
        }

        // Randomly deposit into or withdraw from wallet
        // Prints wallet status and transaction on the Console
        public void RandomTransaction()
        {
            int randomAmount = random.Next(-1000, 500);
            Console.WriteLine("Current balance is " + balance + "/" + maxBalance + ".");
            if (randomAmount < 0)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Withdrawing " + (-randomAmount) + ".");
                Console.ResetColor();
                Withdraw(-randomAmount);
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Depositing " + randomAmount + ".");
                Console.ResetColor();
                Deposit(randomAmount);
            }
        }

        // Withdraw the given amount from the wallet
        public void Withdraw(int amount)
        {
            balance -= amount;
            if (balance < 0)
                throw new YouAreBrokeException();
        }

        // Deposit the given amount into the wallet
        public void Deposit(int amount)
        {
            balance += amount;
            if (balance > maxBalance)
                throw new IllegalGamblingException();
        }

        // Calls RandomTransaction in an infinite loop
        // until YouAreBrokeException or IllegalGamblingException is thrown
        public void Gamble()
        {
            do
            {
                try
                {
                    RandomTransaction();
                }
                catch (YouAreBrokeException)
                {
                    Console.WriteLine("You are broke.");
                    break;
                }
                catch (IllegalGamblingException)
                {
                    Console.WriteLine("Gambling is bad.");
                    break;
                }
            } while (balance > 0 || balance < maxBalance);
        }
    }
}
