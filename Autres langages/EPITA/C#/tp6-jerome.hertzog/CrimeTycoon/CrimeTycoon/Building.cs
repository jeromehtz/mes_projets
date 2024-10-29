using System;

namespace CrimeTycoon
{
	public abstract class Building
	{
		public enum BuildingType
		{
			EMPTY, HOUSE, PRISON, OFFICE
		}
		
		protected int level;
		protected BuildingType buildingType;
		
		public abstract bool IsUpgradable();
		public abstract bool Upgrade(ref long money);
		public abstract char GetBuildingChar();
		public abstract ConsoleColor GetBuildingColor();

		//getters
		public int Level => level;
		public BuildingType GetBuildingType => buildingType;
	}
	
	public class EmptySpace : Building
	{
		private static readonly ConsoleColor clr = Console.BackgroundColor;
		public EmptySpace()
		{
			buildingType = BuildingType.EMPTY;
			level = 0;
		}
		
		public override bool IsUpgradable()
		{
			return false;
		}

		public override bool Upgrade(ref long money)
		{
			return false;
		}

		public override char GetBuildingChar()
		{
			return '0';
		}

		public override ConsoleColor GetBuildingColor()
		{
			return clr;
		}
	}
}