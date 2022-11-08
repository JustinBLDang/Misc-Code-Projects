using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PropertiesC
{
	class Box
	{
		// member variable
		private string color = "white";
		public int length;
		public int height;
		//public int width;
		public int volume;

		// auto - implemented property - enter "prop" + press tab twice
		public int Width { get; set; }

		public Box(int length, int height, int width)
		{
			this.length = length;
			this.height = height;
			this.Width = width;
		}



		public int Volume
		{
			get
			{
				return Height * Width * Length;
			}

			set
			{
				volume = value;
			}
				
		
		}
		public int Height
		{
			get
			{
				return height;
			}
			set
			{
				if (value < 0) //throw new Exception("Size should be positive");
					Console.WriteLine("A negative value has been inputed and has been changed to positive");
					value = -value;
				height = value;
			}
		}
		
		public int Length
		{
			get => length;

			set => length = value;
		}

		


		/* one way you can do this is by doing the following:
		--------------
		public void SetLength(Int length)
		{
			this.length = length
		}
		---------------
		and then set the variable as 
		
		private int length;
		---------------

		public int GetLength()
		{
			return this.length;
		}
		
			 
		*/
		public int FrontSurface
		{
			get { return height * length; }
		}
		public void DisplayInfo()
		{
			Console.WriteLine("Length is {0} and heigth is {1} and width is {2} so the volume is {3}",
				Length, Height, Width, volume = Width*Height*Length);
		}
	}


}
