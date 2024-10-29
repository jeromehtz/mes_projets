using System;

namespace CrimeTycoon
{
	internal class Program
	{
		private const int NB_DAYS = 50;
		private const long INITIAL_MONEY = 4000;
		private const int HEIGHT = 12;
		private const int WIDTH = 70;
		
		public static void Main(string[] args)
		{
			//Game game = new Game(INITIAL_MONEY, NB_DAYS, HEIGHT, WIDTH);
			
			// Comment or remove the next two lines when you are done with the first part
			TestBuilding();
			//return;
			
			// Uncomment the commented parts in TestBot.cs in order to test the second part of the practical
			// Change "TestBot()" to "MyBot()" in order to use your own bot.
			// The current one runs tests.
			/*
			Bot bot = new TestBot();
			long score = game.Play(bot);
			Console.WriteLine("\nYour final score is {0}", score);*/
		}
		
		private static void TestBuilding()
		{
			House house = new House();
			/* Getters have many different syntax. If you can't compile, don't hesitate to add "()" or
			 * even change the name to what you chose.
			 */
			Console.WriteLine("Building type : {0} (should be : HOUSE)\nLevel of building: {1} (should be 1)", house.GetBuildingType, house.Level);
			Console.WriteLine("Total housing per day : {0} (should be 100)", House.TotalHousingPerDay);
			long money = 14000;
			Console.WriteLine("Upgrading the house: {0} (should be True)", house.Upgrade(ref money));
			house.Upgrade(ref money);
			Console.WriteLine("Upgrading the house again, current money: {0} (should be 9000)", money);
			Console.WriteLine("Trying to upgrade the house: {0} (should be False)", house.Upgrade(ref money));
			Console.WriteLine("Adding 1500 money");
			money += 1500;
			Console.WriteLine("Upgrading the house again, {0} (should be True)", house.Upgrade(ref money));
			Console.WriteLine("Current money: {0} (should be 500)", money);
			Console.WriteLine("House is upgradable: {0} (should be False)", house.IsUpgradable());
			Console.WriteLine("Current Housing per day: {0} (should be 1500)", House.TotalHousingPerDay);
		}
	}
}