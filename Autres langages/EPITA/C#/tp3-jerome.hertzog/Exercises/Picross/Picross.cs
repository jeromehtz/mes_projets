using System;
using System.Diagnostics.CodeAnalysis;
using System.Xml.Linq;

namespace Picross
{
    public class Picross
    {
        public static int GetMaxLine(bool[,] solution)
        {
            int max_line = 0;
            int length = solution.GetLength((0));
            for (int i = 0; i < length; i++)
            {
                int compteur = 0;
                bool booleen = false;
                for (int j = 0; j < length; j++)
                {
                    switch (solution[i,j])
                    {
                        case true when booleen==false:
                            compteur += 1;
                            booleen = true;
                            break;
                        case false:
                            booleen = false;
                            break;
                    }
                }
                //Console.WriteLine(compteur);
                if (compteur > max_line)
                    max_line = compteur;
            }
            return max_line;
        }
        public static int GetMaxCol(bool[,] solution)
        {
            int max_line = 0;
            bool booleen = false;
            int length = solution.GetLength((0));
            for (int i = 0; i < length; i++)
            {
                int compteur = 0;
                for (int j = 0; j < length; j++)
                {
                    switch (solution[j,i])
                    {
                        case true when booleen==false:
                            compteur += 1;
                            booleen = true;
                            break;
                        case false:
                            booleen = false;
                            break;
                    }
                }
                //Console.WriteLine(compteur);
                if (compteur > max_line)
                    max_line = compteur;
                booleen = false;
            }
            return max_line;
        }

        public static void GetSolutionColPrint(bool[,] solution, int index, int count)
        {
            // FIXME
            throw new NotImplementedException();
        }
        public static int[] GetSolutionLinePrint(bool[,] solution, int index)
        {
            // FIXME
            throw new NotImplementedException();
        }
        
        public static void PrintGrid(string[,] grid, bool[,] solution)
        {
            // FIXME
            throw new NotImplementedException();
        }

        public static bool IsSolved(string[,] grid, bool[,] solution)
        {
            // FIXME
            throw new NotImplementedException();
        }

        public static bool PutCell(int x, int y, string value, string[,] grid, bool[,] solution)
        {
            // FIXME
            throw new NotImplementedException();
        }
        public static void Game(bool[,] solution)
        {
            // FIXME
            throw new NotImplementedException();  
        }
    }
}