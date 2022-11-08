using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Class_basics
{
	class Program
	{
		static void Main(string[] args)
		{
			// create an object of my class
			// an instance of human
			Human justin = new Human("jacobi", "Anderson", "blue", 25);
			
			justin.IntroduceMyself();

			Human William = new Human("William", "Nugyen", "brown");

			William.IntroduceMyself();

			Human basicHuman = new Human();

			basicHuman.IntroduceMyself();

			

			Console.Read();
		}


		
	}
}
