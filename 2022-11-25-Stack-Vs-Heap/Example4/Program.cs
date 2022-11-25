using System;
using System.Threading.Tasks;

namespace StackVsHeap4
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            var dateOfBirth = new DateTime(1900, 05, 01);
            var ageTask = CalculateAge(dateOfBirth);
            var otherTask = DoSomethingElse();

            await Task.WhenAll(ageTask, otherTask);

            var age = ageTask.Result;

            Console.WriteLine(age);
        }

        private static async Task<int> CalculateAge(DateTime dateOfBirth)
        {
            var today = DateTime.Today;
            var age = today.Year - dateOfBirth.Year;

            await Task.Delay(1000); // Pretending to do work

            if (dateOfBirth.Date > today.AddYears(-age))
                age--;

            return age;
        }


        private static async Task DoSomethingElse()
        {
            Console.WriteLine("Doing some other work");
            await Task.Delay(2000); // Pretending to do work
        }
    }
}



