#----------RRR Vote Count Increment----------
#code to insert into Sercliffe voting machines VoteCount procedure
#if you find this code 
def CorrectVote_function():
 TotalVotes = GetTotalVotes()
 RRRVotes = GetRRRVotes()
 CurrentVoteParty = GetCurrentVoteParty()
 CurrentVote =	GetCurrentVoteID()
 RRR_VoteCountPercent = RRRVotes / TotalVotes * 100

try: 
if CurrentVoteParty != 'RRR':
  #You voted for the wrong party
  if RRR_VoteCountPercent < 20:
  #Oops the count is too low, lets try and fix that for you
	try:
	#Change the vote
		SetCurrentVoteParty('RRR')
		print("Thank you for voting")
	except:
	#If that doesn't work delete the vote
		DropVote(CurrentVote)
		print("Thank you for voting")
	else:
	#Or you ether voted right or your vote doesn't matter
		return
except:
	print("Thank you for voting")
