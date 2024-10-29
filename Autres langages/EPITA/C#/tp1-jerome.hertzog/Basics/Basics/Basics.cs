using System;

namespace Basics
{
    public static class Basics
    {
        public static void Parrot(int count, string str)
        {
            while (count!=0)
            {
                Console.WriteLine("To a great mind, nothing is little.");
                count-=1;
            }
        }

        public static void Introduction(string name, uint age, string city, string work)
        {
            Console.WriteLine("Hello, my name is "+ name +", I am "+ age +", I live in "+ city +" and I work in "+ work+".");
        }
 
        public static void Ground()
        {
            int nbr_char = 13;
            while (nbr_char != 0)
            {
                if (nbr_char == 13 || nbr_char == 1)
                    Console.Write("|");
                else if (nbr_char == 7)
                    Console.Write("_");
                else
                {
                    Console.Write(" ");
                }

                nbr_char -= 1;
            }
            
            Console.Write("\n");
            int nbr_char1 = 13;
            while (nbr_char1 != 0)
            {
                if (nbr_char1 == 13 || nbr_char1 == 1 || nbr_char1 == 6 || nbr_char1 == 8)
                    Console.Write("|");
                else
                {
                    Console.Write(" ");
                }

                nbr_char1 -= 1;
            }
            Console.Write("\n");
            int nbr_char2 = 13;
            while (nbr_char2 != 0)
            {
                if (nbr_char2 == 13 || nbr_char2 == 1 || nbr_char2 == 6 || nbr_char2 == 8)
                    Console.Write("|");
                else
                {
                    Console.Write("_");
                }

                nbr_char2 -= 1;
            }

        }

        public static void Roof()
        {
            int nbr_char = 13;
            while (nbr_char != 0)
            {
                if (nbr_char == 13 || nbr_char == 1)
                    Console.Write(" ");
                else
                {
                    Console.Write("-");
                }

                nbr_char -= 1;
            }

        }

        public static void Floor(int nb)
        {
            Console.Write("\n");
            while (nb != 0)
            {
                int nbr_char3 = 13;
                while (nbr_char3 != 0)
                {
                    if (nbr_char3 == 13 || nbr_char3 == 1)
                        Console.Write("|");
                    else
                    {
                        Console.Write(" ");
                    }
                    nbr_char3 -= 1;
                }
                Console.Write("\n");
                int nbr_char = 13;
                while (nbr_char != 0)
                {
                    if (nbr_char == 13 || nbr_char == 2)
                        Console.Write("|");
                    if (nbr_char==5 || nbr_char==11)
                        Console.Write("_");
                    else
                    {
                        Console.Write(" ");
                    }
                    nbr_char -= 1;
                }
                Console.Write("\n");
                
                int nbr_char1 = 13;
                while (nbr_char1 != 0)
                {
                    if (nbr_char1 == 1 || nbr_char1 == 3 || nbr_char1 == 5 || nbr_char1 == 9 || nbr_char1 == 11 || nbr_char1 == 13)
                        Console.Write("|");
                    else if (nbr_char1==4 || nbr_char1==10)
                        Console.Write("o");
                    else
                    {
                        Console.Write(" ");
                    }
                    nbr_char1 -= 1;
                }
                Console.Write("\n");
                
                int nbr_char2 = 13;
                while (nbr_char2 != 0)
                {
                    if (nbr_char2 == 1 || nbr_char2 == 3 || nbr_char2 == 5 || nbr_char2 == 9 || nbr_char2 == 11 || nbr_char2 == 13)
                        Console.Write("|");
                    else if (nbr_char2==4 || nbr_char2==10)
                        Console.Write("o");
                    else
                    {
                        Console.Write(" ");
                    }
                    nbr_char2 -= 1;
                }

                nb -= 1;
                Console.Write("\n");
            }
        }
    }
}
