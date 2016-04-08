# decoded-privacy-policies
> Decoded uses crowdsourcing to analyze and outline the contents of the Privacy Polices of several popular companies to shed light on what consumers are actually agreeing to.

### The Problem

When buying a product or service, people often agree to ridiculous things online, or even sign away rights they aren’t aware of, because they don’t take the time to read 20 page Privacy Policies. Generally, policies are much better reading material for lawyers than for the people they are supposed to inform. This project will give them the gist of what they are agreeing to, and hopefully incentivize companies to make their policies more clear to consumers.


## 1. /data (5 total)
**Raw data input (1)**

Privacy policies will be gathered from several tech companies, which are easily available in machine-readable form e.g. http://www.apple.com/privacy/privacy-policy/

Right now, there are policies from Apple, Craigslist, Google, Instagram, Thew New York Times, and Twitter, in text form, for parsing and pdf form for display reference in https://github.com/yoninachmany/decoded-privacy-policies/tree/master/data/rawInput

**Sample input/output from QC module (2)**

Though the raw data input consists of an entire privacy policy, the sample input from the quality control module that is shown in our repo is the materials for the HIT that was built on Crowdflower. In that respect, the sample input from the quality control module is the input to crowdworkers, who are selected using quality control methods. Those methods include requiring workers to be English speakers (to read English privacy policies), employing 10 workers for a HIT, and paying workers $0.10/HIT now (which seems like a more significant payment for a more cognitively challenging task, though we are willing to raise our payment if we believe it will be helpful).

HIT design is also part of QC, as the clarity and brevity of our instructions and task are key to allowing workers to perform better. Our original approach to the project was to have crowdworkers summarizing paragraphs of legal documents, which was overly ambitious and unwise, as getting useful output would be difficult, and the workflow for workers would not be very deterministic. We transitioned to a set of checklist items for workers to look for in paragraphs of privacy policies:

* Will your data be used in advertising?
* Are they making money off the data?
* Do they sell geolocation data?
* Do they sell demographic information? 
* Do you own the pictures you post?
* Can you opt out of sections of the policy?
* If so do you lose access to parts of the service
* Can they track your search history outside of the service?
* Is data provided to law enforcement?
* Is sensitive financial data protected?
* Is censorship allowed?
* Can they access other data on your phone without your permission?
* If you delete your account, is your data deleted?

Such a structure also paves the way for clearly-defined quality control questions to filter workers as good or bad.

The output from the HIT are two data (report) files downloaded from Crowdflower, which serve as the results yielded from workers selected using quality control methods.

Our quality control methods overlap highlight with aggregation, which will be explained more in-depth below.

**Sample input/output from your aggregation module (2)**

The sample input for aggregation comes from the sample output for quality control, which is the data report from Crowdflower, with information about paragraphs and worker quality. The output is achieved by running the aggregation code on the HIT output.

The intersection between the modules is pretty high. In sum, here are the measures we are taking for successful quality control and aggregation:

* Reading privacy policies on our own to understand the task better
* Coming up with clear checklist items of things we expect to find in privacy policies
* Gold standard questions with clear qualities marked
* Choosing reasonable sized paragraphs from privacy policy document
* Filtering workers who may participate on our HIT to be English speakers
* Employing 10 workers on HITs and paying them $0.10 or more depending on our results
* Using gold standard questions to assess worker quality (mostly done on crowdsourcing platform)
* Playing with the HIT parameters (length of policy we give to read, number of attributes, number of chunks we have them each do, etc)
* Potentially moving from Crowdflower to Mechanical Turk to get better results

## 2. /src (4 total)
**Working QC module (2)**

The initial approach for quality control was a simple majority for descriptions of sections of the document. The approach was to be tested with a small trial that would identify the benefits and disadvantages of such an approach. Potential paths forward included adding an additional pass to throw out bad answers that should not be voted on or iterative writing of descriptions.

After meeting with our TA, we changed the design of the HIT, including the output format from each task, which was now purely voting on paragraph meaning using a pre-defined checklist. Therefore, quality control moving forward follows these steps:

* For each chunk “decoded” by 10 workers, at least 6 have to agree on each checkbox for it to be considered valid
* If 4-5 people label a chunk with a given checkbox, we check on it manually - don’t want automatically discount, but can’t be sure
* If there is disagreement (many votes for several conflicting labels for a paragraph) we also give it a second pass

**Working aggregation (2)**

Given simulated data, the appropriate descriptions for a section of the Privacy Policy will be chosen and then a final version of the output will be created by appending descriptions in the order of the original sections. In the final version, more work may be required to clean and parse simulated data.

## 3. HIT Prototype (8 total)
* Privacy Policies documents will need to be chunked before inserting them into HITs to ensure logical breaks. (1)
* Price, redundancy, and potential gold standard data will need to be determined. Crowd will need to speak English and may have comprehension tested. (1)
* Crowd touches data by reading small chunks of Privacy Policies and translating into high-level explanation, potentially in an iterative manner. (4)
* A small trial will be run to analyze the quality of a simple majority approach and refine the design iteratively. (2)

## 4. Online Resource (3 total)
* Ultimately, the project will result in an online resource that posts crowdsourced summaries alongside original Privacy policies, to provide consumers with the knowledge of what they’re signing when they agree to use services. (3)

## Q&A for reference
**Who will be the members of your crowd?**

This project will use Mechanical Turk workers to decode what our chosen policies are actually saying by breaking up each policy into segments and having each section summarized by a set of workers, after which another group of workers will determine which of those summaries best encapsulates the content of the section.

**How will you incentivize them to participate?**

We will pay these workers a small sum to participate. There may be a small amount of intrinsic motivation involved as well; a lack of understanding of privacy policies is a problem that affects many internet users, and it’s possible that Turkers will feel that they’re contributing to a worthwhile cause.

**What will they provide, and what sort of skills do they need?**

Turkers will help us determine the main point of a small section of a privacy policy. They will need to speak english and have sufficient analytical and reading comprehension skills to understand what is being stated in the policy. (easier said than done- many policies are primarily written in legal-ese!)

**How will you ensure the quality of the crowd provides? How will you aggregate the results from the crowd?**

We will ultimately create an online resource that posts our crowdsourced summary alongside the original privacy policy, to provide consumers with the knowledge of what they’re signing when they hit “Agree”.

**Describe each of the steps involved in your process. What parts will be done by the crowd, and what parts will be done automatically.**

1. We’ll first have to divide up the privacy policy into different sections, ensuring that the divisions occur at logical breaks in the policy. We will use a machine to do this.
2. We will then survey Mechanical Turk workers and ask them what they think the paragraphs mean. These hits will be run in an iterative process with built in gold-standard questions and multiple summaries written per section. We will encourage Turkers to be as clear and concise as possible in their summaries.
3. Finally, we will add together the summaries for each section and post them onto Mechanical Turk, asking Turkers to mark similar concepts and further summarize the implications for this category. We’ll also build in quality control on this step to ensure that Turkers are writing summaries and voting conscientiously.

**How will you evaluate if your project is successful?**

This project will be successful if we can get Turkers to reliably interpret and summarize the meaning of sections of these privacy policies, and if we are further able to combine these summaries into a useful resource for consumers.

**What potential problems do you foresee when implementing your project?**

We might encounter issues if Turkers are unable to truly understand the legal language that is used in many of these privacy policies, and thus are unable to further explain it clearly to others. This may be problematic for accurately decoding the policies.
Provide a link to your Vimeo video *
