from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia

def analyse(sentences):
	s = sia()
	for sentence in sentences:
		print("{0}: ".format(sentences.index(sentence) + 1)),
		print(sentence)
		r = s.polarity_scores(sentence)
		for k in sorted(r):
			print("{0}: {1}, ".format(k, r[k])),
		print("\n")


sentences = ["ITF protest  at HQ of #Macquariebank #CondorFerries attack on jobs and TU rights of Polish dockers. 1pm 08/02/16 28 Ropemaker St EC2Y 9HD.",
             "Strange to see #MacquarieBank walk away from #roboadvice on death of inspiration behind it. Surely they would have eager juniors #fintech",
             "Well done to Carol Bailey of @macquariebank, who scored gold in this year's women's 5km Run with a time of 23:56 minutes!",
             "Today I worked with this team of leaders. Lots of robust discussion about strategies required for high performing teams. I know! I have the best job in the world. Thank you for having me #Macquarie #macquariebank #leaders #teams",
			 "People's naivety in investment situations like that of the Lewis' on #abc730 now is depressing but the behaviour of #Macquarie is nothing short of reckless and pernicious. Disgusting. #abc730 #macquariebank",
			 "Was an amazing day at the @YBRWealth 'Woman in Finance...' #event at #macquariebank with @markbouris @lindawcheart @EffieNicol and an amazing group of inspirational woman... raising funds @herheartcharity and she is @entourageoz alumni @JackDelosa #morelloltd",
			 "Cabs circling everywhere at Syd Airport but 45 min wait at cab rank. Has the evil #macquariebank #deathstar had a process failure?",
			 "Why does @ABCNews24 continue to provide free publicity to an organisation like #MacquarieBank?",
			 "Nothing like turning up to speak for a booking that only came through 17 hours ago! #macquariebank #preparingnowforwhatsnext #lastminute",
			 "Leadership discussion Wellbeing as a driver of sustainable high performance. Elizabeth Bradford #HSBC, Sean Carroll, ex #AustraliaPost, Stephen Lyons, #MacquarieBank #wbevent18 #Sydney at Doltone House",
			 "I think it's the #MacquarieBank model: build public infrastructure using public funds that become corporate assets (ie. privatize roads, bridges, airports, etc), collect tolls&fees (ex. Sydney Airport & toll roads), pocket profits.Simple really. Transfer wealth to Bankers."			 		 
			 ]

analyse(sentences)