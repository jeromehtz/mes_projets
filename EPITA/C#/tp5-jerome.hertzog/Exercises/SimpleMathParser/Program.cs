using System;

namespace SimpleMathParser
{
    class Program
    {
        static void Main(string[] args)
        {
            string path_depart = "C:/Users/rejom/Documents/test_depart.txt";
            string path_arrivee = "C:/Users/rejom/Documents/test_arrivee.txt";

            
            //Console.WriteLine(Parser.ParseLine("4 * 2 - 5 / 2"));
            //Parser.ParseFile(path_depart,path_arrivee);
            Parser.ParseFilePremium(path_depart,path_arrivee);

        }
    }
}