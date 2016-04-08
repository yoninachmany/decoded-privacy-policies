import csv
import operator
with open('data/qc/f893743.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    paraVoteMap = {}
    for row in reader:
        possibleResponses = ["No",
        "Yes",
        "It_is_not_mentioned_in_this_text",
        "I_can't_tell",
        "The_above_question_isn't_true"]
        questions = ['are_they_making_money_off_the_data',
        'can_they_access_other_data_on_your_phone_without_your_permission',
        'can_they_track_your_search_history_outside_of_the_service',
        'can_you_opt_out_of_sections_of_the_policy',
        'do_they_protect_information_about_children',
        'do_they_sell_data_to_anyone_no_matter_who_they_are',
        'do_they_sell_data_to_trusted_3rd_parties',
        'do_they_sell_demographic_information',
        'do_they_sell_geolocation_data',
        'do_you_own_the_pictures_you_post',
        'if_so_do_you_lose_access_to_parts_of_the_service',
        'if_you_delete_your_account_is_your_data_deleted',
        'is_censorship_allowed',
        'is_data_provided_to_law_enforcement',
        'is_sensitive_financial_data_protected',
        'will_your_data_be_used_in_advertising']
        if row['text'] not in paraVoteMap:
            entry = {}
            for question in questions:
                entry[question] = {}
                for possibleResponse in possibleResponses:
                    entry[question][possibleResponse] = 0
                paraVoteMap[row['text']] = entry
        else:
            for question in questions:
                vote = row[question]
                paraVoteMap[row['text']][question][vote] += 1

    with open('data/qc/output.csv', 'w') as csvfile:
        fieldnames = questions[:]
        fieldnames.append('paragraph')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for entry in paraVoteMap:
            data = {}
            data['paragraph'] = entry
            for question in questions:
                # print question
                o = paraVoteMap[entry][question]
                o['vote'] = max(o.iteritems(), key=operator.itemgetter(1))[0]
                data[question] = o['vote']
                # print data

                writer.writerow(data)
