candidate_f_name = input("Please enter your first name: ")
candidate_l_name = input("Please enter your last name: ")
candidate_prev_occupation = input("Please enter your previous occupation: ")
candidate_experience = int(input("Please enter your experience: "))

# Candidate Qualifies if prev experience is Software Tester and experience is >=5
print("\n1. Nested If")
if(candidate_prev_occupation == "IT Tester"):
    if(candidate_experience >=5):
        print("\tCandidate " + candidate_f_name + " " + candidate_l_name + " is qualified for required experience!")
    else:
        print("\tCandidate " + candidate_f_name + " " + candidate_l_name + " is not qualified for required experience!")
else:
    print("\tCandidate " + candidate_f_name + " " + candidate_l_name + " is not qualified for required position!")

print("\n2. Nested If using operators")
if (candidate_prev_occupation == "IT Tester" and candidate_experience >= 5):
    print("\tCandidate " + candidate_f_name + " " + candidate_l_name + " is qualified for required experience!")
else:
    print("\tCandidate " + candidate_f_name + " " + candidate_l_name + " is not qualified!")
