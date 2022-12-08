using System;

namespace Quadratic
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var n = 10;

            for (int i = 1; i <= n; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    Console.Write("0 ");
                }
                Console.WriteLine();
            }
        }
    }
}



