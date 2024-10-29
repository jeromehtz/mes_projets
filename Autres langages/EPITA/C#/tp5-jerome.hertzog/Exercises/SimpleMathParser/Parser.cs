using System;
using System.Collections.Generic;
using System.IO;

namespace SimpleMathParser
{
    public class Parser
    {
        public enum Symbol
        {
            ADD,
            MINUS,
            MULT,
            DIV
        }
        /*
         * Un fichier est constitué de lignes qui suivent le format suivant :
           1. Un nombre
           2. Un espace
           3. Un symbol mathematique parmi les suivants : ’+’, ’-’, ’*’ et ’/’
           4. Un espace
           5. Un nombre
         */

        public static int Compute(int left, int right, Symbol symbol)
        {
            if (symbol == Symbol.DIV && right != 0)
                return left / right;
            if (symbol == Symbol.DIV && right == 0)
                throw new DivideByZeroException();
            if (symbol == Symbol.ADD)
                return left + right;
            if (symbol == Symbol.MINUS)
                return left - right;
            return left * right;
        }
        
        public static int ParseLine(string inputPath)
        {
            int left = 0;
            Symbol symbol = Symbol.ADD;
            
            //valeurs booleennes :
            bool booleen_right = false;
            bool booleen_symbol = false;
            bool zero_division = false;
            string[] InputPath = inputPath.Split(' ');
            if (InputPath.Length > 3)
            {
                throw new ArgumentException("no more than one operation please");
            }

            for (int i = 0; i < InputPath.Length; i++)
            {
                string c = InputPath[i];
                if (booleen_right == false)
                {
                    try
                    {
                        left = Int32.Parse(InputPath[i]);
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine(e);
                        throw;
                    }

                    booleen_right = true;
                }
                else if (c == "+" && booleen_symbol == false)
                {
                    symbol = Symbol.ADD;
                    booleen_symbol = true;
                }
                else if (c == "-" && booleen_symbol == false)
                {
                    symbol = Symbol.MINUS;
                    booleen_symbol = true;
                }
                else if (c == "/" && booleen_symbol == false)
                {
                    symbol = Symbol.DIV;
                    booleen_symbol = true;
                }
                else if (c == "*" && booleen_symbol == false)
                {
                    symbol = Symbol.MULT;
                    booleen_symbol = true;
                }
                else if (booleen_right && booleen_symbol)
                {
                    try
                    {
                        int right = Int32.Parse(c);
                        left = Compute(left, right, symbol);
                        booleen_symbol = false;
                    }
                    catch (Exception)
                    {
                        Console.WriteLine("Parser error: illegal division by 0");
                        zero_division = true;
                    }
                }
            }

            if (inputPath[0] == ' ' || inputPath[0] == ' ')
                throw new ArgumentException("Parser error: wrong format");
            if (zero_division)
            {
                throw new ArgumentException("Parser error: illegal division by 0");
            }

            return left;
        }

        public static int ParseLineMulti(string inputPath)
        {
            int left = 0;
            Symbol symbol = Symbol.ADD;
            
            //valeurs booleennes :
            bool booleen_right = false;
            bool booleen_symbol = false;
            bool zero_division = false;
            string[] InputPath = inputPath.Split(' ');
            if (InputPath.Length <= 3)
            {
                return 0;
            }

            for (int i = 0; i < InputPath.Length; i++)
            {
                string c = InputPath[i];
                if (booleen_right == false)
                {
                    try
                    {
                        left = Int32.Parse(InputPath[i]);
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine(e);
                        throw;
                    }

                    booleen_right = true;
                }
                else if (c == "+" && booleen_symbol == false)
                {
                    symbol = Symbol.ADD;
                    booleen_symbol = true;
                }
                else if (c == "-" && booleen_symbol == false)
                {
                    symbol = Symbol.MINUS;
                    booleen_symbol = true;
                }
                else if (c == "/" && booleen_symbol == false)
                {
                    symbol = Symbol.DIV;
                    booleen_symbol = true;
                }
                else if (c == "*" && booleen_symbol == false)
                {
                    symbol = Symbol.MULT;
                    booleen_symbol = true;
                }
                else if (booleen_right && booleen_symbol)
                {
                    try
                    {
                        int right = Int32.Parse(c);
                        left = Compute(left, right, symbol);
                        booleen_symbol = false;
                    }
                    catch (Exception)
                    {
                        Console.WriteLine("Parser error: illegal division by 0");
                        zero_division = true;
                    }
                }
            }

            if (inputPath[0] == ' ' || inputPath[0] == ' ')
                throw new ArgumentException("Parser error: wrong format");
            if (zero_division)
            {
                throw new ArgumentException("Parser error: illegal division by 0");
            }

            return left;
        }

        public static void ParseFile(string inputPath, string outputPath)
        {
            using (StreamWriter sw = File.CreateText(outputPath))
            {
                sw.WriteLine();
            }
            StreamReader sr = File.OpenText(inputPath);
            string s;
            while ((s = sr.ReadLine()) != null)
            {
                int res = ParseLine(s);
                if (!File.Exists(outputPath))
                {
                    using (StreamWriter sw = File.CreateText(outputPath))
                    {
                        sw.Write(res);
                    }
                }
                else if (File.Exists(outputPath))
                {
                    using (StreamWriter writer = File.AppendText(outputPath))
                    {
                        writer.WriteLine(res);
                    }
                }
            }
            sr.Close();
        }
        
        public static void ParseFileMulti(string inputPath, string outputPath)
        {
            using (StreamWriter sw = File.CreateText(outputPath))
            {
                sw.WriteLine();
            }
            StreamReader sr = File.OpenText(inputPath);
            string s;
            while ((s = sr.ReadLine()) != null)
            {
                int res = ParseLineMulti(s);
                if (!File.Exists(outputPath))
                {
                    using (StreamWriter sw = File.CreateText(outputPath))
                    {
                        sw.Write(res);
                    }
                }
                else if (File.Exists(outputPath))
                {
                    using (StreamWriter writer = File.AppendText(outputPath))
                    {
                        writer.WriteLine(res);
                    }
                }
            }
            sr.Close();
        }

        public static void ParseFilePremium(string inputPath, string outputPath)
        {
            StreamReader sr = File.OpenText(inputPath);
            string s;
            s = sr.ReadLine();
            if (s == "multi")
            {
                ParseFileMulti(inputPath,outputPath);
            }
            if (s=="single")
                ParseFile(inputPath,outputPath);
        }

        // Bonus
        public static int ParseLinePriority(string line)
        {
            // FIXME
            throw new NotImplementedException();
        }
    }
}
