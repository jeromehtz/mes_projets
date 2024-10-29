using System;

namespace Picross
{
    class Program
    {
        static void Main(string[] args)
        {
            bool[,] test =
            {
                {false, false, false, false, true, true, false, false, false, false},
                {false, false, false, true, false, true, true, false, false, false},
                {false, false, true, false, true, true, true, false, false, false},
                {false, true, false, true, false, true, true, false, false, false},
                {false, true, false, true, false, true, true, false, false, false},
                {true, true, false, true, false, true, true, false, false, false},
                {true, true, false, true, true, true, true, false, false, false},
                {true, false, false, false, false, false, false, false, false, false},
                {true, false, false, true, false, false, true, false, false, false},
                {true, true, true, true, true, true, true, true, true, true}
            };
                
            string[,] solved = 
            {
                {" "," "," "," ","O","O"," "," "," "," " },
                {" "," "," ","O"," ","O","O"," "," "," "},
                {" ","O"," ","O","O","O","O"," "," "," "},
                {" ","O"," ","O"," ","O","O"," "," "," "},
                {" ","O"," ","O"," ","O","O"," "," "," "},
                {"O","O"," ","O"," ","O","O"," "," "," "},
                {"O","O"," ","O","O","O","O"," "," "," "},
                {"O"," "," "," "," "," "," "," "," "," "},
                {"O"," "," ","O"," "," ","O"," "," "," "},
                {"O","O","O","O","O","O","O","O","O","O"} 
            };
            Console.WriteLine(Picross.GetMaxCol(test));
        }
    }
}
