using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TicTacToe
{
	class Program
	{
		
		public static char[,] board =
		{
				{'1', '2', '3'},
				{'4', '5', '6'},
				{'7', '8', '9'}
		};
		public static char[,] newBoard =
		{
				{'1', '2', '3'},
				{'4', '5', '6'},
				{'7', '8', '9'}
		};
		public static void Board()
		{
			Console.WriteLine("       |       |       ");
			Console.WriteLine("   {0}   |   {1}   |   {2}   ", board[0, 0], board[0, 1], board[0, 2]);
			Console.WriteLine("_______|_______|_______");
			Console.WriteLine("       |       |       ");
			Console.WriteLine("   {0}   |   {1}   |   {2}   ", board[1, 0], board[1, 1], board[1, 2]);
			Console.WriteLine("_______|_______|_______");
			Console.WriteLine("       |       |       ");
			Console.WriteLine("   {0}   |   {1}   |   {2}   ", board[2, 0], board[2, 1], board[2, 2]);
			Console.WriteLine("       |       |       ");
		}
		
		public static void Main(string[] args)
		{
			bool player1Turn = true;
			bool player2Turn = false;			
			bool game = true;
			bool win = false;
			do
			{
				while(player1Turn == true)
				{
					bool wrongInput = false;
					wrongInputFix:
					try
					{
						Console.Clear();						
						Board();						
						Console.Write("Player 1: Choose your field! ");
						string player1Input = Console.ReadLine();
						int choice = int.Parse(player1Input);
						switch (choice)
						{
							case 1:
								if (board[0, 0] != 'O')
								{
									board[0, 0] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}
								break;
							case 2:
								if (board[0, 1] != 'O')
								{
									board[0, 1] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 3:
								if (board[0, 2] != 'O')
								{
									board[0, 2] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 4:
								if (board[1, 0] != 'O')
								{
									board[1, 0] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 5:
								if (board[1, 1] != 'O')
								{
									board[1, 1] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 6:
								if (board[1, 2] != 'O')
								{
									board[1, 2] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 7:
								if (board[2, 0] != 'O')
								{
									board[2, 0] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 8:
								if (board[2, 1] != 'O')
								{
									board[2, 1] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 9:
								if (board[2, 2] != 'O')
								{
									board[2, 2] = 'X';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							default:
								Console.WriteLine("Please enter a number between 0-9");
								Console.ReadKey();
								break;
						}
						if (wrongInput == true)
						{
							wrongInput = false;
							goto wrongInputFix;
						}
						foreach (char c in board)
						{
							if (((board[0, 0] == 'X') && (board[0, 1] == 'X') && (board[0, 2] == 'X'))
								|| ((board[1, 0] == 'X') && (board[1, 1] == 'X') && (board[1, 2] == 'X'))
								|| ((board[2, 0] == 'X') && (board[2, 1] == 'X') && (board[2, 2] == 'X'))
								|| ((board[0, 0] == 'X') && (board[1, 0] == 'X') && (board[2, 0] == 'X'))
								|| ((board[0, 1] == 'X') && (board[1, 1] == 'X') && (board[2, 1] == 'X'))
								|| ((board[0, 2] == 'X') && (board[1, 2] == 'X') && (board[2, 2] == 'X'))
								|| ((board[0, 0] == 'X') && (board[1, 1] == 'X') && (board[2, 2] == 'X'))
								|| ((board[2, 0] == 'X') && (board[1, 1] == 'X') && (board[0, 2] == 'X'))
								)
							{
								Console.Clear();
								Board();
								Console.WriteLine("Player 1 has won!");
								Console.WriteLine("Press anything to continue.");
								Console.ReadKey();															
								win = true;
								player1Turn = false;								
								break;
							}						
							else if (choice >= 9)
							{
							}

							else
							{
								player2Turn = true;
								player1Turn = false;
								if (win == true)
								{
									player1Turn = false;
									player2Turn = false;
								}
							}
						}
					}
					catch (FormatException)
					{
						Console.WriteLine("Please enter a number between 0-9");
						Console.WriteLine("Press anything to continue.");
						Console.ReadKey();
						break;
					}
				}				

				while (player2Turn == true)
				{
					bool wrongInput = false;
					wrongInputFix:

					try
					{
						Console.Clear();
						Board();
						string player2Input;
						Console.Write("Player 2: Choose your field! ");
						player2Input = Console.ReadLine();
						int choice = int.Parse(player2Input);
						switch (choice)
						{
							case 1:
								if (board[0, 0] != 'X')
								{
									board[0, 0] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;																	
							case 2:
								if (board[0, 1] != 'X')
								{
									board[0, 1] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 3:
								if (board[0, 2] != 'X')
								{
									board[0, 2] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 4:
								if (board[1, 0] != 'X')
								{
									board[1, 0] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 5:
								if (board[1, 1] != 'X')
								{
									board[1, 1] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 6:
								if (board[1, 2] != 'X')
								{
									board[1, 2] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 7:
								if (board[2, 0] != 'X')
								{
									board[2, 0] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 8:
								if (board[2, 1] != 'X')
								{
									board[2, 1] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							case 9:
								if (board[2, 2] != 'X')
								{
									board[2, 2] = 'O';
								}
								else
								{
									Console.WriteLine("Pick a different box!");
									Console.WriteLine("Press anything to continue.");
									wrongInput = true;
									Console.ReadKey();
								}

								break;
							default:
								Console.WriteLine("Please enter a number between 0-9");
								Console.WriteLine("Press anything to continue.");
								Console.ReadKey();
								break;
						}
						if(wrongInput == true)
						{
							wrongInput = false;
							goto wrongInputFix;
						}
						foreach (char c in board)
						{
							if (((board[0, 0] == 'O') && (board[0, 1] == 'O') && (board[0, 2] == 'O'))
								|| ((board[1, 0] == 'O') && (board[1, 1] == 'O') && (board[1, 2] == 'O'))
								|| ((board[2, 0] == 'O') && (board[2, 1] == 'O') && (board[2, 2] == 'O'))
								|| ((board[0, 0] == 'O') && (board[1, 0] == 'O') && (board[2, 0] == 'O'))
								|| ((board[0, 1] == 'O') && (board[1, 1] == 'O') && (board[2, 1] == 'O'))
								|| ((board[0, 2] == 'O') && (board[1, 2] == 'O') && (board[2, 2] == 'O'))
								|| ((board[0, 0] == 'O') && (board[1, 1] == 'O') && (board[2, 2] == 'O'))
								|| ((board[2, 0] == 'O') && (board[1, 1] == 'O') && (board[0, 2] == 'O')))

							{
								Console.Clear();
								Board();
								Console.WriteLine("Player 2 has won!");
								Console.WriteLine("Press anything to continue.");
								Console.ReadKey();								
								win = true;
								player1Turn = false;
								break;
							}
							else if (choice >= 9)
							{ }

							else
							{
								player1Turn = true;
								player2Turn = false;
								if (win == true)
								{
									player1Turn = false;
									player2Turn = false;
								}


							}
						}
					}
					catch (FormatException)
					{
						Console.WriteLine("Please enter a number between 0-9");
						Console.ReadKey();
						break;
					}



				}
				

				if (win == true)
				{


					Console.WriteLine("Press any key to play again or enter quit to end the game");
					string play = Console.ReadLine();
					if (play == "quit" || play == "Quit" || play == "QUIT")
					{
						Console.WriteLine("Thanks for playing!");
						Console.ReadKey();
						game = false;
					}
					else
					{
						Reset();
						Console.Clear();
						win = false;
						player1Turn = true;
						
						
					}
				}



			}
			while (game);
			
			





		}
		public static void Reset()
		{
			
			board = newBoard;
			

		}
	}
}
