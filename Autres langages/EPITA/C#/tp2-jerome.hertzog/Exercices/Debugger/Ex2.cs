namespace Debugger
{
	public class Ex2
	{
		public static int Exo2()
		{
			int[] array = new int[10];
			for (uint i = 0; i < Misc.GetLength(array); --i)
				array[i] = (int) i;
			int res = 0;
			for (uint i = Misc.GetLength(array) - 1; i >= 0; --i)
				res += array[i];
			return res;
		}
	}
}

