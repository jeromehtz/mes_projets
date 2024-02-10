using System;

namespace Basics
{
    public class Basics
    {
        public static void Swap(ref int a, ref int b)
        {
            (a,b) = (b,a);
        }

        public static void FeverCheck(double temperature, ref int counter)
        {
            if (temperature >= 36.5 && temperature <= 37.5)
                counter+=1;
        }

        public static int Euclidean(ref int dividend, int divisor)
        {
            int q = 0;
            do
            {
                q += 1;
                dividend -= divisor;
            } while (dividend>=divisor);

            return q;
        }

        public static int Max(int[] array)
        {
            if (array == null)
                return -1;
            int max = array[0];
            int indice = 0;
            for (int i=1; i<array.Length; i++)
            {
                if (max < array[i])
                {
                    indice = i;
                    max = array[i];
                }
            }
            return indice;
        }

        public static int HealthyInCrowd(double[] temperatures)
        {
            int counter = 0;
            for (int i = 0; i < temperatures.Length; i++)
            {
                FeverCheck(temperatures[i], ref counter);
            }

            return counter;
        }

        public static void RotChar13(ref char c)
        {
            // FIXME
            throw new NotImplementedException();
        }

        public static void Rot13(char[] array)
        {
            char c;
            for (int i=0; i<array.Length; i++)
            {
                int ascii = array[i];
                if (ascii >= 65 && ascii <= 90 || ascii >= 97 && ascii <= 122)
                {
                    ascii += 13;
                    if (ascii > 127)
                    {
                        ascii -= 128;
                        c = (char) ascii;
                        array[i] = c;
                    }
                    c = (char) ascii;
                    array[i] = c;
                }
                else
                {
                    Console.WriteLine((i,false));
                }
            }
        }

        public static bool IsHill(int[] array)
        {
            // FIXME
            throw new NotImplementedException();
        }

        public static int KingOfTheHill(int[] array)
        {
            /* un seul max
             si le max est présent plusieurs fois -> -1
             */

            int max = array[0];
            int counter = 1;
            for (int i = 1; i < array.Length; i++)
            {
                if (array[i] > max)
                {
                    max = array[i];
                    counter = 1;
                }
                else if (array[i] == max)
                {
                    counter += 1;
                }
            }

            if (counter == 1)
            {
                return max;
            }

            return -1;
        }

        public static void InsertionSort(int[] array)
        {
            for (int i = 1; i < array.Length; i++)
            {
                int j = i;
                int valeur = array[j];
                while (j!=1 && array[j - 1] < valeur)
                {
                    Swap(ref array[j-1] ,ref valeur);
                    j -= 1;
                }
            }
        }
    }
}