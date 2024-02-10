using System;

namespace Basics
{
    class Program
    {
        static bool IsSorted(int[] list)
        {
            int i = 0;
            bool booleen = true;
            while (i<list.Length-1 &&booleen!=false)
            {
                if (list[i] <= list[i + 1])
                    booleen = true;
                else
                {
                    booleen = false;
                }
                i += 1;
            }
            return booleen;
        }

        static void Print_list(int[] list)
        {
            foreach (int element in list)
            {
                Console.Write(element+" ");
            }
        }
        static void Main(string[] args)
        {
            int[] list = new[] {1, 2, 3, 4, 9, 7, 8};
            Console.WriteLine(Basics.KingOfTheHill(list));
        }
    }
}