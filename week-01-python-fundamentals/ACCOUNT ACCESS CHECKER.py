## Getting user information age and verification.
user_Age = int(input("eneter your age: "))
user_identity = input("can you verifiy your identity?, yes or no.")
verified_user_identity = None
valid_reponse = None
## verification based on user response.

if user_identity == "yes" or user_identity == "Yes":
    valid_reponse = True
    verified_user_identity = True

elif user_identity == "no" or user_identity == "No":
    valid_reponse = True
    verified_user_identity = False

else:
    valid_reponse = False


# validility & Account access status
if valid_reponse:
    if  user_Age >= 18 and verified_user_identity:
        print("Account access approved!")
    else:
        print("Account access denied!")
else:
    print("invalid value. please enter the correct response, yes or no.")


## Test Cases

# Test 1 - Valid adult with verified identity      Test: PASS
# Input:
# age = 22
# identity = yes
# Expected output:
# Account access approved!


# Test 2 - Underage user with verified identity    Test: PASS
# Input:
# age = 17
# identity = yes
# Expected output:
# Account access denied!


# Test 3 - Adult with unverified identity    Test: PASS
# Input:
# age = 22
# identity = no
# Expected output:
# Account access denied!


# Test 4 - Boundary age   Test:PASS
# Input:
# age = 18
# identity = yes
# Expected output:
# Account access approved!


# Test 5 - Capitalised yes   Test: PASS
# Input:
# age = 18
# identity = Yes
# Expected output:
# Account access approved!


# Test 6 - Capitalised no Test: PASS
# Input:
# age = 25
# identity = No
# Expected output:
# Account access denied!


# Test 7 - Invalid identity response Test: Fail
# Input:
# age = 22
# identity = maybe
# Expected output:
# invalid value. please enter the correct response, yes or no.