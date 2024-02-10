using System;

namespace CrimeTycoon
{
	public class Prison : Building
	{
		public static readonly long BUILDING_PRICE = 1200;
		public static readonly long[] UPGRADE_COST = {7000, 15000, 40000};
		public static readonly long[] CELLS = {10, 30, 60, 100};

		private static long _totalCellsPerDay;

		public static long TotalCellsPerDay = _totalCellsPerDay;
		
		public Prison()
		{
			level = 0;
			buildingType = BuildingType.EMPTY;
			_totalCellsPerDay += 1;
		}
		
		public override bool IsUpgradable()
		{
			int l = CELLS.Length;
			long xp = CELLS[l - 1];
			(int i, int l2) = (0, UPGRADE_COST.Length);
			while (i < l2 && xp > UPGRADE_COST[i])
			{
				i += 1;
			}

			if (i == l2)
				return false;
			return true;
		}

		public override bool Upgrade(ref long money)
		{
			if (IsUpgradable() && money>= UPGRADE_COST[0])
			{
				money -= UPGRADE_COST[0];
				return true;
			}
			return false;
		}

		public override char GetBuildingChar()
		{
			int l = CELLS.Length - 1;
			long valeur = CELLS[l];
			return (char) valeur;
		}

		public override ConsoleColor GetBuildingColor()
		{
			return ConsoleColor.Red;
		}
	}
}