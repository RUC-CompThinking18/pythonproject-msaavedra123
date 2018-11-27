# -*- coding: utf-8 -*-

'''questionList is a list that contains, in parenthesis, each question, accompanied by the correct answer
  which is an string. Raw_Input is a string so it is easier to simply tell the user they are incorrect if they enter a letter or an
incorrect answer.'''

def blm3():
	questionList = [
		        ("1. How many citizens were killed in plane crashes in 2017? ", "13"),
				("2. In 2017, how many soldiers died in action around the globe? ", "21"),
				("3. In 2017, how many American died in the United States because of terrorism? ", "4"),
				("4. How many people were killed by mass shooters in 2017? ", "428"),
				("5. How many deaths were caused by Chicago's 'top gangs' in 2017? ", "675"),
				("6. In 2017, how many people were killed by police? ", "987")
	]
	print("Please answer the following questions with whole number only")
	print("\n")
	for question, i in questionList: 		#For each 'question', i refers to the indexes of the list questionList, i.e. each question and answer tuple.
		answer = raw_input(question + '')	#The user input is entered using the raw_input() function and is saved as the variable answer
		if answer == i:						#If the user answer matches the actual answer from the questionList "Correct" will be printed
			print("Correct")
		else:
			print("Incorrect, the answer is " + i + "!")				#Otherwise incorrect will be printed after each question, this occurs even if the answer is a letter to avoid error messages
																#Prints incorrect along with the answer so the user is shocked by the statistcs
	print("\n")
	print("Trayvon Martin                                         Jacob Dominguez                                          Edward Taylor                                      James Edward Ray ")
	print("Terence Crutcher  Samuel DuBose                        Andrew Finch                                             Joshua Barre                                     Vincent Hall ")
	print("Emantic Bradford Jr  Jessie J Quinton                  Kameron Prescott                                         Frederick Ricardo Brown                         Eddie Russel Jr. Eric Higgs")
	print("Sandra Bland             Philando Castile              Michael Wilson                                           Jimmie Montel Sanders                         Kiwi Herring  James Owens")
	print("Freddie Gray                Charles Roundtree          Keita O'Neil                                             Quintas Harris  Tyrese Carlyle               Antwon Springer  Malik Carey")
	print("Eric Garner                  Walter L. Scott           Lawrence Hawkins                                         Brian Easley        Vaughn Shaw             Jarvis Hayes      Desmond Phillips")
	print("Antwon Rose                  Cynthia Fields            Isaac Padilla                                            Paul Jones           Tristan Long          Miguel Richards    Anthony Robinson")
	print("Danny Thomas                  Ronnell Foster           Todd A. Stone                                            Burgon Sealy           Caleb Jackson      Raymond Davis       Jarrett Varnado")
	print("Cameron Hall                Paul Braswell              Jean Pedro Pierre                                        Rodney Cole             Jordan Edwards   Keshawn Wilson       Damien Murray")
	print("Juvon Simon               Michael Brown                Johnnie D. Carter                                        Leroy Brown                Avery Richard  Luke O. Stewart     Marc Brandon Davis")
	print("Haydon Taylor            Jalon Johnson                 Shady Bell                                               Kadeem Torres                Epthen Lamont Johnson            Haraesheo Rice")
	print("Charles Smith Jr.  Anthony Jacob Weber                 Cornell Lockhart                                         Jamal Parks                      Brandon Wiley                Kendell Wilson")
	print("Bruan Ziro  Isaiah Tucker  DeAndre Bethea              Phillip Pitts                                            Shelly Porter                                                 Marcus Williams")
	print("Miguel Richards          Luke O. Stewart               Thomas Aikens                                            Eddie Davis                                                   Jerome Allen")
	print("Malik Carey                 Terry Williams             Jamarco McShann                                          Darryl L. Fuqua                                               Ricky Ard")
	print("Armond Brown                 Anthony Antonio Ford      Christopher Carter                                       Jimmy Briggs                                                  Kerry Bradley")
	print("Corsean Lewis                Ervin Eugene Sweat Jr     Earl Riley                                               Marquis Thomas                                                Keith Price")
	print("Don Johnson                  Dennis Tood Rogers        Nathanial Richmond                                       Gavin Williams                                                Darreon Neal")
	print("Alteria Woods               Charleena Lyles            Medger Blake                                             Herbert Johnson                                               Kenneth Lewis")
	print("Jonie Block               Indian N. Nelson             Ronald Singletary   Cardell Vance II  Aries Clark        Artise Manning                                                Luvelle Kennon")
	print("Lawrence Hawkins  Patrick Earl Gatson                  Shaquian Tyrone Johnson  Keo Crockett William Stokes     Herbert Gilbert                                               Deltra Henderson")
	print("Snady Guardiola  Carianna Hithon                       Jermaine Claybrooks  Luvelle Kennon  Vincent Hall        Kesharn K. Burney                                             Quanice Derrick Hayes")



blm3()
