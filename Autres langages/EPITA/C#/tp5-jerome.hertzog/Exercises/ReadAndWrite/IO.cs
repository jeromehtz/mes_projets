using System;
using System.IO;

namespace ReadAndWrite
{
    public class IO
    {
        public static void WriteFile(string filename, string msg)
        {
            try
            {
                if (!File.Exists(filename))
                {
                    using (StreamWriter sw = File.CreateText(filename))
                    {
                        sw.Write(msg);
                    }
                }
                else if (File.Exists(filename))
                {
                    using (StreamWriter writer = new StreamWriter(filename, false))
                    {
                        writer.Write(msg);
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("WriteFile : Something went wrong.");
                throw;
            }
        }

        public static void ReadFile(string filename)
        {
            try
            {
                StreamReader sr = File.OpenText(filename);
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    Console.WriteLine(s);
                }
                sr.Close();
            }
            catch (Exception)
            {
                Console.WriteLine("ReadFile : Something went wrong.");
                throw;
            }
        }

        public static void MirrorWrite(string inputPath, string outputPath)
        {
            try
            {
                if (File.Exists(inputPath))
                {
                    StreamReader sr = File.OpenText(inputPath);
                    string s;
                    using (StreamWriter sw = File.CreateText(outputPath))
                    {
                        sw.WriteLine();
                    }
                    while ((s = sr.ReadLine()) != null)
                    {
                        string s_ = "";
                        for (int i = 0; i < s.Length; i++)
                        {
                            s_ = s[i] + s_;
                        }
                        Console.WriteLine(s_);
                        using (StreamWriter sw = File.AppendText(outputPath))
                        {
                            sw.WriteLine(s_);
                        }
                    }
                    sr.Close();
                }
            }
            catch (Exception)
            {
                Console.WriteLine("MirrorWrite : Something went wrong.");
            }
        }
    }
}