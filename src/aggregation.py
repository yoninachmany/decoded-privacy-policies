import csv

companyToQuestionsToResponsesMap = {}
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

companyToQuestionToYesParagraphMap = {}

with open('analysis/data/qc/realOutput/paragraphToLabel.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        company = row['company']
        if company not in companyToQuestionsToResponsesMap:
            companyToQuestionsToResponsesMap[company] = {}
            companyToQuestionToYesParagraphMap[company] = {}
            for question in questions:
                companyToQuestionsToResponsesMap[company][question] = "No"
                companyToQuestionToYesParagraphMap[company][question] = ""

        paragraph = row['paragraph']
        for question in questions:
            response = row[question]
            if response == "Yes":
                companyToQuestionsToResponsesMap[company][question] = "Yes"
                companyToQuestionToYesParagraphMap[company][question] = paragraph

with open('analysis/data/aggregation/realOutput/companyQuestionResponsesAndYesParagraphs.csv', 'w') as csvfile:
    fieldnames = ['company'] + questions
    for question in questions:
        newFieldname = question + "_yes_paragraph"
        fieldnames.append(newFieldname)

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for company in companyToQuestionsToResponsesMap:
        row = {'company': company}
        for question in questions:
            response = companyToQuestionsToResponsesMap[company][question]
            paragraph = companyToQuestionToYesParagraphMap[company][question]
            if paragraph is "":
                paragraph = "None"
            row[question] = response
            row[question + "_yes_paragraph"] = paragraph

        writer.writerow(row)
