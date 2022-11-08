using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Class_basics
{
	// this class is a blueprint for a datatype
	class Human
	{



		// member variable
		private string firstName;
		private string lastName;
		private string eyeColor;
		private int age;

		// default constructor
		public Human()
		{
			Console.WriteLine("Object created");
		}
		// parameterized constructor
		public Human(string firstName)
		{
			this.firstName = firstName;
		}
		public Human(string firstName, string lastName)
		{
			this.firstName = firstName;
			this.lastName = lastName;
		}
		public Human(string firstName, string lastName, string eyeColor)
		{
			this.firstName = firstName;
			this.lastName = lastName;
			this.eyeColor = eyeColor;
		}
		public Human(string firstName, string lastName, string eyeColor, int age)
		{
			this.firstName = firstName;
			this.lastName = lastName;
			this.eyeColor = eyeColor;
			this.age = age;
		}
		
		



		
		// member method
		public void IntroduceMyself()
		{
			if(age != 0 && eyeColor != null && lastName != null && firstName != null)
				Console.WriteLine("HI, Im {0} {1} and I am a {3} year-old with {2} eyes.", firstName, lastName, eyeColor, age);


			else if (age == 0 && eyeColor == null && lastName == null)
							Console.WriteLine("HI, Im {0}.", firstName);
			else if(age == 0 && eyeColor == null)
							Console.WriteLine("HI, Im {0} {1}.", firstName, lastName);
			else if(age == 0)
				Console.WriteLine("HI, Im {0} {1} and I have {2} colored eyes.", firstName, lastName, eyeColor);
			
			



		}



	}
}
