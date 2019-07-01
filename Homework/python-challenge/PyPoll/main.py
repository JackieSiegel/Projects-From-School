#PyPoll Jackie

#Import 
import os
import csv

#Load and output
csvpath = os.path.join('election_data.csv')
pathout = os.path.join('output/eldata.txt')



#Set Variables
votes = 0 
candidate_total = 0 
candidates = []  
candidate_votes = {}
max_votes = -1

#Read and convert to dictoniaries 
with open(csvpath) as poll_data:
    reader = csv.DictReader(poll_data)

    for row in reader:
        current_candidate = row['Candidate']
        if current_candidate not in candidates :
            candidate_total = candidate_total + 1
            candidates.append(current_candidate)
            candidate_votes[current_candidate] = 0
        
        candidate_votes[current_candidate]=candidate_votes[current_candidate]+1
        votes = votes + 1
        
        if candidate_votes[current_candidate] > max_votes :
            max_votes = candidate_votes[current_candidate]
            maxcandidate = current_candidate


#For output formatting
line1 = '  Election Results'
line2 = '  -------------------------'
line3 = ('  Total Votes: %d' %(votes))
line4 = '  -------------------------'
output = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

for name in candidates :
    linex = ('  %s: %.3f%% (%d)' %(name,  100*candidate_votes[name]/(0.0+votes), candidate_votes[name]))
    output = output + '\n' + linex

output = output + '\n' + '  -------------------------'
output = output + '\n' + ('  Winner: %s' %maxcandidate)
output = output + '\n' + '  -------------------------'

print(output)
with open(pathout,'w') as txt_file:
        txt_file.write(output)

