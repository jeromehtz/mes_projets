using System;

namespace CrimeTycoon
{
	public class TestBot: Bot
	{
		public override void Start(Game game)
		{
			/*
			Console.ForegroundColor = ConsoleColor.Blue;
			// Building a house, check money
			Console.WriteLine(" - Building a House in (1, 1): {0} (should be True)", 
							game.Build(Building.BuildingType.HOUSE, 1, 1));
			Console.WriteLine("Current money: {0} (should be: 3600)", game.Money);
			// Building a prison, check money
			Console.WriteLine(" - Building a Prison in (0, 1): {0} (should be True)", 
							game.Build(Building.BuildingType.PRISON, 0, 1));
			Console.WriteLine("Current money: {0} (should be: 2400)", game.Money);
			// Attempting to build where it is impossible
			Console.WriteLine(" - Attempting to build an Office in (1, 1): {0} (should be False)", 
							game.Build(Building.BuildingType.OFFICE, 1, 1));
			Console.WriteLine("Current money: {0} (should be: 2400)", game.Money);
			// Upgrading a House
			Console.WriteLine(" - Upgrading the house in (1, 1): {0} (should be True)", 
							game.Upgrade(1, 1));
			Console.WriteLine("Current money: {0} (should be: 900)", game.Money);
			// Attempting to build a Prison but not enough money
			Console.WriteLine(" - Attempting to build a Prison in (0, 0): {0} (should be False)", 
							game.Build(Building.BuildingType.PRISON, 0, 0));
			Console.WriteLine("Current money: {0} (should be: 900)", game.Money);
			// End of Start
			Console.WriteLine("Press Enter to keep going:");
			Console.ReadLine();
			Console.ForegroundColor = ConsoleColor.Black;
			*/
		}

		public override void Update(Game game)
		{
			/*
			Console.ForegroundColor = ConsoleColor.Blue;
			if (game.Day == 1)
			{
				Console.WriteLine(@"Total population should be 300 (0 disappearance, 300 arrivals)
Total cells should be: 10 (10 new cells)
Total inspectors should be: 0
Current money should be: 1200 (earned 300)
");
				// Attempting to build an Office out of the map
				Console.WriteLine(" - Attempting to build an Office in (15, 0): {0} (should be False)", 
								game.Build(Building.BuildingType.OFFICE, 15, 0));
				Console.WriteLine("Current money: {0} (should be: 1200)", game.Money);
				// Attempting to build an Office out of the map
				Console.WriteLine(" - Attempting to build an Office in (0, 80): {0} (should be False)", 
								game.Build(Building.BuildingType.OFFICE, 0, 80));
				Console.WriteLine("Current money: {0} (should be: 1200)", game.Money);
				// Building an Office
				Console.WriteLine(" - Attempting to build an Office in (1, 0): {0} (should be True)", 
								game.Build(Building.BuildingType.OFFICE, 1, 0));
				Console.WriteLine("Current money: {0} (should be: 400)", game.Money);
			}
			else if (game.Day == 2)
			{
				Console.WriteLine(@"Total population should be 540 (60 disappearance, 300 arrivals)
Total cells should be: 20 (10 new cells)
Total inspectors should be: 20 (20 new inspectors)
Current money should be: 940 (earned 540)
");
				Console.WriteLine(" - Building a House in (1, 2): {0} (should be True)", 
								game.Build(Building.BuildingType.HOUSE, 1, 2));
				Console.WriteLine("Current money: {0} (should be: 540)", game.Money);
			}
			else if (game.Day == 3)
			{
				Console.WriteLine(@"Total population should be 852 (88 disappearance, 400 arrivals)
Total cells should be: 30 (10 new cells)
Total inspectors should be: 40 (20 new inspectors)
Current money should be: 1392 (earned 852)
");
			}
			else
			{
				Console.ForegroundColor = ConsoleColor.Black;
				return;
			}
			// End of Update
			Console.WriteLine("Press Enter to keep going:");
			Console.ReadLine();
			Console.ForegroundColor = ConsoleColor.Black;
			*/
		}
	}
}