import csv

paragraphToQuestionsToVotesMap = {}
questions=["are_they_making_money_off_the_data",
  "can_they_access_other_data_on_your_phone_without_your_permission",
  "can_they_track_your_search_history_outside_of_the_service",
  "can_you_opt_out_of_sections_of_the_policy",
  "conscientious",
  "text_addresses_questions",
  "do_they_protect_information_about_children",
  "do_they_sell_demographic_information",
  "do_they_sell_geolocation_data",
  "do_they_sell_your_data_to_just_anyone",
  "do_they_sell_your_data_to_trusted_3rd_parties",
  "do_you_own_the_pictures_you_post",
  "if_you_delete_your_account_is_your_data_deleted",
  "is_data_provided_to_law_enforcement",
  "is_your_sensitive_financial_data_protected",
  "text_addresses_questions",
  "text_doesnt_address_questions",
  "will_this_company_use_your_data_in_advertising"]

paragraphToCompanyMap = {}

with open('analysis/data/qc/realInput/FullReport2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    numberOfCorrectlyCheckedBoxes = 0
    totalRows = 0
    for row in reader:
        totalRows += 1
        paragraph = row['text']
        if paragraph not in paragraphToQuestionsToVotesMap:
            paragraphToQuestionsToVotesMap[paragraph] = {}
            company = row['company']
            paragraphToCompanyMap[paragraph] = company
            for question in questions:
                paragraphToQuestionsToVotesMap[paragraph][question] = 0
        else:
            textAddressesQuestions = row['text_addresses_questions']
            textDoesntAddressQuestions = row["text_doesnt_address_questions"]
            if textAddressesQuestions == "true" and textDoesntAddressQuestions == "true":
                continue

            isBoxChecked = False
            shouldBoxBeChecked = False

            if textAddressesQuestions == "true":
                isBoxChecked = True

            for question in questions:
                response = row[question]
                if response == "true":
                    shouldBoxBeChecked = True

            if shouldBoxBeChecked is not isBoxChecked:
                continue
            else:
                numberOfCorrectlyCheckedBoxes += 1

            for question in questions:
                response = row[question]
                if response == "true":
                    paragraphToQuestionsToVotesMap[paragraph][question] += 1

    print "Passed Quality Control #2: " + str(numberOfCorrectlyCheckedBoxes)
    print "Total Number of Responses: " + str(totalRows)

with open('analysis/data/qc/realOutput/paragraphToVotes.csv', 'w') as csvfile:
    fieldnames = ['paragraph', 'company'] + questions

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for paragraph in paragraphToQuestionsToVotesMap:
        row = {'paragraph': paragraph, 'company': paragraphToCompanyMap[paragraph]}
        for question in questions:
            votes = paragraphToQuestionsToVotesMap[paragraph][question]
            row[question] = votes

        writer.writerow(row)

with open('analysis/data/qc/realOutput/paragraphToLabel.csv', 'w') as csvfile:
    fieldnames = ['paragraph','company'] + questions

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    votesKept = 0
    allVotes = 0

    writer.writeheader()
    for paragraph in paragraphToQuestionsToVotesMap:
        row = {'paragraph': paragraph, 'company': paragraphToCompanyMap[paragraph]}
        for question in questions:
            votes = paragraphToQuestionsToVotesMap[paragraph][question]
            allVotes += votes
            if votes >= 6:
                row[question] = "Yes"
                votesKept += votes
            elif votes == 5 or votes == 4:
                row[question] = "Maybe"
                votesKept += votes
            else:
                row[question] = "No"

        writer.writerow(row)

    print "Votes Kept: " + str(votesKept)
    print "All Votes: " + str(allVotes)
    print "Fraction of Votes Kept/All Votes: " + str(float(votesKept)/allVotes)
