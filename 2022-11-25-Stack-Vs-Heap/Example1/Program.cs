using System;

namespace StackVsHeap1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var dateOfBirth = new DateTime(1987, 05, 01);
            var age = CalculateAge(dateOfBirth);

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



