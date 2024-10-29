using System;

namespace Basics
{
    public static class Basics
    {
        public static void HelloWorld()
        {
            // FIXME
            Console.WriteLine("Hello World !\n");
        }

        public static void Welcome()
        {
            Console.WriteLine("Hello, what's your name?");
            String name = Console.ReadLine();
            Console.Write("Welcome to 221B Baker Street, "+name);
            Console.Write("!");
        }

        public static void ComputeAge()
        {
            Console.WriteLine("What's your year of birth?");
            String number = Console.ReadLine();
            int number_int = Int32.Parse(number);
            int age = 2022 - number_int;
            Console.Write("It looks like you're around "+age);
            Console.Write("!");
        }

        public static int Absolute(int x)
        {
            return -1 * x;
        }

        public static double Pow(double x, int n)
        {
            if (n<0)
                Console.WriteLine("Pow : Puissance negative");
            else if (n==0)
            {
                return 1;
            }
            else
            {
                return x * Pow(x, n - 1);
            }

            return 0;
        }

        public static uint Factorial(uint n)
        {
            if (n <= 0)
                return 1;
            return n * Factorial(n - 1);
        }

        public static bool IsPrime(uint n)
        {
            static bool Aux(uint d, uint n)
            {
                if (d % n == 0)
                {
                    return false;
                }

                if (d == 1)
                {
                    return true;
                }

                return Aux(d-1,n);

            }

            return Aux(n - 1, n);
        }

        //a modifier :
	    public static int GetCharPos(string str, char c)
        {
            static int Aux(int pos, string str, char c, int length)
            {
                if (pos == length)
                    return -1;
                if (str[pos] == c)
                    return pos;
                return Aux(pos + 1, str, c, length);
            }

            return Aux(0, str, c, str.Length);
        }

        public static string ModifyNthChar(string str, char c, int n)
        {
            int length = str.Length;
            if (n < 0 || n>length)
                return str;

            static string Aux(int i, int n, char c, string str, int length)
            {
                if (i == length)
                    return "";
                if (i == n)
                    return c + Aux(i + 1, n, c, str, length);
                return str[i] + Aux(i + 1, n, c, str, length); 
            }

            return Aux(0, n, c, str, length);
        }

        public static uint Fibonacci(uint n)
        {
            if (n == 0 || n == 1)
                return 1;

            static uint Aux(uint i, uint inter, uint res,uint n)
            {
                if (i > n)
                    return res;
                return Aux(i + 1, res, inter + res, n);
            }

            return Aux(3, 1, 2, n);
        }

        public static bool IsPalindrome(string str)
        {
            int length = str.Length;

            static bool Aux(int i, int j, string str, int length)
            {
                if (i > j)
                    return false;
                if (i == j && str[i]==str[j])
                    return true;
                return str[i] == str[j] && Aux(i + 1, j - 1, str, length);
            }

            return Aux(0, str.Length - 1, str, length);
        }

        public static string FizzBuzz(uint n)
        {
            static string Aux(uint i, uint n)
            {
                if (i > n)
                {
                    return "";
                }

                if (i % 15 == 0)
                {
                    return ", Fizz Buzz" + Aux(i+1,n);
                }

                if (i % 3 == 0)
                {
                    return ", Fizz" + Aux(i+1,n);
                }

                if (i % 5 == 0)
                {
                    return ", Buzz" + Aux(i+1,n);
                }
                if (i==1)
                    return i + Aux(i+1,n);
                return ", " + i + Aux(i+1,n);
            }

            return Aux(1, n);
        }

        public static void ComputeRealAge()
        {
            //fait sur la base du 16 avril 2022
            Console.WriteLine("What's your year of birth?");
            string year = Console.ReadLine();
            int year_int = Int32.Parse(year);
            int res = 2022 - year_int;
            
            Console.WriteLine("What's your month of birth?");
            string month = Console.ReadLine();
            int month_int = Int32.Parse(month);

            Console.WriteLine("What's your day of birth?");
            string day = Console.ReadLine();
            int day_int = Int32.Parse(day);
            if (month_int > 4)
                res -= 1;
            else if (day_int > 16 && month_int == 4)
                res -= 1;
            Console.WriteLine("Looks like you're exactly "+res+"!");
            
        }
    }
}
