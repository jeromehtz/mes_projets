using System;
using System.Security.Policy;

namespace Basics
{
    public class MoreOrLess
    {
        static bool CheckNumber(int input, int number)
        {
            return input == number;
        }

        static bool Game(int number, int tries)
        {
            string nombre = Console.ReadLine();
            int nv_nbr = Int32.Parse(nombre);
            while (!CheckNumber(nv_nbr,number) && tries != 1)
            { 
                tries -= 1;
                nombre = Console.ReadLine();
                nv_nbr = Int32.Parse(nombre);
            }

            if (nv_nbr==number)
                return true;
            return false;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Vous avez demmare une nouvelle partie.");
            
            //ouverture de la classe Random
            Random value = new Random();
            
            //variables
            int essais = 20;
            int maison = 0;
            int village = 0;
            int tours = 0;

            while (essais != 0)
            {
                tours += 1;
                int new_value = value.Next(5);
                Console.WriteLine("Quel est mon chiffre?");
                bool res = Game(new_value, 3);
                if (res && maison == 3)
                {
                    village += 1;
                    maison = 0;
                    Console.WriteLine("Vous venez de construire un village.");
                }
                else if (res)
                {
                    maison += 1;
                    Console.WriteLine("Vous venez de construire une maison.");
                }
                else
                {
                    Console.WriteLine("Mon chiffre etait : "+new_value);
                }
                essais -= 1;
                Console.WriteLine(tours+"****");
            }

            if (village >= 3)
            {
                Console.WriteLine("Vous avez gagne.");
                Console.WriteLine("Vous avez construit " + village + "villlages.");
            }

            else
            {
                Console.WriteLine("Vous avez perdu.");
                Console.WriteLine("Vous avez construit "+ village +" villlage(s).");
            }

        }
    }
}