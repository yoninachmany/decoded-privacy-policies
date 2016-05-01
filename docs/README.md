# decoded-privacy-policies
> Decoded uses crowdsourcing to analyze and outline the contents of the Privacy Policies of several popular companies to shed light on what consumers are actually agreeing to.

### The Problem

When signing up for a product or service, people often agree to ridiculous things online, or even sign away rights they aren’t aware of, because they don’t take the time to read long Privacy Policies. Generally, policies are much better reading material for lawyers than for the people they are supposed to inform. This project will give consumers the gist of what they are agreeing to, and hopefully incentivize companies to make their policies more clear to their users.

### Running the code
From the base directory (https://github.com/yoninachmany/decoded-privacy-policies/), run the following commands:
* `python src/qc.py` runs quality control as follows: it reads in the Final Report from `data/qc/sampleInput/`, checking whether or not people correctly answered a question that helps guard against randomly answering questions. Afterwards, it performs a majority vote system and writes the results to another csv that, for every paragraph, indicates the crowd's answer for the questions about the paragraph. 
* `python src/aggregation.py` runs aggergation by combining paragraphs from the same company and writing that a company does or does not mention a certain issue, with a paragraph justifying the answer.

## 1. /data (5 total)
**Raw data input (1)**

We've gathered privacy policies from several large tech companies (namely Apple, Craigslist, Google, Instagram, The New York Times, and Twitter), which can be found on their websites:

* http://www.apple.com/privacy/privacy-policy/
* https://www.craigslist.org/about/privacy.policy 
* https://www.google.com/policies/privacy/
* https://www.instagram.com/about/legal/privacy/ 
* http://www.nytimes.com/content/help/rights/privacy/policy/privacy-policy.html
* https://twitter.com/privacy?lang=en

We've uploaded these policies in text form for parsing and in pdf form for display reference in https://github.com/yoninachmany/decoded-privacy-policies/tree/master/data/rawInput

**Sample input/output from QC module (2)**

We've broken each policy into paragraph "chunks", and used these chunks as input to the quality control module (shown in our repo under data/rawInput). For this project, we've incorporated quality control in our CrowdFlower HIT as well as in our aggregation step, rather than doing a separate QC task. One of the most important parts of our project is a list of questions we compiled to have workers search for in each privacy policy. After reading quite a few privacy policies, we identified privacy and data use issues that consumers care about and that are addressed in many policies. These questions include: 

* Will this company use your data in advertising?
* Are they making money off the data?
* Do they sell your data to trusted 3rd parties?
* Do they sell your data to just anyone?
* Do they sell geolocation data?
* Do they sell demographic information?
* Do you own the pictures you post?
* Can you opt out of sections of the policy?
* Can they track your search history outside of the service?
* Is data provided to law enforcement?
* Is your sensitive financial data protected?
* Can they access other data on your phone without your permission?
* If you delete your account, is your data deleted?
* Do they protect information about children?

The clarity and brevity of our instructions and task are key to allowing workers to perform better, so we went through several iterations of HIT designs before landing on our final design. Our original approach to the project was to have crowdworkers summarizing paragraphs of legal documents, but we realized this was overly ambitious and unwise- it was unlikely that the majority of workers would actually take the time to give us any useful output, and we had no way of screening these summaries for quality control. 

Once we decided to have workers search for answers to the questions above in each policy chunk, we tried two different HIT formats, with different forms of quality control embedded. We attempted to make the tasks as simple as possible for workers, in order to motivate them to actually do the HIT (rather than spam us). Our first HIT design (seen in docs/screenshots/newDesign1-radioButtons) included buttons to note "Yes", "No", "It is not mentioned in this text", and "I can't tell" for each question, but we found that this made it too easy for workers the ability to just click the same answer to answer every question (i.e. "Yes" to every one). 

We adapted this design by creating a new HIT design with simple checkboxes next to each question (seen in docs/screenshots/newDesign2-checkboxes), instructing workers to check the questions that are addressed in the text provided. As a means of quality control, we also included a required question at the end asking users to check "Yes" if the text addressed any of the questions and they checked them accordingly, or "No" if the text didn't address any of the questions, and they left all questions unchecked. (This allowed us to immediately throw out any data that checked some of the questions, yet noted "No" for this final question). 

For the QC module output, we've uploaded the two CrowdFlower data (report) files from these two HITs, which show the results we got from workers. HIT Design 2 is the one we've chosen to use moving forward.

As we noted above, our quality control methods overlap with how we're aggregating our data, which will be explained more in-depth below.

**Sample input/output from your aggregation module (2)**

The sample input for aggregation comes from the sample output for quality control, which is the data report from Crowdflower, with information about paragraphs and worker quality. The output is achieved by running the aggregation code on the HIT output.

The intersection between the modules is pretty high. In sum, here are the measures we are taking for successful quality control and aggregation:

* Reading privacy policies on our own to understand the what questions an ideal policy would answer
* Coming up with clear checklist items of things we expect to find in privacy policies
* Gold standard questions with clear qualities marked
* Choosing reasonable sized paragraph "chunks" from each privacy policy document
* Only allowing English speaking workers to participate in our HIT 
* Employing 10 workers on HITs and paying them $0.10 (the exact amount may change, depending on our results)
* Using gold standard questions to assess worker quality (mostly done on crowdsourcing platform)
* Playing with the HIT parameters (length of policy we give to read, number of attributes, number of chunks we have them each do, etc)

## 2. /src (4 total)
**Working QC module (2)**

When we originally designed HITs that had workers summarize sections of privacy policies, our approach for quality control was to upload a 2nd round HIT that would use a simple majority vote to pick out the best of these summaries for each section. Potential paths forward included adding an additional pass to throw out bad answers that should not be voted on or iterative writing of descriptions.

After meeting with our TA, we changed the design of the HIT (as described in detail above in "Sample input/output from QC module"), including the output format from each task, which was now purely voting on the content of given text using a pre-defined checklist of questions. Apart from the quality control we embedded in the actual HIT, quality control moving forward follows these steps:

* Each chunk is seen by 10 workers, who check the boxes next to the questions that the text addresses. 
* For each chunk “decoded” by 10 workers, at least 6 have to agree on each checkbox for it to be considered valid
* If 4-5 people label a chunk with a given checkbox, we will check on it manually - don’t want automatically discount those 4-5 workers, but can’t be sure
* If 3 or fewer workers agree on a checkbox, we assume that question isn't addressed in the chunk. 
* If there is significant disagreement (many votes for several conflicting labels for a paragraph) we also give it a second pass

**Working aggregation (2)**

Given final CrowdFlower data from workers, the code above will layer the attributes (boxes checked) for each paragraph chunk of each policy together, in order to determine which questions the policy answers in total. Our output will be a list of questions each policy addresses, and links to different paragraphs of original policy for reference (the text where each question is actually answered). In the final version, more work may be required to clean and parse simulated data, but we think the quality control we implement in each step will go a long way to make this final aggregation step fairly straightforward. 

## 3. HIT Prototype (8 total)
* Input: Privacy Policies documents manually chunked before inserting them into HITs to ensure logical breaks. (1)
* Create list of questions (i.e., questions an ideal privacy policy would answer) for workers to search for in each policy (1)
* Price, redundancy, and gold standard data will be determined. Crowd will need to speak English, do the gold standard tasks correctly, and pass internal HIT QC (check "Yes" if did check boxes, "No" if not) in final checkbox HIT design. (1)
* Crowd touches data by reading small chunks of Privacy Policies and checking boxes next to the questions the text addresses. (3)
* A small trial will be run to analyze the quality of a simple majority approach and refine the design iteratively. (2)

## 4. Online Resource (3 total)
* Ultimately, the project will result in an online resource that shows the qualities of each privacy policy (shows if they use your data in advertising, if they protect sensitive financial information, etc), and links to sections of the actual policy where we found this information. This will go a long way in quickly helping users understand what they’re signing when they agree to use services, without them having to read the entire policy. We'll also be able to compare the policies of companies to each other, adding a further level of utility to this model. (3)

## Q&A for reference
**Who will be the members of your crowd?**

This project will use Crowdflower workers to decode our chosen privacy policies by asking them to read small sections of a policy, and check a box next to any of our questions of interest that the section answers.

**How will you incentivize them to participate?**

We will pay these workers a small sum to participate. There may be a small amount of intrinsic motivation involved as well; a lack of understanding of privacy policies is a problem that affects many internet users, and it’s possible that workers will feel that they’re contributing to a worthwhile cause.

**What will they provide, and what sort of skills do they need?**

Turkers will help us determine the main point of a small section of a privacy policy. They will need to speak English and have sufficient analytical and reading comprehension skills to understand what is being stated in the policy. (easier said than done- many policies are primarily written in legal-ese!)

**How will you ensure the quality of the crowd provides? How will you aggregate the results from the crowd?**

We will have multiple layers of quality control embedded in our HIT and methods of aggregation - we will have 10 workers "decode" each chunk of policy and use a majority vote system based on the boxes they check to determine which questions are actually answered. We'll have each worker answer gold standard questions as well, and throw out any spammers (those who check all the boxes, etc). 

To aggregate the data, we will write a program to combine the questions our workers reported were answered for each chunk to form a list of questions that the entire policy answers, as well as the associated chunks text where those questions were addressed. 

**How will you evaluate if your project is successful?**

This project will be successful if we can get Turkers to reliably interpret the meaning each section of these privacy policies, and if we can coherently combine the data from each chunk into a larger resource that notes the ways that companies are actually using consumer data.

**What potential problems do you foresee when implementing your project?**

We might encounter issues if workers are unable to truly understand the legal language that is used in many of these privacy policies, and thus are unable to label the paragraphs accurately.
