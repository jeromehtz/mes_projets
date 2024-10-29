using System;

namespace CrimeTycoon
{
	public class Map
	{
		//attributs
		private Building.BuildingType[,] map;
		private long _population;
		private long _cells;
		private long _inspectors;
		
		//getters
		public Building.BuildingType[,] Mapp => map;
		public long Population => _population;
		public long Cells => _cells;
		public long Inspectors => _inspectors;
		
		

		public Map(int height, int width)
		{
			height = map.Length;
			width = map.GetLength(0);
		}

		public long NewDay()
		{
			_population = _population + House.TotalHousingPerDay - Prison.TotalCellsPerDay;
			_cells = Prison.TotalCellsPerDay;
			_inspectors = Office.TotalInspectorPerDay;
			return _population - (House.TotalHousingPerDay + Prison.TotalCellsPerDay);
		}

		public bool Build(Building.BuildingType buildingType, int i, int j, ref long money)
		{
			if (map[i, j] == Building.BuildingType.EMPTY)
			{
				map[i, j] = buildingType;
				return true;
			}
			return false;
		}

		public bool Upgrade(int i, int j, ref long money)
		{
			if (map[i, j] == Building.BuildingType.HOUSE)
			{
				House batiment = new House();
				batiment.Upgrade(ref money);
				return true;
			}

			if (map[i, j] == Building.BuildingType.PRISON)
			{
				Prison batiment = new Prison();
				batiment.Upgrade(ref money);
				return true;
			}
			return false;
		}

		public void PrintMap()
		{
			for (int i = 0; i < map.Length; i++)
			{
				for (int j = 0; j < map.GetLength(i); j++)
				{
					Console.Write(map[i,j]);
				}
				Console.Write("\n");
			}
		}
		
	}
}