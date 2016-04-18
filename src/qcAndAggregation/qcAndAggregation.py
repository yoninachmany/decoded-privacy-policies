import csv

paragraphToQuestionsToVotesMap = {}
questions=["are_they_making_money_off_the_data",
  "can_they_access_other_data_on_your_phone_without_your_permission",
  "can_they_track_your_search_history_outside_of_the_service",
  "can_you_opt_out_of_sections_of_the_policy",
  "did_the_text_address_any_of_the_above_questions",
  "do_they_protect_information_about_children",
  "do_they_sell_demographic_information",
  "do_they_sell_geolocation_data",
  "do_they_sell_your_data_to_just_anyone",
  "do_they_sell_your_data_to_trusted_3rd_parties",
  "do_you_own_the_pictures_you_post",
  "if_you_delete_your_account_is_your_data_deleted",
  "is_data_provided_to_law_enforcement",
  "is_your_sensitive_financial_data_protected",
  "will_this_company_use_your_data_in_advertising",
  "can_you_opt_out_of_sections_of_the_policy_gold",
  "did_the_text_address_any_of_the_above_questions_gold"]

with open('data/qc/sampleInput/HITDesign2Report.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        paragraph = row['text']
        if paragraph not in paragraphToQuestionsToVotesMap:
            paragraphToQuestionsToVotesMap[paragraph] = {}
            for question in questions:
                paragraphToQuestionsToVotesMap[paragraph][question] = 0
        else:
            qcResponse = row['did_the_text_address_any_of_the_above_questions']
            shouldBoxBeChecked = False
            isBoxChecked = False
            for question in questions:
                response = row[question]
                if response is True:
                    isBoxChecked = True

            if shouldBoxBeChecked is not isBoxChecked:
                continue

            for question in questions:
                response = row[question]
                paragraphToQuestionsToVotesMap[paragraph][question] += 1


with open('data/qc/sampleOutput/paragraphToLabel.csv', 'w') as csvfile:
    fieldnames = questions[:]
    fieldnames.append('paragraph')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for paragraph in paragraphToQuestionsToVotesMap:
        row = {'paragraph': paragraph}
        for question in questions:
            votes = paragraphToQuestionsToVotesMap[paragraph][question]
            if votes >= 6:
                row[question] = "Yes"
            elif votes == 5 or votes == 4:
                row[question] = "Maybe"
            else:
                row[question] = "No"

        writer.writerow(row)
