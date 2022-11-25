using System;

namespace StackVsHeap3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var maxAge = 99;
            var dateOfBirth = new DateTime(1900, 05, 01);
            var calculateAge = () =>
            {
                var today = DateTime.Today;
                var age = today.Year - dateOfBirth.Year;

                if (dateOfBirth.Date > today.AddYears(-age))
                    age--;

                return age;
            };

            var age = calculateAge();

            if (age >= maxAge)
                Console.WriteLine($"Are you sure you are {age}?");
            else
                Console.WriteLine(age);
        }

    }
}



