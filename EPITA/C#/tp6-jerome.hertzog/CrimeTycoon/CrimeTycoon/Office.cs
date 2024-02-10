using System;

namespace CrimeTycoon
{
	public class Office : Building
	{
		public static readonly long BUILDING_PRICE = 800;
		public static readonly long[] UPGRADE_COST = {3000, 10000, 40000};
		public static readonly long[] DESKS = {20, 55, 100, 150};

		private static long _totalInspectorPerDay;

		public static long TotalInspectorPerDay => _totalInspectorPerDay;
		
		// TODO: FIX ME
		
		public Office()
		{
			level = 0;
			buildingType = BuildingType.EMPTY;
			_totalInspectorPerDay += 1;
		}
		
		public override bool IsUpgradable()
		{
			int l = DESKS.Length;
			long xp = DESKS[l - 1];
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
			int l = DESKS.Length - 1;
			long valeur = DESKS[l];
			return (char) valeur;
		}

		public override ConsoleColor GetBuildingColor()
		{
			return ConsoleColor.Green;
		}
	}
}