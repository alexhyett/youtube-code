using System;

namespace StackVsHeap2
{
    internal class Program
    {
        const int MAX_AGE = 99;

        static void Main(string[] args)
        {
            var dateOfBirth = new DateTime(1900, 05, 01);
            var age = CalculateAge(dateOfBirth);

            if (age >= MAX_AGE)
                Console.WriteLine($"Are you sure you are {age}?");
            else
                Console.WriteLine(age);
        }

        private static int CalculateAge(DateTime dateOfBirth)
        {
            var today = DateTime.Today;
            var age = today.Year - dateOfBirth.Year;

            if (dateOfBirth.Date > today.AddYears(-age))
                age--;

            return age;
        }
    }
}



