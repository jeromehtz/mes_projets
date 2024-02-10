using System;

namespace Loop
{
    public class Loop
    {
        public static void PrintNaturals(uint n)
        {
            for (int i = 1; i <= n; i++)
            {
                if (i==n)
                    Console.Write(i+"\n");
                else
                {
                    Console.Write(i+" ");
                }
            }
            
        }

        public static void PrintPrimes(uint n)
        {
            for (int i = 2; i <= n; i++)
            {
                if (i == 2 || i==3 || i==5 || i==7)
                    Console.Write(i+" ");
                else if (i % 2 != 0 && i % 3 != 0 && i % 5 != 0 && i % 7 != 0)
                    Console.Write(i + " ");
            }
            Console.WriteLine();
            
        }

        public static ulong Fibonacci(ulong n)
        {
            if (n == 1 || n == 0)
                return 1;
            ulong init;
            ulong first = 1;
            ulong second = 1;
            ulong i = 2;
            while (i <= n)
            {
                init = second;
                second += first;
                first = init;
                i += 1;
            }

            return second;
        }

        public static long Factorial(uint n)
        {
            if (n == 0)
                return 1;
            long res = 1;
            for (long i = 1; i <= n; i++)
            {
                res *= i;
            }

            return res;
        }

        public static void PrintStrong(uint n)
        {
            int init = 1;
            for (uint i = 1; i <= n; i++)
            {
                uint a = i;
                uint somme = 0;
                while (a > 0)
                {
                    somme += (uint) Factorial(a % 10);
                    a /= 10;
                }
                if (somme == init)
                    Console.Write(init +" ");
                init += 1;
            }
        }

        public static long Power(long a, ulong b)
        {
            if (b == 0)
                return a;
            long init = a;
            while (b != 1)
            {
                a *= init;
                b -= 1;
            }

            return a;
        }

        public static bool IsArmstrong(int n)
        {
            int m = n;
            if (n < 10)
                return true;
            int init = n;
            long res = 0;
            while (init >= 1)
            {
                res += 1;
                init /= 10;
            }

            long somme = 0;
            for (int i = 1; i <= res; i++)
            {
                somme += Power(n%10, (ulong) res );
                n /= 10;
            }
            return somme==m;
        }

        public static float Abs(float n)
        {
            if (n < 0)
                return -n;
            return n;
        }

        public static float Sqrt(float n)
        {
            if (n < 0)
            {
                Console.WriteLine("sqrt : nombre negatif");
                return 0;
            }

            double S = n;
            double X = S;
            
            for (float i = 0; i < n; i++)
            {
                X = 0.5 * (X + S / X);
            }
            return (float) X;

        }

        public static void PrintEgg(uint n, string pattern)
        {
            int j = 1;
            int k = 3;
            for (int i = 0; i <= n+1; i++)
            {
                int ind_j;
                if (i == n)
                {
                    ind_j = j-2;
                    while (ind_j != 0)
                    {
                        Console.Write(pattern[0]);
                        ind_j -= 1;
                    }
                    Console.Write("\n");
                }
                else if (i == n + 1)
                {
                    ind_j = j-4;
                    Console.Write(" ");
                    while (ind_j != 0)
                    {
                        Console.Write(pattern[1]);
                        ind_j -= 1;
                    }
                }
                else
                {
                    ind_j = j;
                    int ind_k1 = k;

                    while (ind_k1 != 0)
                    {
                        Console.Write(" ");
                        ind_k1 -= 1;
                    }

                    while (ind_j != 0)
                    {
                        Console.Write(pattern[i]);
                        ind_j -= 1;
                    }

                    Console.Write("\n");
                    j += 2;
                    k -= 1;
                }
            }
        }
        
        public static void PrintRoundedEgg(int r, string pattern)
        {
            throw new NotImplementedException();
        }

        public static int Syracuse(uint n)
        {
            throw new NotImplementedException();
        }
    }
}
