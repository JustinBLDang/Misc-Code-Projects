using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Switch_Statements
{
	class Program
	{
		static void Main(string[] args)
		{
			
			Console.WriteLine("Please enter your age:");
			string input = Console.ReadLine();
			int Age = int.Parse(input);

			switch(Age)
			{
				case 15:
					Console.WriteLine("Too young to party in the club!");
					break;
				case 25:
					Console.WriteLine("Good to go!");
					break;
				default:
					Console.WriteLine("How old are you then?");
					break;
				
			}
			// switch statement written as if statements
			
			if(Age <= 21)
			{
				Console.WriteLine("Dunno buddy, you kinda underage");
			}
			if (Age >= 21)
			{
				Console.WriteLine("Go ham");
			}
			else
			{
				Console.WriteLine("Please specify your age:");
			}
			Console.Read();
		}
	}
}
