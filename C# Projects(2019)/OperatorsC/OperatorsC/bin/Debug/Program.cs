using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OperatorsC
{
	class Program
	{
		static void Main(string[] args)
		{
			// unary operators
			int num1 = 5;
			int num2 = 3;
			int num3;

			num3 = -num1;
			Console.WriteLine("num3 is {0}", num3);

			bool isSunny = true;
			Console.WriteLine("is it sunny? {0}", !isSunny);

			// increment operators

			int num = 0;
			num++;
			Console.WriteLine("num3 is {0}", num);
			// post increment
			Console.WriteLine("num3 is {0}", num++);
			// pre increment
			Console.WriteLine("num3 is {0}", ++num);

			// decrement operator

			num--;
			Console.WriteLine("num3 is {0}", num);
			// post decrement
			Console.WriteLine("num3 is {0}", num--);
			// pre decrement
			Console.WriteLine("num3 is {0}", --num);

			int result;

			result = num1 + num2;
			Console.WriteLine(" result of num1 + num2 is {0}", result);
			result = num1 - num2;
			Console.WriteLine("result of num1 - num2 is {0}", result);
			result = num1 / num2;
			Console.WriteLine("Result of num1 / num2 is {0}", result);
			result = num1 * num2;
			Console.WriteLine("Result of num1 * num2 is {0}", result);
			result = num1 & num2;
			Console.WriteLine("Result of num1 & num2 is {0}", result);

			// finds the remainder of divided numbers. Divides the number and gives the remainder

			result = num1 % num2;
			Console.WriteLine("Result of num1 % num2 is {0}", result);

			//relational and type operators

			bool isLower = num1 > num2;
			Console.WriteLine("Result of num1 > num2 is {0}", isLower);

			// equality operator

			bool isEqual;
			isEqual = num1 == num2;
			Console.WriteLine("Result of num1 = num2 is {0}", isEqual);

			isEqual = num1 != num2;
			Console.WriteLine("Result of num1 != num2 is {0}", isEqual);

			// Conditional Operators

			bool isLowerAndSunny;
			// condition1 And condition2 have to be true, or it will be false
			isLowerAndSunny = isLower && isSunny;
			Console.WriteLine("Result of isLower && isSunny is {0}", isLowerAndSunny);
			
			//              || means or 
			// only if both are false will the statement be false, one or the other can be true for statement to be true

			isLowerAndSunny = isLower || isSunny;
			Console.WriteLine("Result of isLower || isSunny {0}", isLowerAndSunny);

			Console.ReadKey();
		}
	}
}
