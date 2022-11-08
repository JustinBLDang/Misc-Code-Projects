using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Challenge_Loops_1
{
	class Program
	{
		public static void Main(string[] args)
		{
			string input = "0";
			int count = 0;
			int total = 0;
			int currentNumber = 0;

			while(input != "-1")
			{
				Console.WriteLine("Last number was {0}", currentNumber);
				Console.WriteLine("The current total is {0}", total);
				Console.WriteLine("Current amount of entries {0}", count);
				Console.WriteLine("Please enter the next score");
				Console.WriteLine("Type -1 when you have finished");

				input = Console.ReadLine();
				if(input == "-1")
				{
					Console.WriteLine("========================================================");
					// Calculate Average and let the teacher know
					double average = (double)total / (double)count;
					Console.WriteLine("The average is {0}", average);
				}

				if(int.TryParse(input, out currentNumber) && currentNumber > 0 && currentNumber < 21)
				{
					total += currentNumber;
				}

				else
				{
					if (!(input.Equals("-1")))
					{
						Console.WriteLine("Please enter a value between 1 and 20");
					}
					continue;
				}
				count++;
				
			}

			Console.Read();

			




			Console.Read();
		}
	}
}
