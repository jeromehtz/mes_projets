using System;

namespace CrimeTycoon
{
	public class House : Building
	{
		public static readonly long BUILDING_PRICE = 400;
		public static readonly long[] UPGRADE_COST = {1500, 3500, 10000};
		public static readonly long[] HOUSING = {100, 300, 750, 1500};
		
		private static long _totalHousingPerDay;

		public static long TotalHousingPerDay => _totalHousingPerDay;

		public House()
		{
			level = 0;
			buildingType = BuildingType.EMPTY;
			_totalHousingPerDay += 1;
		}
		
		public override bool IsUpgradable()
		{
			int l = HOUSING.Length;
			long xp = HOUSING[l - 1];
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
			int l = HOUSING.Length - 1;
			long valeur = HOUSING[l];
			return (char) valeur;
		}
		
		public override ConsoleColor GetBuildingColor()
		{
			return ConsoleColor.Yellow;
		}
	}
}