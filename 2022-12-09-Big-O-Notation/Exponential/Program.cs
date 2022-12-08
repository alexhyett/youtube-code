using System;

namespace Exponential
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(fib(6));
        }

        static int fib(int num)
        {
            if (num <= 1) return num;
            return fib(num - 2) + fib(num - 1);
        }
    }
}



