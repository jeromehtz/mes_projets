using System;

namespace CrimeTycoon
{
	public class Game
	{
		//attributs
		private long _money;
		private int _nbDay;
		private int _day;
		private Map map;

		//getters
		public long Money => _money;
		public int NbDay => _nbDay;
		public int Day => _day;
		public Map Map => map;
		
		

		public Game(long intialMoney, int nbDay, int height, int width)
		{
			intialMoney = _money;
			nbDay = _nbDay;
			height = map.Mapp.Length;
			width = map.Mapp.GetLength(0);
		}

		public bool Build(Building.BuildingType buildingType, int i, int j)
		{
			return map.Build(buildingType, i, j,ref _money);
		}

		public bool Upgrade(int i, int j)
		{
			return map.Upgrade(i, j, ref _money);
		}
		
		public long Play(Bot bot)
		{
			Game game = new Game(_money,_nbDay,0,0);
			bot.Start(game);
			bot.Update(game);
			return _money;
		}

		public void Update()
		{
			Console.WriteLine("Day "+_day+"/"+_nbDay);
			map.PrintMap();
			Console.WriteLine("Total population: "+map.Population+" ("+Map.NewDay()+" disappeared)");
			Console.WriteLine("Total cells: "+map.Cells);
			Console.WriteLine("Total inspectors: "+map.Inspectors);
			Console.WriteLine("Current money: "+_money);
			Console.Write("Press Enter to go to next round: ");
			Console.ReadLine();
		}
	}
}