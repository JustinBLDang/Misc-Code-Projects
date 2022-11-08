using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MembersC
{
	class members
	{
		// member - private field
		private string memberName;
		private string jobTitle;
		private int salary = 20000;

		// member - public field
		public int age;

		// member - property - exposes JobTitle safely - properties start witha  capital letter
		public string JobTitle
		{
			get
			{
				return JobTitle;
			}
			set
			{
				JobTitle = value;
			}

		}

		// public  member Method - can be called from other classes
		public void Introducing(bool isFriend)
		{
			if (!isFriend)
			{
				SharingPrivateInfo();
			}
			else
			{
				Console.WriteLine("Hi, my name is {0}, and my job title is {1}, I'm {2} years old", memberName, jobTitle, age);
			}
		}

		private void SharingPrivateInfo()
		{
			Console.WriteLine("My salary is {0}", salary);
		}

		// member constructor
		public members()
		{
			age = 31;
			memberName = "Lucy";
			salary = 60000;
			jobTitle = "Developer";
			Console.WriteLine("Object created");
		}

		// member - finalizer - deconstructor
		~members()
		{
			// clean up statements
			Console.WriteLine("Deconstruction of Members object");
			Debug.Write("Deconstruction of Members object");
		}


	}
}
