#to check whether the subsequence is in the given sequence or not

full_string = input()
sub_sequence = input()
sub_sequence_length = len(sub_sequence)

sub_sequence_index = 0

#for checking each character is present in sequence or not

for char in full_string:
	if char == sub_sequence[sub_sequence_index]:
		sub_sequence_index +=1
		if sub_sequence_index == sub_sequence_length:
			break

if sub_sequence_index == sub_sequence_length:
	print ("Yes")
else:
	print ("No")