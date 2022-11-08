using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestingErrors
{
	class Program
	{
		static void Main(string[] args)
		{
			
			

			try
			{
				var result = Divide();
				string output = string.Format("The sum of {0} divided by {1} is {2}", result.Item1, result.Item2, result.Item3);
				Console.WriteLine(output);
				Console.Read();

			}
			catch (FormatException)
			{

				Console.WriteLine("Please enter the correct data type");
				
			}
			catch (OverflowException)
			{
				Console.WriteLine("Number was too long or too short");
			}
			catch (ArgumentNullException)
			{
				Console.WriteLine("Impossible Action");
			}
			catch (Exception)
			{
				Console.WriteLine("Cant Do That");
			}
			finally
			{
				Console.WriteLine("Please enter a number");
			}
			Console.ReadKey();

		}
		public static (float, float, float) Divide()
		{
			Console.WriteLine("Please enter the first number:");
			string number1Input = Console.ReadLine();
			Console.WriteLine("Please enter the second number:");
			string number2Input = Console.ReadLine();

			float num1 = float.Parse(number1Input);
			float num2 = float.Parse(number2Input);
			float result = num1 / num2;

			return (num1, num2, result);
			
		}
	}
}
